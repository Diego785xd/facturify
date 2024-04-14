import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("firebasecreds.json")
firebase_admin.initialize_app(cred)


def get_db():
    return firestore.client()
