import os
import requests

api_key = os.getenv("GEMINI_API_KEY")
prompt = "Hello Gemini, test message."

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "contents": [{"parts": [{"text": prompt}]}]
}

response = requests.post(
    "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent",
    headers=headers,
    json=data
)

print(response.status_code)
print(response.text)
