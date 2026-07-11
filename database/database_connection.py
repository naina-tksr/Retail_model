from sqlalchemy import create_engine
from config.config import HOST, USER, PASSWORD, DATABASE

engine = create_engine(
    f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
)