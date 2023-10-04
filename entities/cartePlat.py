from sqlalchemy import Column,Integer,String,Date,Boolean,ForeignKey,PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from config.database import Base

class CartePlat(Base):
    __tablename__ = 'carte_plat'
    id_plat=Column(Integer,ForeignKey('plat.id_plat'),nullable=False)
    id_carte=Column(Integer,ForeignKey("carte.id_carte"),nullable=False)
    __table_args__ = (PrimaryKeyConstraint("id_plat","id_carte"),)

