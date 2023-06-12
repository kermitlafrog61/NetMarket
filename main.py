from fastapi import FastAPI

from products.routers import product_router


app = FastAPI()
app.include_router(product_router)
