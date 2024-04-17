from conecao.db import DB
from modelo.professor import Professor
from repositorio.professorRepositorio import ProfessorRepositorio
from modelo.disciplina import Disciplina
from repositorio.disciplinaRepositorio import DisciplinaRepositorio

class LecionandoRepositorio:
    
    def Adiciona_Lecionando(professor, disciplina):
        if not isinstance(disciplina, Disciplina):
            raise ValueError("A variável 'disciplina' deve ser uma instância da classe Disciplina.")
        elif not isinstance(professor, Professor):
            raise ValueError("A variável 'professor' deve ser uma instância da classe Professor.")
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Lecionando()
        Db.Cursor.execute(
            "INSERT INTO lecionando VALUES (?, ?)",(professor.GetMatricula() , disciplina.GetCodigo()))
        Db.Conn.commit()
        Db.Encerra_Connection()
    
    def Busca_Disciplinas_Professor(matricula):
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Lecionando()
        Db.Cursor.execute("SELECT CodigoDisciplina FROM lecionando WHERE MatriculaProfessor = ?", (matricula, ))
        Db.Conn.commit()
        resultado = Db.Cursor.fetchall()
        Db.Encerra_Connection()
        Disciplinas = []
        for codDisciplina in resultado:
            codigo = codDisciplina[0]
            disciplina = DisciplinaRepositorio.Busca_Disciplina_Codigo(codigo=codigo)
            Disciplinas.append(disciplina)
        return Disciplinas
    
    def Busca_Professor_Disciplinas(codigo):
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Lecionando()
        Db.Cursor.execute("SELECT MatriculaProfessor FROM lecionando WHERE CodigoDisciplina = ?", (codigo, ))
        Db.Conn.commit()
        resultado = Db.Cursor.fetchall()
        Db.Encerra_Connection()
        professores = []
        for matricula_professor in resultado:
            matricula = matricula_professor[0]
            professor = ProfessorRepositorio.Busca_Professor_Matricula(matricula=matricula)
            professores.append(professor)
        return professores
    
    def Deleta_Lecionando(professor, disciplina):
        if not isinstance(disciplina, Disciplina):
            raise ValueError("A variável 'disciplina' deve ser uma instância da classe Disciplina.")
        elif not isinstance(professor, Professor):
            raise ValueError("A variável 'professor' deve ser uma instância da classe Professor.")
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Lecionando()
        Db.Cursor.execute("DELETE FROM lecionando WHERE MatriculaProfessor = ? AND CodigoDisciplina = ?",(professor.GetMatricula(), disciplina.GetCodigo(),))
        Db.Conn.commit()
        Db.Encerra_Connection()