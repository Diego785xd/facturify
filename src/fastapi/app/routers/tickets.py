from fastapi import FastAPI, File, UploadFile, HTTPException, APIRouter
from fastapi.responses import FileResponse
from db.firestore import upload_file
import shutil

router = APIRouter()

@app.post('/tickets') 
async def upload_ticket(image: UploadFile = File(...)):
    if 'name' not in image.headers.get('content-disposition', ''):
        raise HTTPException(status_code=400, detail='Invalid file type. Only images are allowed.') 
    
    # Save the image to the server
    path = f'images/{image.filename}'
    print(image.filename)
    try:
        # TODO
        file_path = f"../../telegram/temp_image.jpg"
        url = upload_file(file_path, "images" + file_path.split("/")[-1])
        return {'url': url}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f'An error occurred while saving the image {e}')
    
    return {'filename': image.filename}