# from app.db import firestore
from app.models.items import Items

data = {"name": "Los Angeles", "state": "CA", "country": "USA"}


async def process_ocr():
    try:
        # db = firestore.get_db()
        # db.collection("cities").document("LA").set(data)
        return {"Status": "200"}
    except Exception as e:
        return {"Error": str(e)}
