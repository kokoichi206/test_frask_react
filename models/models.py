from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
# from database import Base
from datetime import datetime


class Ranks(Base):
    __tablename__ = 'total'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True)
    amount = Column(Integer)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, name=None, amount=None, date=None):
        self.name = name
        self.amount = amount
        self.date = date

    def __repr__(self):
        return f'User(id={self.id}, name={self.amount}, amount={self.amount}, date={self.date})'
