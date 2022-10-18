from sqlalchemy.orm import Session

import db.models as models
import db.schemas as schemas


def get_user_by_id(db: Session, id: int):
    return db.query(models.User).get(id)


def create_user(db: Session, user:schemas.User):
    user = models.User(firstname=user.firstname, lastname=user.lastname, email=user.email, age=user.age)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user