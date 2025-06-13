import os
import httpx
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

def test_together_api():
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/Llama-3-8b-chat-hf",
        "messages": [
            {"role": "user", "content": "What does OpenAI do?"}
        ],
        "max_tokens": 100
    }

    try:
        response = httpx.post("https://api.together.xyz/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        print("✅ API test successful!")
        print("🔍 Model response:\n")
        print(data['choices'][0]['message']['content'])
    except Exception as e:
        print("❌ API test failed!")
        print(e)

if __name__ == "__main__":
    test_together_api()
