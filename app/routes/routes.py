from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.schemas.aluno_schema import AlunoCriar, AlunoAtualizar, AlunoResposta
from app.schemas.nota_schema import NotaCriar, NotaResposta, SituacaoResposta
from app.controllers import aluno_controller, nota_controller

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/alunos", response_model=AlunoResposta, tags=["Alunos"], summary="Cadastrar um novo aluno", response_description="Aluno cadastrado com sucesso")
def criar_aluno(aluno: AlunoCriar, db: Session = Depends(get_db)):
    try:
        return aluno_controller.criar_aluno(db, aluno.nome)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/alunos", response_model=list[AlunoResposta], tags=["Alunos"], summary="Listar todos os alunos", response_description="Lista de alunos retornada com sucesso")
def listar(db: Session = Depends(get_db)):
    return aluno_controller.listar_alunos(db)

@router.put("/alunos/{aluno_id}", response_model=AlunoResposta, tags=["Alunos"], summary="Atualizar dados de um aluno", response_description="Aluno atualizado com sucesso")
def atualizar(aluno_id: int, aluno: AlunoAtualizar, db: Session = Depends(get_db)):
    try:
        return aluno_controller.atualizar_aluno(db, aluno_id, aluno.nome)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/alunos/{aluno_id}", tags=["Alunos"], summary="Excluir um aluno", response_description="Aluno excluído com sucesso")
def deletar(aluno_id: int, db: Session = Depends(get_db)):
    try:
        return aluno_controller.deletar_aluno(db, aluno_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/notas", response_model=NotaResposta, tags=["Notas"], summary="Lançar uma nota para um aluno", response_description="Nota lançada com sucesso")
def lancar_nota(nota: NotaCriar, db: Session = Depends(get_db)):
    try:
        return nota_controller.lancar_nota(db, nota.aluno_id, nota.valor)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/alunos/{aluno_id}/situacao", response_model=SituacaoResposta, tags=["Alunos"], summary="Obter situação acadêmica do aluno", response_description="Média e situação calculadas com sucesso")
def situacao(aluno_id: int, db: Session = Depends(get_db)):
    return nota_controller.calcular_situacao(db, aluno_id)


