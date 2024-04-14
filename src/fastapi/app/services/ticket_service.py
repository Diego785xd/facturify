# app/services/ticket_service.py

from firebase_admin import storage
from app.db import firestore
from app.services.user_service import search_user
import random
import string

def set_id_ticket():
    """Genera un id para un ticket."""
    id_length = 10
    characters = string.ascii_letters + string.digits
    random_id = ''.join(random.choice(characters) for _ in range(id_length))
    return random_id

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

async def create_ticket_data(rfc:str, ticket:dict, url: str):
    """Crea un ticket en Firestore."""
    """
        params: 
            rfc : str - RFC del usuario
            ticket: dict - Datos del ticket extraidos por el OCR
            url: str - URL de la imagen del ticket en Firebase Storage
    """
    try:
        user = search_user(rfc)
        db = firestore.get_db()
        data_save = {
            'nombre_negocio': ticket['nombre_negocio'],
            'rfc': rfc,
            'nombre_razon_social': user.get('nombre_razon_social', ''),
            'codigo_postal_domicilio_fiscal': user.get('codigo_postal_domicilio_fiscal', '')
            'regimen_fiscal': user.get('regimen_fiscal', ''),
            'no_operacion': ticket['no_operacion'],
            'fecha': ticket['fecha'],
            'asiento': ticket['asiento'],
            'forma_de_pago': ticket['forma_de_pago'],
            'tipo de venta': ticket['tipo de venta'],
            'precio': ticket['precio'],
            'descuento': ticket['descuento'],
            'subtotal': ticket['subtotal'],
            'iva': ticket['iva'],
            'total': ticket['total'],
            'url': url
        }
        db.collection("users").document(rfc).collection("tickets").document(set_id_ticket()).set(data_save)
        return {"Status": "201"}
    except KeyError as ke:
        return {"Error": "Bad Key", "message": str(ke)}
    except Exception as e:
        return {"Error": str(e)}