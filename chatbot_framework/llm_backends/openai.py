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
# Simulated change on 2023-04-27 17:55:00
# Simulated change on 2023-05-08 17:14:00
# Simulated change on 2023-05-11 09:51:00
# Simulated change on 2023-05-15 18:10:00
# Simulated change on 2023-06-02 12:46:00
# Simulated change on 2023-06-14 11:56:00
# Simulated change on 2023-06-16 10:53:00
# Simulated change on 2023-06-21 12:46:00
# Simulated change on 2023-07-10 18:27:00
# Simulated change on 2023-07-18 15:17:00
# Simulated change on 2023-07-26 16:46:00
# Simulated change on 2023-07-28 16:20:00
# Simulated change on 2023-08-16 09:05:00
# Simulated change on 2023-08-24 09:35:00
# Simulated change on 2023-08-30 11:25:00
# Simulated change on 2023-09-15 14:46:00
# Simulated change on 2023-10-16 15:46:00
