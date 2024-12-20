from fastapi import Request, APIRouter, HTTPException
from fastapi.responses import JSONResponse

fake_db = [{"id": 1, "name": "product1", "price": 100}, {"id": 2, "name": "product2", "price": 200}]

router = APIRouter()


@router.get("/", response_class=JSONResponse)
async def get_products(request: Request):
    return fake_db


@router.get("/{product_id}", response_class=JSONResponse)
async def get_product(product_id: int):
    for product in fake_db:
        if product["id"] == product_id:
            return product
    return HTTPException(status_code=404, detail="Product not found!")


@router.post("/", response_class=JSONResponse)
async def add_product(product_to_add: dict):
    next_id = max(product["id"] for product in fake_db) + 1
    product_to_add["id"] = next_id
    fake_db.append(product_to_add)
    return product_to_add
