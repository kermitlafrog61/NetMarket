from fastapi import HTTPException

from core.db import SessionLocal
from products.dal import ProductDAL
from products.schemas import ProductCreate, ProductDetail, ProductList, ProductUpdate


async def _create_product(body: ProductCreate) -> ProductDetail:
    async with SessionLocal() as session:
        async with session.begin():
            product_dal = ProductDAL(session)
            product = await product_dal.create(body)

        return ProductDetail.from_orm(product)


async def _retrieve_product(id: int) -> ProductDetail:
    async with SessionLocal() as session:
        async with session.begin():
            product_dal = ProductDAL(session)
            product = await product_dal.retrieve(id)
        return ProductDetail.from_orm(product)


async def _list_products() -> ProductList:
    async with SessionLocal() as session:
        async with session.begin():
            product_dal = ProductDAL(session)
            products = await product_dal.list()
        return [ProductList.from_orm(product) for product in products]


async def _update_product(id: int, body: ProductUpdate) -> ProductDetail:
    async with SessionLocal() as session:
        async with session.begin():
            product_dal = ProductDAL(session)
            product = await product_dal.update(id, body)
        return ProductDetail.from_orm(product)


async def _delete_product(id: int) -> None:
    async with SessionLocal() as session:
        async with session.begin():
            product_dal = ProductDAL(session)
            await product_dal.destroy(id)
