import requests
import json
from config import GEMINI_API_KEY

def generate_structured_events(fused_data):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key=" + GEMINI_API_KEY
    headers = {"Content-Type": "application/json"}
    prompt = {
    "contents": [{
        "parts": [{
            "text": (
                "Given these news snippets, extract structured events with:\n"
                "- location (specific areas like Whitefield, KR Puram)\n"
                "- event_type (flood, rain, protest, traffic)\n"
                "- time (use published time)\n"
                "- severity (low, medium, high)\n"
                "- image_url\n\n"
                f"Data: {json.dumps(fused_data)}"
            )
        }],
        "role": "user"
    }]
}

    response = requests.post(url, headers=headers, json=prompt)
    return response.json()['candidates'][0]['content']['parts'][0]['text']