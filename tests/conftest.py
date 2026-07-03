import pytest
from fastapi.testclient import TestClient
import sys
import os

# Adiciona a raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app
from database import Base, engine

@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown_db():
    # Limpa o banco antes de cada teste
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    # Opcional: limpa novamente após o teste
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client():
    return TestClient(app)
