import json
import requests

model = "llama3.2"

systemPrompt = "You are a helpful AI assistant"
prompt = "What are some popular things to do in Detroit?"

url = "http://localhost:11434/api/generate"

payload = {
    "model": model,
    "prompt": prompt,
    "systemPrompt": systemPrompt,
    "stream": False,
    "temperature": 1
}  

payload_json = json.dumps(payload)
headers = {"Content-Type": "application/json"}
response = requests.post(url, headers=headers, data=payload_json)

response_json = json.loads(response.text)["response"]

print(response_json)