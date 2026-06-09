from pydantic import BaseModel

class AlunoCriar(BaseModel):
    nome: str

class AlunoAtualizar(BaseModel):
    nome: str

class AlunoResposta(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True


