import io
import imageio
from imageio import v3 as iio
import os
import cv2
import base64
import numpy as np
from fastapi import FastAPI
from fastapi.responses import StreamingResponse, Response

SATELLITE_PATH = os.environ['SATELLITE_PATH']
print(SATELLITE_PATH)

app = FastAPI()

@app.get("/organization/{organization_id}/entities")
async def root(skip: int = 0, limit: int = 10):
    return {"message": "Get"}

@app.post("/organization/{organization_id}/entity")
async def root():
    return {"message": "Post"}

@app.get("/organization/{organization_id}/entity/{entity_id}")
async def root(entity_id: str):
    return {"message": f"Get {entity_id}"}

@app.put("/organization/{organization_id}/entity/{entity_id}")
async def root(entity_id: str):
    return {"message": f"Put {entity_id}"}

@app.delete("/organization/{organization_id}/entity/{entity_id}")
async def root(entity_id: str):
    return {"message": f"Delete {entity_id}"}

@app.get("/tiles/satellite/{z}/{x}/{y}.png", response_class=Response)
async def root(z, x, y):
    img = cv2.imread(f'{SATELLITE_PATH}/{z}/{y}/{x}.png')
    if img is None:
        img = np.zeros((256,256,3), np.uint8)
        img.fill(255) 

    with io.BytesIO() as buf:
        iio.imwrite(buf, img, plugin="pillow", format="JPEG")
        im_bytes = buf.getvalue()
        
    headers = {'Content-Disposition': 'inline; filename="test.jpeg"'}
    return Response(im_bytes, headers=headers, media_type='image/jpeg')