import os 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# When using the declarative system, classes are defined in terms of a base class.  
# This base class maintains a catalog of classes and tables relative to that base 
Base = declarative_base()

# The engine represents the core interface to the database adapted through a dialect. In this example, SQLite 
# is the dialect 
uri = os.environ.get('DATABASE_URL', 'sqlite:///db/data.db').replace('postgres', 'postgresql')
engine = create_engine(uri)

# Session creates new session objects that can talk to the database. 
Session = sessionmaker(bind=engine)
session = Session()
