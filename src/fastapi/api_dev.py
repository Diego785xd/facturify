from fastapi import FastAPI
import uvicorn

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from pydantic import BaseModel

cred = credentials.Certificate("firebasecreds.json")
firebase_admin.initialize_app(cred)

app = FastAPI()

db = firestore.client()

class Items(BaseModel):
    rfc: str
    nombre_razon_social: str
    codigo_postal_domicilio_fiscal: int
    regimen_fiscal: str
    correo_electronico: str



data = {"name": "Los Angeles", "state": "CA", "country": "USA"}

@app.get('/', status_code=200)
async def root():
    """
    End Point for API health check


    Returns: Health:Ok

    """
    return {"Health": "Ok"}



@app.get('/ocr', status_code=200)
async def root():

    return {"message": "Hello World get"}


@app.post('/ocr', status_code=200)
async def root():
    try:
        db.collection("cities").document("LA").set(data)
        return {"Status": "200"}
    except Exception as e:
        return {"Error": str(e)}



@app.post('/users/')
async def create_item(item: Items):
    """

    Endpoint for user creation
    Args:
        item: Json object with user details

    {
    "rfc": "ABCD123456XYZ",
    "nombre_razon_social": "Empresa Ejemplo S.A. de C.V.",
    "codigo_postal_domicilio_fiscal": "12345",
    "uso_fiscal_factura": "G01",
    "regimen_fiscal": "General de Ley",
    "correo_electronico": "example@example.com"
    }


    Returns:

    """
    try:
        item_dict = item.dict()
        data_save = {"nombre_razon_social": item_dict["nombre_razon_social"],
                "codigo_postal_domicilio_fiscal": item_dict["codigo_postal_domicilio_fiscal"],
                "regimen_fiscal": item_dict["regimen_fiscal"],
                "correo_electronico": item_dict["correo_electronico"]}

        db.collection("users").document(item_dict["rfc"]).set(data_save)
        return {"Status": "201"}
    except KeyError as ke:
        return {"Error": "Bad Key",
                "message": str(ke)}
    except Exception as e:
        return {"Error": str(e)}

@app.get("/users/")
async def search_in_firestore(query: str):
    """
    Endpoint to search in firestore using query


    Args:
        query: GET http://localhost:5000/users/?query=ABCD123456XYZ

    Returns:
        JSON header with data of the required sections

    """
    try:
        user_ref = db.collection("users").document(query)
        user_doc = user_ref.get()
        if user_doc.exists:
            return user_doc.to_dict()
        else:
            return {"Error": "404"}
    except Exception as e:
        return {"Error": "500", "Message": str(e)}

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=5000)
