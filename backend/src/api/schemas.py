from typing import List, Optional
from pydantic import BaseModel


class TagBase(BaseModel):
    name: str


class TagCreate(TagBase):
    pass


class Tag(TagBase):
    id: int
    books: List["Book"] = []

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    name: str
    author: str
    price: int
    category: str


class BookCreate(BookBase):
    description: Optional[str]
    owner_id: int
    tags: Optional[List[int]]


class Book(BookBase):
    id: int
    description: Optional[str]
    is_available: bool
    owner_id: int
    favorited_by: Optional[List["User"]] = []
    tags: List[Tag] = []

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False


class UserRoleBase(BaseModel):
    role_name: str
    permissions: Optional[dict]


class UserRole(UserRoleBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    hashed_password: str
    is_verified: Optional[bool] = False
    books: List[Book] = []
    favorite_books: List[Book] = []
    carts: List["Cart"] = []
    roles: List[UserRole] = []

    class Config:
        orm_mode = True


class CartItemBase(BaseModel):
    book_id: int
    quantity: int
    price: int


class CartItemCreate(CartItemBase):
    pass


class CartItem(CartItemBase):
    id: int
    cart_id: int
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
    owner: User

    class Config:
        orm_mode = True

