import sys
import logging
import os
from dotenv import load_dotenv
from azure.storage.blob import BlockBlobService

sys.path.append("..")

from image_detection.make_detection import main

load_dotenv()

BLOB_STORAGE_KEY  = os.environ.get("BLOB_STORAGE_KEY")

async def process_ocr(image_name: str):

    account_name = 'storageangelhack'
    account_key = BLOB_STORAGE_KEY
    block_blob_service = BlockBlobService(account_name, account_key)

    container_name = 'images'
    blob_name = image_name
    blob = block_blob_service.get_blob_to_bytes(container_name, blob_name).content

    return main(blob)
