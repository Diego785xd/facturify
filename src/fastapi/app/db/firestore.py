import os
from dotenv import load_dotenv

import firebase_admin
from firebase_admin import credentials, storage
from firebase_admin import firestore

# read credentials from environment variable with a value of a path to the json file
load_dotenv()

cred = credentials.Certificate(os.environ.get("FIREBASE_CREDS_PATH"))
firebase_admin.initialize_app(cred, {
        'storageBucket': 'global-hack-week-apis.appspot.com'
})


def get_db():
    return firestore.client()

def upload_file(file_path, dest_path):
    """Sube un archivo a Firebase Storage."""
    try:
        bucket = storage.bucket()
        blob = bucket.blob(dest_path)
        blob.upload_from_filename(file_path)
        return blob.public_url
    except Exception as e:
        print(e)
        raise e
