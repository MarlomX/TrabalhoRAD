from repositorio.alunoRepositorio import AlunoRepositorio
from repositorio.professorRepositorio import ProfessorRepositorio
from repositorio.disciplinaRepositorio import DisciplinaRepositorio
from modelo.aluno import Aluno
from modelo.professor import Professor
from modelo.disciplina import Disciplina
from datetime import date

disciplina = Disciplina("BDDWE78854", "Banco_De_Dados")
DisciplinaRepositorio.Adiciona_Disciplina(disciplina=disciplina)

disciplina2 = Disciplina("POOWE", "POO")
DisciplinaRepositorio.Adiciona_Disciplina(disciplina=disciplina2)

disciplina3= Disciplina("SOWES", "SO")
DisciplinaRepositorio.Adiciona_Disciplina(disciplina=disciplina3)

aluno = Aluno(200208568457, "Albert", date(year=2002, month=6, day=19))
AlunoRepositorio.Adiciona_Aluno(aluno)

aluno.AdicionaDisciplina(disciplina=disciplina)
aluno.AdicionaDisciplina(disciplina=disciplina2)

aluno2 = Aluno(200609542368, "Rafael", date(year=2006, month=3, day=29))
AlunoRepositorio.Adiciona_Aluno(aluno2)

aluno2.AdicionaDisciplina(disciplina3)


professor = Professor(199002458768 ,"Gilbert", date(year=1990, month=9, day=1))
ProfessorRepositorio.Adiciona_Professor(professor=professor)

professor.AdicionaDisciplina(disciplina2)

professor2 = Professor(198808578423 ,"Pedro", date(year=1988, month=6, day=19))
ProfessorRepositorio.Adiciona_Professor(professor=professor2)

professor2.AdicionaDisciplina(disciplina)
professor2.AdicionaDisciplina(disciplina2)


print("Fim")