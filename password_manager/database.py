from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
from databases import Database
import os

load_dotenv()

USER = os.getenv("PROD_USER")
PASSWORD = os.getenv("PROD_PASS")

DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@localhost/password_manager"
database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(DATABASE_URL)


