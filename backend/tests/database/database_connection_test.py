from sqlalchemy import Engine
from sqlalchemy.orm import Session


def test_create_connection_creates_session_instance(
    get_database_connection_handler,
) -> None:
    database = get_database_connection_handler

    database.create_connection()
    assert isinstance(database.session, Session)
    database.close_connection()


def test_create_connection_creates_engine_instance(
    get_database_connection_handler,
) -> None:
    database = get_database_connection_handler

    database.create_connection()
    assert isinstance(database.engine, Engine)
    database.close_connection()


def test_create_connection_is_called_on_enter(
    mocker, get_database_connection_handler
) -> None:
    spy = mocker.spy(get_database_connection_handler, "create_connection")
    database = get_database_connection_handler

    with database as db:
        pass

    assert spy.call_count == 1


def test_close_connection_clears_session_transaction(
    get_database_connection_handler, get_object_mock
) -> None:
    database = get_database_connection_handler
    mock = get_object_mock

    database.create_connection()
    database.session.add(mock)
    database.close_connection()

    assert database.session.get_transaction() is None


def test_close_connection_does_not_destroy_engine(
    get_database_connection_handler,
) -> None:
    database = get_database_connection_handler

    database.create_connection()
    database.close_connection()

    assert isinstance(database.engine, Engine)


def test_create_connection_is_called_on_exit(
    mocker, get_database_connection_handler
) -> None:
    spy = mocker.spy(get_database_connection_handler, "close_connection")
    database = get_database_connection_handler

    with database as db:
        pass

    assert spy.call_count == 1
