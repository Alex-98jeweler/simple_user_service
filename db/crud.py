from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

import db.models as models
import db.schemas as schemas


async def get_user_by_id(db: AsyncSession):
    result = await db.execute(select(models.User).order_by(models.User.id))
    return result.scalar().all()


def create_user(db: Session, user:schemas.User):
    user = models.User(firstname=user.firstname, lastname=user.lastname, email=user.email, age=user.age)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user