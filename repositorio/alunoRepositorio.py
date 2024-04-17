from datetime import date
from conecao.db import DB
from modelo.aluno import Aluno

class  AlunoRepositorio:
    
    def Adiciona_Aluno(aluno):
        if not isinstance(aluno, Aluno):
            raise ValueError("A variável 'aluno' deve ser uma instância da classe Aluno.")
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Aluno()
        Db.Cursor.execute(
            "INSERT INTO aluno VALUES (?, ?, ?)",(aluno.GetMatricula() , aluno.GetNome(), aluno.GetData()))
        Db.Conn.commit()
        Db.Encerra_Connection()
    
    def Edita_Aluno(aluno):
        if not isinstance(aluno, Aluno):
            raise ValueError("A variável 'aluno' deve ser uma instância da classe Aluno.")
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Aluno()
        Db.Cursor.execute("UPDATE aluno SET Nome = ?, DataDeNascimento = ? WHERE Matricula = ?",(aluno.GetNome(), aluno.GetData(), aluno.GetMatricula()))
        Db.Conn.commit()
        Db.Encerra_Connection()
    
    def Busca_Aluno_Matricula(matricula) -> Aluno:
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Aluno()
        Db.Cursor.execute("SELECT Nome, DataDeNascimento FROM aluno WHERE Matricula = ?", (matricula,))
        Db.Conn.commit()
        resultado = Db.Cursor.fetchone()
        Db.Encerra_Connection()
        if resultado:
            nome, data = resultado
            return Aluno(matricula=matricula, nome=nome, data=data)
        else:
            return None
    
    def Busca_Todos_Alunos():
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Aluno()
        Db.Cursor.execute("SELECT Matricula, Nome, DataDeNascimento FROM aluno")
        Db.Conn.commit()
        resultado = Db.Cursor.fetchall()
        Db.Encerra_Connection()
        if resultado:
            Alunos = []
            for aluno in resultado:
                matricula, nome, data = aluno
                Alunos.append(Aluno(matricula, nome, data=data))
            return Alunos
        else:
            return None
    
    def Busca_Todas_Matriculas():
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Aluno()
        Db.Cursor.execute("SELECT Matricula FROM aluno")
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
    
    def Deleta_Aluno(aluno):
        if not isinstance(aluno, Aluno):
            raise ValueError("A variável 'aluno' deve ser uma instância da classe Aluno.")
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Aluno()
        Db.Cursor.execute("DELETE FROM aluno WHERE Matricula = ?",(aluno.GetMatricula(),))
        Db.Conn.commit()
        Db.Encerra_Connection()
    