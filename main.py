from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from models import User
from auth import hash_password, verify_password, create_access_token
from models import Product

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para registrar usuário
@app.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    if len(password) > 72:
        raise HTTPException(status_code=400, detail="Senha não pode ter mais que 72 caracteres")

    user = User(username=username, hashed_password=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"msg": "Usuário criado com sucesso", "id": user.id, "username": user.username}

@app.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Credenciais inválidas")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

# Criar produto
@app.post("/products")
def create_product(name: str, description: str, price: float, stock: int, db: Session = Depends(get_db)):
    product = Product(name=name, description=description, price=price, stock=stock)
    db.add(product)
    db.commit()
    db.refresh(product)
    return {"msg": "Produto criado com sucesso", "id": product.id}

# Listar produtos
@app.get("/products")
def list_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products

# Atualizar produto
@app.put("/products/{product_id}")
def update_product(product_id: int, name: str, description: str, price: float, stock: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    product.name = name
    product.description = description
    product.price = price
    product.stock = stock
    db.commit()
    db.refresh(product)
    return {"msg": "Produto atualizado com sucesso"}

# Deletar produto
@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    db.delete(product)
    db.commit()
    return {"msg": "Produto deletado com sucesso"}
