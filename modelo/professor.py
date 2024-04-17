from datetime import date
from modelo.disciplina import Disciplina

class Professor:

    def __init__(self, matricula, nome, data) -> None:
        self.__Matricula__ = matricula
        self.__Nome__ = nome
        self.__Data__ = data
        self.__Disciplinas__ = []
        
    def GetMatricula(self)->int:
        return self.__Matricula__
    
    def GetNome(self)->str:
        return self.__Nome__
    
    def GetData(self) -> date:
        return self.__Data__
    
    def GetDisciplinas(self):
        return self.__Disciplinas__
    
    def BuscarDisciplinas(self):
        from repositorio.lecionandoRepositoio import LecionandoRepositorio
        self.__Disciplinas__ = LecionandoRepositorio.Busca_Disciplinas_Professor(self.GetMatricula())
    
    def atualisar_disciplinas(self, codigos_disciplinas): 
        from repositorio.disciplinaRepositorio import DisciplinaRepositorio
        
        self.BuscarDisciplinas()

        #Pega os codigos das disciplinas e transforma em objetos Disciplinas e coloca em uma lista
        disciplinas_atualizadas =  []
        for codigo in codigos_disciplinas:
            disciplina_nova = DisciplinaRepositorio.Busca_Disciplina_Codigo(codigo=codigo)
            disciplinas_atualizadas.append(disciplina_nova)

        #Remove as disciplinas que não foram recebidas pelo usuario
        for disciplina in self.GetDisciplinas():
            if disciplina not in disciplinas_atualizadas:
                self.RemoveDisciplina(disciplina=disciplina)

        #Adiciona as novas disciplinas recebidas pelo usuario
        for disciplina in disciplinas_atualizadas:
            if disciplina not in self.GetDisciplinas():
                self.AdicionaDisciplina(disciplina=disciplina)
    
    def AdicionaDisciplina(self, disciplina):
        from repositorio.lecionandoRepositoio import LecionandoRepositorio
        if not isinstance(disciplina, Disciplina):
            raise ValueError("A variável 'disciplina' deve ser uma instância da classe Disciplina.")
        LecionandoRepositorio.Adiciona_Lecionando(professor=self, disciplina=disciplina)
    
    def RemoveDisciplina(self, disciplina):
        from repositorio.lecionandoRepositoio import LecionandoRepositorio
        if not isinstance(disciplina, Disciplina):
            raise ValueError("A variável 'disciplina' deve ser uma instância da classe Disciplina.")
        LecionandoRepositorio.Deleta_Lecionando(professor=self , disciplina=disciplina)
    
    def __str__(self) -> str:
        return self.GetNome()