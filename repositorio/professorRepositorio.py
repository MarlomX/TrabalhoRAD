from datetime import date
from conecao.db import DB
from modelo.professor import Professor

class  ProfessorRepositorio:
    
    def Adiciona_Professor(professor):
        if not isinstance(professor, Professor):
            raise ValueError("A variável 'professor' deve ser uma instância da classe Professor.")
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Professor()
        Db.Cursor.execute(
            "INSERT INTO professor VALUES (?, ?, ?)",(professor.GetMatricula() , professor.GetNome(), professor.GetData()))
        Db.Conn.commit()
        Db.Encerra_Connection()
    
    def Edita_Professor(professor):
        if not isinstance(professor, Professor):
            raise ValueError("A variável 'professor' deve ser uma instância da classe Professor.")
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Professor()
        Db.Cursor.execute("UPDATE professor SET Nome = ?, DataDeNascimento = ? WHERE Matricula = ?",(professor.GetNome(), professor.GetData(), professor.GetMatricula()))
        Db.Conn.commit()
        Db.Encerra_Connection()
    
    def Busca_Professor_Matricula(matricula) -> Professor:
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Professor()
        Db.Cursor.execute("SELECT Nome, DataDeNascimento FROM professor WHERE Matricula = ?", (matricula,))
        Db.Conn.commit()
        resultado = Db.Cursor.fetchone()
        Db.Encerra_Connection()
        if resultado:
            nome, data = resultado
            return Professor(matricula=matricula, nome=nome, data=data)
        else:
            return None
    
    def Busca_Todos_Professores():
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Professor()
        Db.Cursor.execute("SELECT Matricula, Nome, DataDeNascimento FROM professor")
        Db.Conn.commit()
        resultado = Db.Cursor.fetchall()
        Db.Encerra_Connection()
        if resultado:
            Professores = []
            for professor in resultado:
                matricula, nome, data = professor
                Professores.append(Professor(matricula, nome, data))
            return Professores
        else:
            return None
    
    def Busca_Todas_Matriculas():
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Aluno()
        Db.Cursor.execute("SELECT Matricula FROM professor")
        Db.Conn.commit()
        resultado = Db.Cursor.fetchall()
        Db.Encerra_Connection()
        if resultado:
            matriculas = []
            for matricula in resultado:
                 matriculas.append(str(matricula[0]))
            return matriculas
        else:
            return None
    
    def Deleta_Professor(professor):
        if not isinstance(professor, Professor):
            raise ValueError("A variável 'professor' deve ser uma instância da classe Professor.")
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Professor()
        Db.Cursor.execute("DELETE FROM professor WHERE Matricula = ?",(professor.GetMatricula(),))
        Db.Conn.commit()
        Db.Encerra_Connection()
