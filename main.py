from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from models import User
from auth import hash_password, verify_password, create_access_token

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
