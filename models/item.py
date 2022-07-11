from typing import List
from db_a import Base, session
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class ItemModel(Base): 
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    price = Column(Float(precision=2))

    store_id = Column(Integer, ForeignKey('stores.id'))
    store = relationship('StoreModel', back_populates='items')
    
    def __init__(self, name: str, price: float, store_id: int):
        self.name = name 
        self.price = price 
        self.store_id = store_id
        
    def json(self):
        return { 'name': self.name, 'store_id': self.store_id, 'price': self.price }

    @classmethod
    def find_by_name(cls, name: str) -> List:
        return session.query(ItemModel).filter_by(name=name).first()
    
    @classmethod
    def select_all(cls):
        return session.query(ItemModel).all()
        
    def save_to_db(self):
        session.add(self)
        session.commit()
       
    def delete_from_db(self):
        session.delete(self)
        session.commit()
