from typing import Self
from types import TracebackType
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session

from src.config.database_settings import DatabaseSettings


class DatabaseConnectionHandler:
    """Connect in some database service

    Attributes:
        session: Manage database CRUD operations.
        engine: Provides a source of connectivity to the database.
        connection_string: The string used for connect engine with the database service.
    """

    def __init__(
        self,
        dialect: str,
        driver: str,
        username: str,
        password: str,
        host: str,
        port: int,
        database_name: str,
    ) -> None:
        """Constructor method this class

        Args:
            dialect: The name of the SGBD, as "postgresql" for exemple.
            driver: The name of the driver (adapter) used to connect the application to the database service.
            username: Your username used as a credential in the databse service.
            password: Your password used as a credential in the databse service.
            host: IP or domain of machine running the database service.
            port: Port number what the databse service is listening on.
            database_name: Name of the database used.
        """
        self.session: Session | None = None
        self.engine: Engine | None = None
        self._connection_string: str = (
            f"{dialect}+{driver}://{username}:{password}@{host}:{port}/{database_name}"
        )

    def create_connection(self) -> None:
        """Create connection with the database service"""

        self._engine = create_engine(url=self._connection_string)
        Session = sessionmaker(self._engine)
        self.session = Session()

    def close_connection(self) -> None:
        """Close connection with the database service"""

        if self.session is not None:
            self.session.close()

        self.engine = None

    def __enter__(self) -> Self:
        self.create_connection()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.close_connection()

    def __str__(self) -> str:
        return f"ConnectPostgreSQL: {self._connection_string}"


config = DatabaseSettings()  # type: ignore

# The singleton instance of the main database
database = DatabaseConnectionHandler(
    config.db_dialect,
    config.db_driver,
    config.db_username,
    config.db_password,
    config.db_host,
    config.db_port,
    config.db_name,
)
