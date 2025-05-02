from database import Base
from sqlalchemy.orm import mapped_column, Mapped

class SchoolOrm(Base):
    __tablename__ = 'schools'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    phone: Mapped[str]
    address: Mapped[str]
    
