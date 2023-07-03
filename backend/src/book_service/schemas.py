from typing import List, Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class User(UserBase):
    id: int
    email: str
    username: str

    class Config:
        orm_mode = True


class ProfileUserBase(BaseModel):
    username: Optional[str] = None


class ProfileUserCreate(ProfileUserBase):
    pass


class ProfileUserUpdate(ProfileUserBase):
    pass


class ProfileUser(ProfileUserBase):
    id: int
    username: str

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    name: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    category: Optional[str] = None
    is_available: Optional[bool] = None


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class Book(BookBase):
    id: int
    owner: Optional[ProfileUser] = None
    tags: Optional[List[Tag]] = []

    class Config:
        orm_mode = True

class TagBase(BaseModel):
    name: Optional[str] = None

class TagCreate(TagBase):
    pass

class TagUpdate(TagBase):
    pass


class Tag(TagBase):
    id: int
    books: Optional[List[Book]] = []

    class Config:
        orm_mode = True


class CartItemBase(BaseModel):
    book_id: Optional[int] = None
    quantity: Optional[int] = None
    price: Optional[int] = None

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(CartItemBase):
    pass

class CartItem(CartItemBase):
    id: int
    book: Optional[Book] = None

    class Config:
        orm_mode = True


class CartBase(BaseModel):
    owner_id: Optional[int] = None
    total_price: Optional[int] = None


class CartCreate(CartBase):
    pass


class CartUpdate(CartBase):
    pass


class Cart(CartBase):
    id: int
    owner: Optional[ProfileUser] = None
    items: Optional[List[CartItem]] = []

    class Config:
        orm_mode = True

