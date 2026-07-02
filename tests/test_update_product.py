import pytest
from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

client = TestClient(app)

def test_update_product():
    # Cria produto inicial
    client.post("/products?name=Mouse&description=Sem fio&price=150&stock=20")

    # Atualiza o produto
    response = client.put("/products/1?name=Mouse Gamer&description=RGB&price=250&stock=15")
    assert response.status_code == 200
    assert response.json()["msg"] == "Produto atualizado com sucesso"
