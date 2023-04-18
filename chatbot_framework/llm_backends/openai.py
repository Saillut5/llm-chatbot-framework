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
# Simulated change on 2023-01-18 15:54:00
# Simulated change on 2023-03-01 12:40:00
# Simulated change on 2023-03-02 10:19:00
# Simulated change on 2023-03-06 12:21:00
# Simulated change on 2023-03-06 17:36:00
# Simulated change on 2023-03-28 10:51:00
# Simulated change on 2023-04-04 13:29:00
# Simulated change on 2023-04-04 18:39:00
# Simulated change on 2023-04-18 10:55:00
