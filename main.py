from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import storage

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. Replace "*" with specific domains for production.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Pydantic model to validate request data
class Name(BaseModel):
    name: str

@app.post("/submit")
async def submit_name(name: Name):
    try:
        storage.save_name(name.name)
        return {"message": "Name saved successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
