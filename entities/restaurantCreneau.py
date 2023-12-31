from sqlalchemy import Column,PrimaryKeyConstraint,Integer,String,Date,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class RestaurantCreneau(Base):
    __tablename__ = "restaurant_creneau"
    id_creneau = Column(Integer,ForeignKey("creneau.id_creneau"),nullable=False)
    id_restaurant = Column(Integer,ForeignKey("restaurant.id_restaurant"),nullable=False)
    __table_args__ = (PrimaryKeyConstraint('id_creneau', "id_restaurant"),)