from database import Base
from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text


class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


class Products(Base):
    __tablename__='products'
    id=Column(Integer,primary_key=True,nullable=False)
    price=Column(Integer,nullable=False)
    name=Column(String,nullable=False)
    is_sale=Column(Boolean,server_default='False')
    inventory=Column(Integer,nullable=False,server_default="0")
    
