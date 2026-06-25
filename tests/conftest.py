import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

os.environ.setdefault("DATABASE_URL", "sqlite://")

from src.database.config import get_db
from src.database.models import Base
from src.reservas.api import app


@pytest.fixture
def db_session():
    engine_test = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool
    )

    connection = engine_test.connect()
    transaction = connection.begin()

    Base.metadata.create_all(bind=connection)

    TestingSessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=connection,
        join_transaction_mode="create_savepoint"
    )

    session = TestingSessionLocal()

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()
        engine_test.dispose()


@pytest.fixture
def client_con_bd(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()
