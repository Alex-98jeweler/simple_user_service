from sqlalchemy import (
                        Column,
                        Integer,
                        ForeignKey,
                        String,
                        Boolean,
                    )
from sqlalchemy.orm import relationship

from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True)
    age = Column(String)
    job = Column(String)
    test_field = Column(String)
