import sqlite3

class DB:
    
    def __init__(self) -> None:
        self.Conn =  None
        self.Cursor = None
    
    def Inicia_Connection(self):
        self.Conn = sqlite3.connect("Faculdade.db")
        self.Cursor = self.Conn.cursor()
    
    def Encerra_Connection(self):
        self.Conn.close()
        
    def Inicia_DB_Aluno(self):
        self.Inicia_Connection()
        self.Cursor.execute(
        "CREATE TABLE IF NOT EXISTS aluno \
            (Matricula INT PRIMARY KEY, Nome VARCHAR(50), DataDeNascimento DATE)")
        self.Conn.commit()
    
    def Inicia_DB_Professor(self):
        self.Inicia_Connection()
        self.Cursor.execute(
        "CREATE TABLE IF NOT EXISTS professor \
            (Matricula INT PRIMARY KEY, Nome VARCHAR(50), DataDeNascimento DATE)")
        self.Conn.commit()
    
    def Inicia_DB_Disciplina(self):
        self.Inicia_Connection()
        self.Cursor.execute(
            "CREATE TABLE IF NOT EXISTS disciplina \
                (Codigo VarChar(10) PRIMARY KEY, Nome VARCHAR(30))")
        self.Conn.commit()
    
    def Inicia_DB_Matriculado(self):
        self.Inicia_Connection()
        self.Cursor.execute(
            "CREATE TABLE IF NOT EXISTS matriculado \
            (MatriculaAluno INT, CodigoDisciplina VARCHAR(20), \
            PRIMARY KEY (MatriculaAluno, CodigoDisciplina), \
            FOREIGN KEY (MatriculaAluno) REFERENCES aluno(Matricula), \
            FOREIGN KEY (CodigoDisciplina) REFERENCES disciplina(Codigo))")
        self.Conn.commit()
    
    def Inicia_DB_Lecionando(self):
        self.Inicia_Connection()
        self.Cursor.execute(
            "CREATE TABLE IF NOT EXISTS lecionando \
            (MatriculaProfessor INT, CodigoDisciplina VARCHAR(20), \
            PRIMARY KEY (MatriculaProfessor, CodigoDisciplina), \
            FOREIGN KEY (MatriculaProfessor) REFERENCES professor(Matricula), \
            FOREIGN KEY (CodigoDisciplina) REFERENCES disciplina(Codigo))")
        self.Conn.commit()
        
    

    