from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///students.db")
Session = sessionmaker(bind=engine)
session = Session()