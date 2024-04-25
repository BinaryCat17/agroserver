import os
from fastapi import FastAPI
from fastapi.responses import FileResponse

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

@app.get("/tiles/satellite/{z}/{x}/{y}.png")
async def root(z, x, y):
    return FileResponse(f'{SATELLITE_PATH}/{z}/{x}/{y}.png')
