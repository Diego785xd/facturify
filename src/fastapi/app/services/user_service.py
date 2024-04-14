# app/services/user_service.py
from app.db import firestore
from app.models.items import Items


async def create_user(item: Items):
    try:
        db = firestore.get_db()
        item_dict = item.dict()
        data_save = {
            "nombre_razon_social": item_dict["nombre_razon_social"],
            "codigo_postal_domicilio_fiscal": item_dict[
                "codigo_postal_domicilio_fiscal"
            ],
            "regimen_fiscal": item_dict["regimen_fiscal"],
            "correo_electronico": item_dict["correo_electronico"],
        }
        db.collection("users").document(item_dict["rfc"]).set(data_save)
        return {"Status": "201"}
    except KeyError as ke:
        return {"Error": "Bad Key", "message": str(ke)}
    except Exception as e:
        return {"Error": str(e)}


async def search_user(query: str):
    try:
        db = firestore.get_db()
        user_ref = db.collection("users").document(query)
        user_doc = user_ref.get()
        if user_doc.exists:
            return user_doc.to_dict()
        else:
            return {"Error": "404"}
    except Exception as e:
        return {"Error": "500", "Message": str(e)}
