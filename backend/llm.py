import requests
import os

def query_llm(prompt: str) -> str:
    """
    Sends the prompt to a local Mistral 7B server and returns the response.
    """
    print(f"[LLM] Sending prompt to local Mistral 7B: {prompt}")
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "mistral-7b-instruct",
        "prompt": prompt,
        "stream": False
    }
    try:
        resp = requests.post(url, json=payload, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        response = data.get("response") or data.get("text") or str(data)
        print(f"[LLM] Response: {response}")
        return response
    except Exception as e:
        print(f"[LLM] Error: {e}")
        return f"LLM error: {e}"

# Example usage:
# response = query_llm("What is the capital of France?")
# print(response)
