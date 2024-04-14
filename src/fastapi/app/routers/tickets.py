from fastapi import FastAPI, File, UploadFile, HTTPException, APIRouter
from fastapi.responses import FileResponse
from app.services.ticket_service import upload_file, create_ticket_data

router = APIRouter()

@app.post('/tickets') 
async def upload_ticket(image: UploadFile = File(...)):
    if 'name' not in image.headers.get('content-disposition', ''):
            raise HTTPException(status_code=400, detail='Invalid file type. Only images are allowed.') 
        
    path = f'images/{image.filename}'
    try:
        file_path = f"../../telegram/temp_image.jpg"
        url = upload_file(file_path, "images" + file_path.split("/")[-1])
        try:
            create_ticket(rfc, ticket, url) 
            return {'url': url}
        except Exception as e:
            print(e)    
            raise HTTPException(status_code=500, detail=f'An error occurred while saving the ticket data {e}')
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f'An error occurred while saving the image {e}')
    
    return {'filename': image.filename}