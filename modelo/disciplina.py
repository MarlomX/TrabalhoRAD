
class Disciplina:
    def __init__(self, codigo, nome) -> None:
        self.__codigo__ = codigo
        self.__nome__ = nome
        self.__profesores__ = []
        self.__alunos__ = []
    
    def GetNome(self)-> str:
        return self.__nome__
    
    def GetCodigo(self)->str:
        return self.__codigo__
    
    def GetProfessores(self):
        return self.__profesores__
    
    def GetAlunos(self):
        return self.__alunos__
    
    def atualiza_professores_e_alunos(self):
        from repositorio.lecionandoRepositoio import LecionandoRepositorio
        self.__profesores__ = LecionandoRepositorio.Busca_Professor_Disciplinas(codigo=self.GetCodigo())
        
        from repositorio.matriculadoRepositorio import MatriculadoRepositorio
        self.__alunos__ = MatriculadoRepositorio.Busca_Aluno_Disciplinas(codigo=self.GetCodigo())
    
    def __str__(self) -> str:
        return self.GetNome()
    
    def  __eq__(self, value: object) -> bool:
        if isinstance(value, Disciplina):
            if self.GetCodigo() == value.GetCodigo():
                return True
        return False