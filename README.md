# 🚀 API REST em Python (FastAPI + PostgreSQL)

## 📖 Descrição
Este projeto é uma **API REST** desenvolvida em **Python** utilizando **FastAPI**, com autenticação via **JWT** e integração com **PostgreSQL**.  
O objetivo é demonstrar boas práticas de desenvolvimento back-end, incluindo organização em camadas, segurança e documentação automática.

---

## 🛠 Tecnologias
- Python 3.13  
- FastAPI  
- PostgreSQL  
- SQLAlchemy  
- JWT (python-jose)  
- Docker (opcional)  
- Git  
- Pytest (testes automatizados)



---

Crie e ative o ambiente virtual

``` python
python -m venv venv
```
```
source venv/bin/activate   # Linux/Mac
```
```
venv\Scripts\activate      # Windows
```

Instale as dependências

```
pip install -r requirements.txt
```

🔐 Configuração do .env
Crie um arquivo .env na raiz do projeto com as variáveis:

env
```
DATABASE_URL=postgresql://USUARIO:SENHA@localhost:5432/NOME_DO_BANCO
SECRET_KEY=chave_super_secreta
```
⚠️ Importante:

Substitua USUARIO, SENHA e NOME_DO_BANCO pelos valores do seu ambiente.

Adicione .env ao .gitignore para não expor credenciais no GitHub.

🗄️ Banco de Dados
Crie o banco no PostgreSQL:

```
CREATE DATABASE NOME_DO_BANCO;
```
Verifique se o encoding está em UTF-8:


SHOW SERVER_ENCODING;
▶️ Executando a aplicação
Rode o servidor:

```
uvicorn main:app --reload
```
Acesse a documentação automática:
👉 http://localhost:8000/docs (localhost in Bing)

📂 Endpoints principais
- POST /register → Criar usuário

- POST /login → Autenticação e geração de token JWT

- GET /users → Listar usuários (rota protegida)

- POST /products → Criar produto

- GET /products → Listar produtos

- PUT /products/{id} → Atualizar produto

- DELETE /products/{id} → Excluir produto

🧪 Testes automatizados
Os testes foram criados com pytest e estão na pasta tests/.

Exemplo de execução:

```
pytest -v
```
Testes disponíveis:

test_main.py → Registro de usuário, login, criação e listagem de produtos.

test_update_product.py → Atualização de produto.

test_delete_product.py → Exclusão de produto.