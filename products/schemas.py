from typing import Optional

from pydantic import BaseModel, validator


class TunedModel(BaseModel):
    class Config:
        orm_mode = True


class ProductList(TunedModel):
    id: int
    title: str


class ProductCreate(TunedModel):
    title: str
    description: Optional[str]
    price: float


class ProductDetail(TunedModel):
    id: int
    title: str
    description: str
    price: float


class ProductUpdate(TunedModel):
    title: Optional[str]
    description: Optional[str]
    price: Optional[float]
