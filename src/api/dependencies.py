from typing import Generator
from src.db.session import Sessionlocal

def get_db() -> Generator:
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()    