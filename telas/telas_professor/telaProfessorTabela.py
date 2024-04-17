import tkinter as tk
from tkinter import ttk
from modelo.professor import Professor
from repositorio.professorRepositorio import ProfessorRepositorio
import suporte.Utilidades as Utilidades

class TelaProfessorTabela:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabela de Professores")

        # Título da tabela
        self.titulo = tk.Label(root, text="Tabela de Professores", font=("Helvetica", 16))
        self.titulo.pack(pady=10)

        # Criar a grade (grid) para exibir os dados
        self.tabela = ttk.Treeview(root, columns=("Nome", "Matrícula", "Data de Nascimento", "Disciplinas"), show="headings")
        self.tabela.heading("#1", text="Nome", anchor="w")  # Alinhar à esquerda
        self.tabela.heading("#2", text="Matrícula", anchor="w")  # Alinhar à esquerda
        self.tabela.heading("#3", text="Data de Nascimento", anchor="w")  # Alinhar à esquerda
        self.tabela.heading("#4", text="Disciplinas", anchor="w")  # Alinhar à esquerda
        self.tabela.pack(fill="both", expand=True)  # Preencher toda a janela

        professores = ProfessorRepositorio.Busca_Todos_Professores()
        if professores != None:
            for professor in professores:
                self.atualiza_tabela(professor)

        # Botões
        self.botao_adicionar = tk.Button(root, text="Adicionar", command=self.tela_adicionar_professor)
        self.botao_editar = tk.Button(root, text="Editar", command=self.tela_editar_professor)
        self.botao_deletar = tk.Button(root, text="Deletar", command=self.deletar_professor)
        self.botao_voltar = tk.Button(root, text="Voltar", command=self.tela_voltar)
        
        
        self.botao_adicionar.pack(side="left", padx=10)
        self.botao_editar.pack(side="left", padx=10)
        self.botao_deletar.pack(side="left", padx=10)
        self.botao_voltar.pack(side="left", padx=10)

    def atualiza_tabela(self, professor):
        if not isinstance(professor, Professor):
            raise ValueError("A variável 'professor' deve ser uma instância da classe Professor.")
        professor.BuscarDisciplinas()
        self.tabela.insert("", "end", values=(professor.GetNome(), professor.GetMatricula(), professor.GetData(), professor.GetDisciplinas()))

    def deletar_professor(self):
        item_selecionado = self.tabela.selection()
        if item_selecionado:
            # Obtém os valores das colunas para o item selecionado
            matricula = self.tabela.item(item_selecionado, "values")[1]
            professor = ProfessorRepositorio.Busca_Professor_Matricula(matricula=matricula)
            
            #Deleta todas as relações do professor
            professor.BuscarDisciplinas()
            for disciplina in professor.GetDisciplinas():
                professor.RemoveDisciplina(disciplina=disciplina)
            
            #Deleta o professor
            ProfessorRepositorio.Deleta_Professor(professor=professor)
            
            #Renicia a pagina
            Utilidades.mudar_de_tela(self.root, TelaProfessorTabela)
                   

    def tela_editar_professor(self):
        item_selecionado = self.tabela.selection()
        if item_selecionado:
            from telas.telas_professor.telaProfessorEditar import TelaProfessorEditar
            
            # Obtém os valores das colunas para o item selecionado
            matricula = self.tabela.item(item_selecionado, "values")[1]
            
            # Muda de tela
            Utilidades.mudar_de_tela_com_dados(self.root ,TelaProfessorEditar, matricula)
    
    def tela_voltar(self):
        from telaInicial import TelaInicial
        Utilidades.mudar_de_tela(self.root, TelaInicial)

    def tela_adicionar_professor(self):
        from telas.telas_professor.telaProfessorAdicionar import TelaProfessorAdicionar
        Utilidades.mudar_de_tela(self.root, TelaProfessorAdicionar)

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaProfessorTabela(root)
    # Definir o tamanho da janela com base nas dimensões da tela
    root.geometry("800x600")  # Ajuste conforme necessário
    root.mainloop()