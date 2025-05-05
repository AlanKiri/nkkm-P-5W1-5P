from database import Base
from sqlalchemy.orm import Mapped, mapped_column

class ServersOrm(Base):
    __tablename__ = 'servers'
    id: Mapped[int] = mapped_column(primary_key=True)
    region: Mapped[str]
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    private: Mapped[bool] = mapped_column(nullable=False)