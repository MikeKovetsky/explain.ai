import os

from openai import OpenAI

from config import settings

openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)


def process_image(image):
    file_location = os.path.join('/assets', image.filename)
    with open(file_location, "wb+") as file_object:
        file_object.write(image.file.read())
    response = openai_client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What’s in this image?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    return response.choices[0]