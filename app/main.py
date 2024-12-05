import os

from dotenv import load_dotenv

load_dotenv()
if os.getenv("DEVELOPMENT") == "DEV":
    import sys
    sys.path.append('../')

import sys
sys.path.append('../')

from fastapi import Depends, FastAPI

from app.db import Message, SessionLocal, get_db, init_db
from app.routers import router
from datetime import datetime

app = FastAPI()
app.include_router(router)

@app.on_event("startup")
async def startup_event():
    # Initialize the database
    init_db()

    # Add an initial record to the database
    db = SessionLocal()
    db.add(Message(user="Admin", message=f"Started at {datetime.now()}"))
    db.commit()
    db.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)