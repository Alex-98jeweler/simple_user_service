from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import db.crud as crud, db.models as models, db.schemas as schemas
from db.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


#Dependency
def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()


@app.get("/")
async def root():
    return "Piska siska"

@app.post("/add-user/", response_model=schemas.User)
async def create_user(user: schemas.User, db: Session=Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=schemas.User)
async def get_user(user_id, db: Session=Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Not found")
    return user