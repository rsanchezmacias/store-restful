from db_a import Base, session
from sqlalchemy import Column, Integer, String 


class UserModel(Base): 
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(80))
    password = Column(String(80))
    
    
    def __init__(self, username, password):
        self.username = username 
        self.password = password 

    @classmethod
    def find_by_username(cls, username):
        # return cls.query.filter_by(username=username).first()
        return session.query(UserModel).filter_by(username=username).first()
    
    @classmethod 
    def find_by_id(cls, _id):
        # return cls.query.filter_by(id=_id).first()
        return session.query(UserModel).filter_by(id=_id).first()
    
    def save_to_db(self):
        # db.session.add(self)
        # db.session.commit()
        session.add(self)
        session.commit()
