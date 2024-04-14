import firebase_admin
from firebase_admin import credentials, storage

def initialize_app():
    """Inicializa la aplicación Firebase con un archivo de credenciales."""
    cred = credentials.Certificate("authkey.json")
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'global-hack-week-apis.appspot.com'
    })

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
