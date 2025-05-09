from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from database import Base

class RoleORM(Base):
    __tablename__ = 'roles'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    default:Mapped[bool]
    name:Mapped[str]
    slug:Mapped[str]
    
    users: Mapped[list["UserORM"]] = relationship(back_populates='role')
    
    
class UserORM(Base):
    __tablename__ = 'users'
    
    id:Mapped[int] = mapped_column(primary_key=True)
    first_name:Mapped[str]
    last_name:Mapped[str]
    birthdate_unix: Mapped[int]
    
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))
    role: Mapped["RoleORM"] = relationship(back_populates='users')
    
    profile: Mapped["ProfileORM"] = relationship(back_populates="user", uselist=False)
    
    
class ProfileORM(Base):
    __tablename__ = 'profiles'
    
    id:Mapped[int] = mapped_column(primary_key=True)
    nicename: Mapped[str]
    bio: Mapped[str]
    avatar: Mapped[str]
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["UserORM"] = relationship(back_populates='profile')
    
    