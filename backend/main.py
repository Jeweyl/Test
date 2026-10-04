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


@app.post("/section")
async def postSection(session:AsyncSession = Depends(get_session)):
    await session.execute(
        text("""
            CREATE TABLE section(
                id NUMERIC(10) PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            )
        """)
    )
    await session.execute(
        text("""
            INSERT INTO section (id, name)
            VALUES (1, 'TEST')
        """)    
    )
    await session.commit()
    return {"message": "section created sucsess"}


@app.get("/get_section")
async def get_section(session:AsyncSession=Depends(get_session)):
    result = await session.execute(
        text(
        """
        SELECT * FROM section
        WHERE id = 1
        """
        )
    )
    row = result.first()
    return {"id": row.id, "name":row.name}

@app.delete("/section/{id}")
async def section_del(id:int, session:AsyncSession = Depends(get_session)):
    result = await session.execute(text("""
        DELETE FROM section
        WHERE id = :id
        """),
        {"id": id})
    await session.commit()
    row_count = result.rowcount 
    if row_count < 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Не удалось найти ни одной строки с таким id'
        )
    return {"message":f"section by {id} deleted"}
