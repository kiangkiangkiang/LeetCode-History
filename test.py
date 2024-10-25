from openai import OpenAI


class OpenAIModel:
    def __init__(self, **kwargs) -> None:
        """An OpenAI Model Handler"""

        try:
            self.client = OpenAI()
        except Exception as e:
            raise ValueError(f"Cannot initialize OpenAI GPT: {e}")

    def call_model(self, input_text: str, prompt: str):
        """Do invoke openai api

        Args:
            input_text (str): A string denoted as text or question or query.
            prompt (str): Prompt that openai model needs.

        Returns:
            Any: OpenAI model raw response.
        """

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": prompt,
                },
                {
                    "role": "user",
                    "content": input_text,
                },
            ],
        )
        return response


client = OpenAIModel()
result = client.call_model(prompt="你是一個專業的理財機器人", input_text="我想要理財")
print(result)
