from configuracion import engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Paises(Base):
    __tablename__ = 'pais'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(200))
    capital = Column(String(200))
    continente = Column(String(200))
    dial = Column(String(200))
    geoname_id = Column(Integer)
    itu = Column(String(200))
    lenguajes = Column(String(200))
    es_independiente = Column(String(200))


Base.metadata.create_all(engine)