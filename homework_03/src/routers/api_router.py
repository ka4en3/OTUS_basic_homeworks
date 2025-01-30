from fastapi import APIRouter
from fastapi import Response
from fastapi import status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/ping", response_class=JSONResponse)
async def ping_pong(response : Response):
    response.status_code = status.HTTP_200_OK
    return {"message": "pong"}
