from fastapi import FastAPI

from src.routes.root_route import root_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(router=root_router)

    return app


app = create_app()
