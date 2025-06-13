# EMAIL_TRANSCRIBE

EMAIL_TRANSCRIBE is an AI-driven automation tool that intelligently extracts contact and business details from email addresses, scrapes company websites for contextual insights, and generates hyper-personalized, visually appealing HTML emails using LLM-based content generation. The platform is designed to help businesses scale personalized outreach by combining natural language processing, web intelligence, and professional-grade email delivery.

## Features

- Upload or manually input recipient email addresses

- Scrape company websites for additional context

- Generate HTML email content using LLM (via Together.ai)

- Send emails securely via SMTP

- Lightweight and easy-to-use frontend interface

- Fully customizable email templates

## Technologies Used

- **Python (Flask)** – Backend server

- **Together.ai** – LLM API integration

- **HTML/CSS** – Frontend structure and styling

- **SMTP** – Email sending functionality

- **BeautifulSoup / Requests** – Web scraping

- **Git** – Version control

## Folder Structure

EMAIL_TRANSCRIBE/

├── app/

│ ├── static/

│ │ └── style.css

│ ├── templates/

│ │ └── index.html

│ ├── email_generator.py

│ ├── llm_integration.py

│ ├── routes.py

│ ├── scraper.py

│ ├── smtp_mailer.py

│ └── utils.py

├── env/ # Virtual environment (included intentionally)

├── .env # Environment variables (if used)

├── config.py

├── requirements.txt

├── run.py

└── test_together_api.py


## Getting Started

### Clone the Repository


git clone https://github.com/YujiItaori/EMAIL_TRANSCRIBE.git

Note: This project includes a Python virtual environment folder (env/) for convenience. You may also choose to create your own.

## Install Dependencies

After cloning, create a virtual environment (optional) and install required packages:

pip install -r requirements.txt

## Run the Application

python run.py

Then open http://127.0.0.1:5000/ in your browser.




![Screenshot 2025-06-13 085940](https://github.com/user-attachments/assets/50e3dedc-2201-419d-8b33-dd09d79c9a78)
![Screenshot 2025-06-13 090004](https://github.com/user-attachments/assets/cb55da37-ea20-47a8-bbc9-dee73cbe5ec1)
![Screenshot 2025-06-13 090012](https://github.com/user-attachments/assets/f1870dec-95f7-4937-b7bf-5cd01b410eb8)

