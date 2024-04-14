from image_detection.builder.detection_builder import DectectionBuilder
from image_detection.components.detection import DetectionComponent
from image_detection.components.response import ResponseComponent
from image_detection.constants import PROMPT
import requests


def main(image):

    detection = DetectionComponent(image, PROMPT)
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
