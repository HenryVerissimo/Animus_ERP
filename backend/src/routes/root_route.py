from fastapi import APIRouter, status
from fastapi.responses import JSONResponse


root_router = APIRouter(tags=["root"])


@root_router.get("/", status_code=status.HTTP_200_OK)
def welcome() -> JSONResponse:
    """Just a welcome route for new API users"""
    body = {
        "message": "Welcome! This is the Animus API. For more details, use the /docs or /redoc endpoints to target documentation."
    }

    response = JSONResponse(content=body, status_code=status.HTTP_200_OK)

    return response
