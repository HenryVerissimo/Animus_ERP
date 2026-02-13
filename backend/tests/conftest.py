import pytest

from fastapi import FastAPI
from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base

from app import create_app
from src.database.database_connection import DatabaseConnectionHandler


@pytest.fixture
def get_app() -> FastAPI:
    app = create_app()

    return app


@pytest.fixture
def get_database_connection_handler() -> DatabaseConnectionHandler:
    database = DatabaseConnectionHandler(
        dialect="postgresql",
        driver="psycopg2",
        username="UserTest",
        password="Test123",
        host="0.0.0.0",
        port=5432,
        database_name="TestDatabase",
    )

    return database


@pytest.fixture
def get_object_mock():
    Base = declarative_base()

    class MockObject(Base):
        __tablename__ = "mock_table"

        id = Column(Integer, primary_key=True)

    return MockObject()
