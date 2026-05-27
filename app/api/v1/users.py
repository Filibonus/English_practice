from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def count_routers():
    return {"count": 10}