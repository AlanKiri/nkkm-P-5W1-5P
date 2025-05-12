from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from database import Base

class BusinessManORM(Base):
    __tablename__ = 'business_mans'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
    
    owned_cars:Mapped[list['CarsORM']] = relationship(back_populates='owner')
    owned_stores: Mapped[list['StoresORM']] = relationship(back_populates='owner')
    
class StoresORM(Base):
    __tablename__ = 'stores'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    address:Mapped[str]
    price: Mapped[int]
    
    owner_id: Mapped[int] = mapped_column(ForeignKey('business_mans.id'))
    owner: Mapped['BusinessManORM'] = relationship(back_populates='owned_stores')
    
class CarsORM(Base):
    __tablename__ = 'cars'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    model:Mapped[str]
    brand:Mapped[str]
    
    owner_id: Mapped[int] = mapped_column(ForeignKey("business_mans.id"))
    owner: Mapped['BusinessManORM'] = relationship(back_populates='owned_cars')

    