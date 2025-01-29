from fastapi import Request, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from schemas.product import ProductCreate, ProductRead

fake_db = [{"id": 1, "name": "product1", "price": 100}, {"id": 2, "name": "product2", "price": 200}]

router = APIRouter()


@router.get("/", response_model=list[ProductRead], response_class=JSONResponse)
async def get_products(request: Request):
    return fake_db


@router.get("/{product_id}", response_model=ProductRead, response_class=JSONResponse)
async def get_product(product_id: int):
    for product in fake_db:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found!")


@router.post("/", response_model=ProductRead, response_class=JSONResponse)
async def add_product(product_to_add: ProductCreate):
    next_id = max(product["id"] for product in fake_db) + 1
    new_product = {"id": next_id, **product_to_add.dict()}
    fake_db.append(new_product)
    return new_product
