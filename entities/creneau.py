from config.database import Base
from sqlalchemy import Column,Integer,String,Date

#new
class Creneau (Base):
    __tablename__="creneau"
    id_creneau=Column(Integer,primary_key=True,autoincrement=True)
    heure = Column(Integer,nullable=False)
    capacite_max = Column(Integer,nullable=False)
    date= Column(Date,nullable=False)