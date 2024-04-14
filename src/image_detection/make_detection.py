from builder.detection_builder import DectectionBuilder
from components.detection import DetectionComponent
from components.response import ResponseComponent
from constants import PROMPT

def main(image):
    detection = DetectionComponent(image, PROMPT)
    raw_response = ResponseComponent() 
    builder = DectectionBuilder(detection, raw_response)

    builder.process_receipt()
    response = builder.get_response()
    
    return response

if __name__ == "__main__":
    image = open("images/example_01.jpeg", "rb")
    response = main(image)
    print(response)