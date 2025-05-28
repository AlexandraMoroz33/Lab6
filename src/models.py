from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    TIMESTAMP,
    UniqueConstraint,
    func
)
from sqlalchemy.orm import relationship
from database import Base


class Role(Base):
    __tablename__ = "roles"

    id         = Column(Integer, primary_key=True, index=True)
    name       = Column(String(255), unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    users       = relationship("User", back_populates="role")
    permissions = relationship("RolePermission", back_populates="role")


class Permission(Base):
    __tablename__ = "permissions"

    id         = Column(Integer, primary_key=True, index=True)
    name       = Column(String(255), unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    roles = relationship("RolePermission", back_populates="permission")


class RolePermission(Base):
    __tablename__ = "role_permissions"
    __table_args__ = (UniqueConstraint('role_id', 'permission_id'),)

    id            = Column(Integer, primary_key=True, index=True)
    role_id       = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"), index=True)
    permission_id = Column(Integer, ForeignKey("permissions.id", ondelete="CASCADE"), index=True)

    role       = relationship("Role", back_populates="permissions")
    permission = relationship("Permission", back_populates="roles")


class User(Base):
    __tablename__ = "users"

    id         = Column(Integer, primary_key=True, index=True)
    username   = Column(String(255), unique=True, nullable=False)
    password   = Column(String(255), nullable=False)
    role_id    = Column(Integer, ForeignKey("roles.id"), index=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    role  = relationship("Role", back_populates="users")
    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = "posts"

    id         = Column(Integer, primary_key=True, index=True)
    title      = Column(String(255), nullable=False)
    content    = Column(Text, nullable=False)
    user_id    = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), index=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    user = relationship("User", back_populates="posts")
