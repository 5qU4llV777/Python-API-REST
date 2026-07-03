import pytest
from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

client = TestClient(app)

def test_delete_product():
    # Cria produto inicial
    client.post("/products?name=Teclado&description=Mecânico&price=400&stock=5")

    # Exclui o produto
    response = client.delete("/products/1")
    assert response.status_code == 200
    assert response.json()["msg"] == "Produto deletado com sucesso"
