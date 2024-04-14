import base64
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get("API_KEY")
API_URL = os.environ.get("API_URL")


class DetectionComponent:

    def __init__(self, image, prompt):
        self.__image = self.__encode_image(image)
        self.__prompt = prompt

    def __encode_image(self, image):
        return base64.b64encode(image).decode("utf-8")

    def __make_payload(self, prompt, image, max_tokens):
        return {
            "model": "gpt-4-vision-preview",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{image}"},
                        },
                    ],
                }
            ],
            "max_tokens": max_tokens,
        }

    def receipt_scan(self):

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
        }

        payload = self.__make_payload(self.__prompt, self.__image, 1000)

        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to retrieve data")
