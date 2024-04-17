from conecao.db import DB
from modelo.disciplina import Disciplina

class DisciplinaRepositorio:
    
    def Adiciona_Disciplina(disciplina):
        if not isinstance(disciplina, Disciplina):
            raise ValueError("A variável 'disciplina' deve ser uma instância da classe Disciplina.")
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Disciplina()
        Db.Cursor.execute(
            "INSERT INTO disciplina VALUES (?, ?)",(disciplina.GetCodigo() , disciplina.GetNome()))
        Db.Conn.commit()
        Db.Encerra_Connection()
    
    def Edita_Disciplina(disciplina):
        if not isinstance(disciplina, Disciplina):
            raise ValueError("A variável 'disciplina' deve ser uma instância da classe Disciplina.")
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Disciplina()
        Db.Cursor.execute("UPDATE disciplina SET Nome = ? WHERE Codigo = ?",(disciplina.GetNome(), disciplina.GetCodigo()))
        Db.Conn.commit()
        Db.Encerra_Connection()
    
    def Busca_Disciplina_Codigo(codigo) -> Disciplina:
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Disciplina()
        Db.Cursor.execute("SELECT Nome FROM disciplina WHERE Codigo = ?", (codigo,))
        Db.Conn.commit()
        resultado = Db.Cursor.fetchone()
        Db.Encerra_Connection()
        if resultado:
            nome = resultado[0]
            return Disciplina(codigo=codigo, nome=nome)
        else:
            print("Disciplina não enontrada")
            return None
    
    def Busca_Todas_Disciplinas():
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Disciplina()
        Db.Cursor.execute("SELECT Codigo, Nome FROM Disciplina")
        Db.Conn.commit()
        resultado = Db.Cursor.fetchall()
        Db.Encerra_Connection()
        if resultado:
            Disciplinas = []
            for disciplina in resultado:
                codigo, nome = disciplina
                Disciplinas.append(Disciplina(codigo=codigo, nome=nome))
            return Disciplinas
        else:
            return None
        
    def Busca_Todao_Codigos():
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Disciplina()
        Db.Cursor.execute("SELECT Codigo FROM Disciplina")
        Db.Conn.commit()
        resultado = Db.Cursor.fetchall()
        Db.Encerra_Connection()
        if resultado:
            Codigos = []
            for codigo in resultado:
                Codigos.append(codigo[0])
            return Codigos
        else:
            return None
    
    def Deleta_Disciplina(disciplina):
        if not isinstance(disciplina, Disciplina):
            raise ValueError("A variável 'disciplina' deve ser uma instância da classe Disciplina.")
        Db = DB()
        Db.Inicia_Connection()
        Db.Inicia_DB_Disciplina()
        Db.Cursor.execute("DELETE FROM disciplina WHERE Codigo = ?",(disciplina.GetCodigo(),))
        Db.Conn.commit()
        Db.Encerra_Connection()