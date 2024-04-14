from fastapi import FastAPI
import uvicorn

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

app = FastAPI()


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
    return {"message": "Hello World post"}


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=5000)
