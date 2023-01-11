import openai

class OpenAIBackend:
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        openai.api_key = api_key
        self.model = model

    def generate_response(self, prompt):
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error from OpenAI: {e}"
# Simulated change on 2023-01-09 12:52:00
# Simulated change on 2023-01-11 14:34:00
