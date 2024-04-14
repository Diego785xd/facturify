import os
from dotenv import load_dotenv

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# read credentials from environment variable with a value of a path to the json file
load_dotenv()

cred = credentials.Certificate(os.environ.get("FIREBASE_CREDS_PATH"))
firebase_admin.initialize_app(cred)


def get_db():
    return firestore.client()
