import openai
import os

class TutorAI:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def get_response(self, user_id: str, text: str) -> str:
        # Simple GPT-4o call, can be expanded for context
        if not text:
            return "Please say something for me to help you."
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful AI tutor."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message["content"]
