from db_a import Base, session
from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import relationship


class StoreModel(Base):
    __tablename__ = 'stores'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    
    items = relationship('ItemModel', back_populates='store')
    
    def __init__(self, name):
        self.name = name 
    
    def json(self):
        return { 'name': self.name, 'id': self.id, 'items': list(map(lambda item: item.json(), self.items)) }

    @classmethod
    def find_by_name(cls, name: str):
        return session.query(StoreModel).filter_by(name=name).first()
    
    @classmethod
    def select_all(cls):
        return session.query(StoreModel).all()
        
    def save_to_db(self):
        session.add(self)
        session.commit()
     
    def delete_from_db(self):
        session.delete(self)
        session.commit()
        