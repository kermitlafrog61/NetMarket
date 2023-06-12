from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .models import Product
from .schemas import ProductCreate, ProductUpdate


class ProductDAL:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, body: ProductCreate) -> Product:
        product = Product(**body.dict())
        self.session.add(product)
        await self.session.flush()
        return product

    async def list(self) -> list[Product]:
        statement = select(Product)
        result = await self.session.execute(statement)
        products = result.scalars().all()
        return products

    async def retrieve(self, id: int):
        statement = select(Product).where(Product.id == id)
        result = await self.session.execute(statement)
        product = result.scalar()
        if not product:
            raise HTTPException(
                status_code=404, detail="Product not found")

        return product

    async def update(self, id: int, body: ProductUpdate) -> Product:
        statement = select(Product).where(Product.id == id)
        result = await self.session.execute(statement)
        product = result.scalar()

        if not product:
            raise HTTPException(
                status_code=404, detail="Product not found")

        if not body.dict(exclude_none=True):
            raise HTTPException(
                status_code=400,
                detail="Empty body. At least one field should be provided.",
            )

        for k, v in body.dict(exclude_unset=True).items():
            setattr(product, k, v)

        await self.session.flush()
        return product

    async def destroy(self, id: int) -> None:
        statement = select(Product).where(Product.id == id)
        result = await self.session.execute(statement)
        product = result.scalar()
        print(product)

        if not product:
            raise HTTPException(
                status_code=404, detail="Product not found")

        await self.session.delete(product)
