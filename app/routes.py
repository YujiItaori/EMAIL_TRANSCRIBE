from flask import Flask, render_template, request, redirect
import pandas as pd
from app.utils import parse_emails
from app.scraper import scrape_site
from app.llm_integration import generate_email_content
from app.email_generator import render_email
from app.smtp_mailer import send_email
from app.email_generator import render_email, format_llm_output

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result_emails = []

    if request.method == "POST":
        emails = []

        if "file" in request.files and request.files["file"].filename:
            df = pd.read_csv(request.files["file"])
            emails = df.iloc[:, 0].tolist()

        manual_emails = request.form.get("emails")
        if manual_emails:
            emails += [e.strip() for e in manual_emails.split(",")]

        for email in emails:
            name, domain = parse_emails(email)
            html_content = scrape_site(domain)
            llm_output_raw = generate_email_content(name, domain, html_content)
            llm_output = format_llm_output(llm_output_raw)
            final_email = render_email(name, domain, llm_output)
            send_email(email, final_email, name)

            # Store for rendering in result
            result_emails.append({"to": email, "html": final_email})

        return render_template("index.html", result_emails=result_emails)

    return render_template("index.html", result_emails=None)
