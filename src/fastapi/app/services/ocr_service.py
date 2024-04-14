import sys
import logging

sys.path.append("..")

from image_detection.make_detection import main


async def process_ocr(url: str):
    return main(url)
