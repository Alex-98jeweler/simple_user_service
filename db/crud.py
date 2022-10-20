from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import sqlalchemy.engine.row as r

import db.models as models
import db.schemas as schemas


async def get_user_by_id(db: AsyncSession):
    result = await db.execute(select(models.User).order_by(models.User.id))
    data = result.fetchall()
    results = []
    for i in data:
        user = schemas.User.parse_obj(i["User"].__dict__)
        results.append(user)
        print(i["User"].__dict__)
    return results


async def create_user(db: AsyncSession, user:schemas.User):
    user_db = models.User()
    user_db.firstname = user.firstname
    user_db.lastname = user.lastname
    user_db.email = user.email
    user_db.age = user.age
    db.add(user_db)
    await db.commit()
    await db.refresh(user_db)
    return user.__dict__