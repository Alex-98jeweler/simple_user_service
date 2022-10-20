from typing import List
from webbrowser import get
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import db.crud as crud, db.models as models, db.schemas as schemas
from db.database import engine, AsyncSession, get_session


app = FastAPI()


#Dependency


@app.get("/")
async def root():
    return "Piska siska"

@app.post("/add-user/", response_model=schemas.User)
async def create_user(user: schemas.User, db: AsyncSession=Depends(get_session)):
    return await crud.create_user(db=db, user=user)

@app.get("/users/",)
async def get_user(db: AsyncSession=Depends(get_session)):
    user = await crud.get_user_by_id(db)
    print(user)
    if user is None:
        raise HTTPException(status_code=404, detail="Not found")
    return {'users': user}