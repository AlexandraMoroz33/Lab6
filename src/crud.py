from sqlalchemy.orm import Session
from models import Role, Permission, User, Post
from schemas import RoleCreate, PermissionCreate, UserCreate, PostCreate


def create_role(db: Session, data: RoleCreate):
    role = Role(name=data.name)
    db.add(role)
    db.commit()
    db.refresh(role)
    return role

def read_roles(db: Session):
    return db.query(Role).all()

def read_role(db: Session, role_id: int):
    return db.query(Role).filter(Role.id == role_id).first()

def update_role(db: Session, role_id: int, data: RoleCreate):
    role = db.query(Role).filter(Role.id == role_id).first()
    if role:
        role.name = data.name
        db.commit()
        db.refresh(role)
    return role

def delete_role(db: Session, role_id: int):
    role = db.query(Role).filter(Role.id == role_id).first()
    if role:
        db.delete(role)
        db.commit()
    return role


def create_permission(db: Session, data: PermissionCreate):
    perm = Permission(name=data.name)
    db.add(perm)
    db.commit()
    db.refresh(perm)
    return perm

def read_permissions(db: Session):
    return db.query(Permission).all()

def read_permission(db: Session, permission_id: int):
    return db.query(Permission).filter(Permission.id == permission_id).first()

def update_permission(db: Session, permission_id: int, data: PermissionCreate):
    perm = db.query(Permission).filter(Permission.id == permission_id).first()
    if perm:
        perm.name = data.name
        db.commit()
        db.refresh(perm)
    return perm

def delete_permission(db: Session, permission_id: int):
    perm = db.query(Permission).filter(Permission.id == permission_id).first()
    if perm:
        db.delete(perm)
        db.commit()
    return perm


def create_user(db: Session, data: UserCreate):
    user = User(**data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def read_users(db: Session):
    return db.query(User).all()

def read_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user_id: int, data: UserCreate):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.username = data.username
        user.password = data.password
        user.role_id = data.role_id
        db.commit()
        db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user


def create_post(db: Session, data: PostCreate):
    post = Post(**data.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def read_posts(db: Session):
    return db.query(Post).all()

def read_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def update_post(db: Session, post_id: int, data: PostCreate):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        post.title = data.title
        post.content = data.content
        post.user_id = data.user_id
        db.commit()
        db.refresh(post)
    return post

def delete_post(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
    return post
