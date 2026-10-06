from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from database import SessionLocal

async def get_session():
    async with SessionLocal() as session:
        yield session

app = FastAPI()

@app.get("/")
async def root(session: AsyncSession = Depends(get_session)):
    return {"message": "Hello!"}


