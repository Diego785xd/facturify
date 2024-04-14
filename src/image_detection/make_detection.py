from image_detection.builder.detection_builder import DectectionBuilder
from image_detection.components.detection import DetectionComponent
from image_detection.components.response import ResponseComponent
from image_detection.constants import PROMPT
import requests


def main(image):
    if image.startswith("http"):
        img = requests.get(image).content
    else:
        img = open(image, "rb").read()

    detection = DetectionComponent(img, PROMPT)
    raw_response = ResponseComponent()
    builder = DectectionBuilder(detection, raw_response)

    builder.process_receipt()
    response = builder.get_response()

    return response


if __name__ == "__main__":
    url = "images/example_01.jpeg"
    response = main(url)
    print(response)
    print(response)
