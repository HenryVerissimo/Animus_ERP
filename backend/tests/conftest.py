import pytest

from fastapi import FastAPI

from app import create_app


@pytest.fixture
def get_app() -> FastAPI:
    app = create_app()

    return app
