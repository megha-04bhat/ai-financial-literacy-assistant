import requests

def generate_response(prompt):
    try:
        url = "http://127.0.0.1:11434/api/generate"

        payload = {
            "model": "llama3",   #  your model
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(url, json=payload)

        # Debug
        print("STATUS:", response.status_code)

        if response.status_code != 200:
            return f"⚠️ Error {response.status_code}: {response.text}"

        data = response.json()

        result = data.get("response")

        if not result:
            return "⚠️ Empty response from llama3"

        return result.strip()

    except Exception as e:
        return f"⚠️ Connection error: {str(e)}"