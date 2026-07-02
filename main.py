from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from models import User
from auth import hash_password, verify_password, create_access_token

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    user = User(username=username, password=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"msg": "Usuário criado com sucesso"}

@app.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Credenciais inválidas")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
