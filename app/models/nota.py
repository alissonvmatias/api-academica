from sqlalchemy import Column, Integer, Float, ForeignKey
from app.database.db import Base

class Nota(Base):
    __tablename__ = "notas"

    id = Column(Integer, primary_key=True, index=True)
    valor = Column(Float, nullable=False)
    aluno_id = Column(Integer, ForeignKey("alunos.id"))
