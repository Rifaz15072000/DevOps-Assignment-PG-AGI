# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# app = FastAPI()

# # Configure CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/api/health")
# async def health_check():
#     return {"status": "healthy", "message": "Backend is running successfully"}

# @app.get("/api/message")
# async def get_message():
#     return {"message": "You've successfully integrated the backend!"}


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}
    
# ✅ REQUIRED HEALTH CHECK (PRIMARY)
@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": "fastapi-backend"
    }

# ✅ OPTIONAL (kept for compatibility with your existing API)
@app.get("/api/health")
async def api_health_check():
    return {
        "status": "ok",
        "service": "fastapi-backend"
    }

@app.get("/api/message")
async def get_message():
    return {
        "message": "You've successfully integrated the backend!"
    }
