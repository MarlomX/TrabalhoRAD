from conecao.db import DB
from modelo.aluno import Aluno
from modelo.disciplina import Disciplina
from repositorio.disciplinaRepositorio import DisciplinaRepositorio
from repositorio.alunoRepositorio import AlunoRepositorio

class MatriculadoRepositorio:
    
    def Adiciona_Matriculado(aluno, disciplina):
        if not isinstance(disciplina, Disciplina):
            raise ValueError("A variável 'disciplina' deve ser uma instância da classe Disciplina.")
        elif not isinstance(aluno, Aluno):
            raise ValueError("A variável 'aluno' deve ser uma instância da classe Aluno.")
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Matriculado()
        Db.Cursor.execute(
            "INSERT INTO matriculado VALUES (?, ?)",(aluno.GetMatricula() , disciplina.GetCodigo()))
        Db.Conn.commit()
        Db.Encerra_Connection()
    
    def Busca_Disciplinas_Aluno(matricula):
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Matriculado()
        Db.Cursor.execute("SELECT CodigoDisciplina FROM matriculado WHERE MatriculaAluno = ?", (matricula, ))
        Db.Conn.commit()
        resultado = Db.Cursor.fetchall()
        Db.Encerra_Connection()
        Disciplinas = []
        for codDisciplina in resultado:
            codigo = codDisciplina[0]
            disciplina = DisciplinaRepositorio.Busca_Disciplina_Codigo(codigo=codigo)
            Disciplinas.append(disciplina)
        return Disciplinas
    
    def Busca_Aluno_Disciplinas(codigo):
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Matriculado()
        Db.Cursor.execute("SELECT MatriculaAluno FROM matriculado WHERE CodigoDisciplina = ?", (codigo, ))
        Db.Conn.commit()
        resultado = Db.Cursor.fetchall()
        Db.Encerra_Connection()
        Alunos = []
        for maticulaAluno in resultado:
            matricula = maticulaAluno[0]
            aluno = AlunoRepositorio.Busca_Aluno_Matricula(matricula=matricula)
            Alunos.append(aluno)
        return Alunos
    
    def Deleta_Matriculado(aluno, disciplina):
        if not isinstance(disciplina, Disciplina):
            raise ValueError("A variável 'disciplina' deve ser uma instância da classe Disciplina.")
        elif not isinstance(aluno, Aluno):
            raise ValueError("A variável 'aluno' deve ser uma instância da classe Aluno.")
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Matriculado()
        Db.Cursor.execute("DELETE FROM matriculado WHERE MatriculaAluno = ? AND CodigoDisciplina = ?",(aluno.GetMatricula(), disciplina.GetCodigo(),))
        Db.Conn.commit()
        Db.Encerra_Connection()