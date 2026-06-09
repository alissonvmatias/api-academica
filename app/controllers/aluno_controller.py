from sqlalchemy.orm import Session
from app.models.aluno import Aluno

def criar_aluno(db: Session, nome: str):
    if not nome:
        raise ValueError("Nome é obrigatório")

    if db.query(Aluno).filter(Aluno.nome == nome).first():
        raise ValueError("Aluno já cadastrado")

    aluno = Aluno(nome=nome)
    db.add(aluno)
    db.commit()
    db.refresh(aluno)
    return aluno

def listar_alunos(db: Session):
    return db.query(Aluno).all()

def atualizar_aluno(db: Session, aluno_id: int, nome: str):
    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()

    if not aluno:
        raise ValueError("Aluno não encontrado")

    aluno.nome = nome
    db.commit()
    return aluno

def deletar_aluno(db: Session, aluno_id: int):
    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()

    if not aluno:
        raise ValueError("Aluno não encontrado")

    db.delete(aluno)
    db.commit()
    return {"mensagem": "Aluno deletado"}

