import pytest
from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app


client = TestClient(app)

def test_register_user():
    response = client.post("/register?username=testuser&password=123456")
    assert response.status_code == 200
    assert "Usuário criado com sucesso" in response.json()["msg"]

def test_login_user():
    # Primeiro registra
    client.post("/register?username=loginuser&password=123456")
    # Depois faz login
    response = client.post("/login?username=loginuser&password=123456")
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_create_product():
    response = client.post("/products?name=Notebook&description=Ultrabook&price=3500&stock=10")
    assert response.status_code == 200
    assert response.json()["msg"] == "Produto criado com sucesso"

def test_list_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
