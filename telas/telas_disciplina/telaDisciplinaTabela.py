import tkinter as tk
from tkinter import ttk
from modelo.disciplina import Disciplina
from repositorio.disciplinaRepositorio import DisciplinaRepositorio
import suporte.Utilidades as Utilidades

class TelaDisciplinaTabela:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabela de Disciplinas")
        
        #Título da tabela
        self.titulo = tk.Label(root, text="Tabela de Disciplinas", font=("Helvetica", 16))
        self.titulo.pack(pady=10)
        
        #Criar a grade (grid) para exibir os dados
        self.tabela = ttk.Treeview(root, columns=("Nome", "Codigo", "Alnos Matriculados", "Professor(es) Responsavel(is)"), show="headings")
        self.tabela.heading("#1", text="Nome", anchor="w")
        self.tabela.heading("#2", text="Codigo", anchor="w")
        self.tabela.heading("#3", text="Professores", anchor="w")
        self.tabela.heading("#4", text="Alunos", anchor="w")
        self.tabela.pack(fill="both", expand=True)
        
        disciplinas = DisciplinaRepositorio.Busca_Todas_Disciplinas()
        if disciplinas != None:
            for disciplina in disciplinas:
                self.atualiza_tabela(disciplina)
        
        #Botões
        self.botao_adicionar = tk.Button(root, text="Adicionar", command=self.tela_adicionar_disciplina)
        self.botao_editar = tk.Button(root, text="Editar", command=self.tela_editar_disciplina)
        self.botao_deletar = tk.Button(root, text="Deletar", command=self.deletar_disciplina)
        self.botao_voltar = tk.Button(root, text="Voltar", command=self.tela_voltar)
        
        self.botao_adicionar.pack(side="left", padx=10)
        self.botao_editar.pack(side="left", padx=10)
        self.botao_deletar.pack(side="left", padx=10)
        self.botao_voltar.pack(side="left", padx=10)
    
    def atualiza_tabela(self, disciplina):
        if not isinstance(disciplina, Disciplina):
            raise ValueError("A variável 'disciplina' deve ser uma instância da classe Disciplina.")
        disciplina.atualiza_professores_e_alunos()
        self.tabela.insert("", "end", values=(disciplina.GetNome(), disciplina.GetCodigo(), disciplina.GetProfessores(), disciplina.GetAlunos()))

    def deletar_disciplina(self):
        item_selecionado = self.tabela.selection()
        if item_selecionado:
            # Obtém os valores das colunas para o item selecionado
            codigo = self.tabela.item(item_selecionado, "values")[1]
            disciplina = DisciplinaRepositorio.Busca_Disciplina_Codigo(codigo=codigo)
            
            #Deleta todas as relações da disciplina
            disciplina.atualiza_professores_e_alunos()
            
            for professor in disciplina.GetProfessores():
                professor.RemoveDisciplina(disciplina=disciplina)
            
            for aluno in disciplina.GetAlunos():
                aluno.RemoveDisciplina(disciplina=disciplina)
            
            #Deleta a disciplina
            DisciplinaRepositorio.Deleta_Disciplina(disciplina=disciplina)
            
            #Renicia a pagina
            Utilidades.mudar_de_tela(self.root, TelaDisciplinaTabela)
                   

    def tela_editar_disciplina(self):
        item_selecionado = self.tabela.selection()
        if item_selecionado:
            from telas.telas_disciplina.telaDisciplinaEditar import TelaDisciplinaEditar
            
            # Obtém os valores das colunas para o item selecionado
            codigo = self.tabela.item(item_selecionado, "values")[1]
            
            # Muda de tela
            Utilidades.mudar_de_tela_com_dados(root=self.root ,tela_a_mudar=TelaDisciplinaEditar, dados=codigo)
    
    def tela_voltar(self):
        from telaInicial import TelaInicial
        Utilidades.mudar_de_tela(self.root, TelaInicial)

    def tela_adicionar_disciplina(self):
        from telas.telas_disciplina.telaDisciplinaAdicionar import TelaDisciplinaAdicionar
        Utilidades.mudar_de_tela(self.root, TelaDisciplinaAdicionar)

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaDisciplinaTabela(root)
    # Definir o tamanho da janela com base nas dimensões da tela
    root.geometry("800x600")  # Ajuste conforme necessário
    root.mainloop()