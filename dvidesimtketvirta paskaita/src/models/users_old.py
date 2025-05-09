from database import Base
from sqlalchemy.orm import mapped_column, Mapped

class UserORM(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)


