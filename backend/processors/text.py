from openai import OpenAI

from config import settings

openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)


def process_text(text: str):
    try:
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Who won the world series in 2020?"},
                {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                {"role": "user", "content": "Where was it played?"}
            ]
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error in processing text: {str(e)}"
