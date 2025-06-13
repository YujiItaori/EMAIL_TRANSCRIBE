import requests
from bs4 import BeautifulSoup

def scrape_site(domain):
    try:
        response = requests.get(f"http://{domain}", timeout=10)
        soup = BeautifulSoup(response.text, "lxml")
        content = soup.get_text(separator="\n")
        return content[:5000]  # Limit for prompt size
    except Exception as e:
        return "Could not scrape the website."
    