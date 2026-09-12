from database import Base, engine
from db_models import User, Transaction, Budget


Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")