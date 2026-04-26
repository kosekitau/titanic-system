from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True, autoincrement=True)
    pclass = Column(Integer)
    sex = Column(String(255))
    age = Column(Integer)
    slibSp = Column(Integer)
    parch = Column(Integer)
    ticket = Column(String(255))
    fare = Column(Float)
    cabin = Column(String(255))
    embarked = Column(String(255))

    def __repr__(self):
        return "<Person(id='%s', pclass='%s', sex='%s', age='%s')>" % (self.id, self.pclass, self.sex, self.age)
