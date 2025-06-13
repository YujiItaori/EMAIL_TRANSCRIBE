import httpx
from config import TOGETHER_API_KEY

def generate_email_content(name, domain, content):
    prompt = f"""
You are writing a professional, personalized email for {name} from {domain}.
Here's the content from their company website:
\"\"\"
{content}
\"\"\"

Your task:
1. Start with a warm opening line about their company.
2. List 4–5 specific issues or improvement opportunities.
3. End with a call to action and sign off as Dave from NetWit.

Use professional tone and keep the email clear and helpful.
"""

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/Llama-3-8b-chat-hf",
        "messages": [
            {"role": "system", "content": "You are a helpful email assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 600,
        "temperature": 0.7
    }

    try:
        response = httpx.post("https://api.together.xyz/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print("LLM error:", e)
        return "LLM failed to generate content."
