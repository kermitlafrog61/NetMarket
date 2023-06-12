from typing import List

from fastapi import APIRouter

from .queries import (_create_product, _delete_product, _list_products,
                      _retrieve_product, _update_product)
from .schemas import ProductCreate, ProductDetail, ProductList, ProductUpdate

product_router = APIRouter()


@product_router.post("/products", status_code=201)
async def create_product(product: ProductCreate) -> ProductDetail:
    return await _create_product(product)


@product_router.get("/products/{id}")
async def retrieve_product(id: int):
    return await _retrieve_product(id)


@product_router.get("/products")
async def list_products() -> List[ProductList]:
    return await _list_products()


@product_router.patch("/products/{id}", response_model=ProductDetail)
async def update_product(id: int, product: ProductUpdate) -> ProductDetail:
    return await _update_product(id, product)


@product_router.delete("/products/{id}", status_code=204)
async def delete_product(id: int):
    return await _delete_product(id)
