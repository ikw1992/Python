from sqlalchemy import Column,PrimaryKeyConstraint,Integer,String,Date,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Reserver(Base):
    __tablename__ = "reservation"
    id_creneau = Column(Integer, ForeignKey("creneau.id_creneau"), nullable=False)
    id_client = Column(Integer, ForeignKey("client.id_client"), nullable=False)
    allergene = Column(String(50), nullable=False)
    nb_personne=Column(Integer,nullable=False)
    __table_args__ = (PrimaryKeyConstraint("id_creneau","id_client"),)
