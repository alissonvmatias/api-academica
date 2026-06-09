from sqlalchemy.orm import Session
from app.models.nota import Nota

def lancar_nota(db: Session, aluno_id: int, valor: float):
    if valor < 0 or valor > 10:
        raise ValueError("Nota inválida")

    nota = Nota(aluno_id=aluno_id, valor=valor)
    db.add(nota)
    db.commit()
    db.refresh(nota)
    return nota

def calcular_situacao(db: Session, aluno_id: int):
    notas = db.query(Nota).filter(Nota.aluno_id == aluno_id).all()

    if not notas:
        return {"media": 0, "situacao": "Sem notas"}

    media = sum(n.valor for n in notas) / len(notas)
    situacao = "Aprovado" if media >= 7 else "Reprovado"

    return {"media": round(media, 2), "situacao": situacao}
