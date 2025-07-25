#El nombre de la tabla va ser la relacionada pero en minuscula

from sqlalchemy.ext.declarative import declarative_base, as_declarative, declared_attr

"""@as_declarative()
class Base:
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()"""
    
Base = declarative_base() 
        