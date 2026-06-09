from pydantic import BaseModel, Field

class NotaCriar(BaseModel):
    aluno_id: int
    valor: float = Field(..., ge=0, le=10)

class NotaResposta(BaseModel):
    id: int
    aluno_id: int
    valor: float

    class Config:
        from_attributes = True

class SituacaoResposta(BaseModel):
    media: float
    situacao: str


