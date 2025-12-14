from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
import uvicorn
from .Routes import auth, sweets, inventory

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sweet Shop Management System")

# ✅ ADD THIS (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app
    allow_credentials=True,
    allow_methods=["*"],  # allows OPTIONS, POST, GET, etc.
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(sweets.router)
app.include_router(inventory.router)


# 👇 THIS makes it listen
if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
