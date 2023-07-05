from typing import List, Optional
from pydantic import BaseModel


class TagBase(BaseModel):
    name: str


class TagCreate(TagBase):
    pass


class Tag(TagBase):
    id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    name: str
    author: str
    description: Optional[str]
    price: int
    category: str
    is_available: bool


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    owner_id: int
    tags: List[Tag] = []

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    books: List[Book] = []

    class Config:
        orm_mode = True


class CartItemBase(BaseModel):
    cart_id: int
    book_id: int
    quantity: int


class CartItemCreate(CartItemBase):
    pass


class CartItem(CartItemBase):
    id: int
    book: Book

    class Config:
        orm_mode = True


class CartBase(BaseModel):
    owner_id: int


class CartCreate(CartBase):
    pass


class Cart(CartBase):
    id: int
    total_price: int
    items: List[CartItem] = []

    class Config:
        orm_mode = True


class ProfileUserBase(BaseModel):
    username: str


class ProfileUserCreate(ProfileUserBase):
    pass


class ProfileUser(ProfileUserBase):
    id: int
    user_id: int
    user: User
    books: List[Book] = []
    favorite_books: List[Book] = []
    carts: List[Cart] = []

    class Config:
        orm_mode = True
