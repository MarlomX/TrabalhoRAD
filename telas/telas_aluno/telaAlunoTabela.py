import tkinter as tk
from tkinter import ttk
from modelo.aluno import Aluno
from repositorio.alunoRepositorio import AlunoRepositorio
import suporte.Utilidades as Utilidades

class TelaAlunoTabela:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabela de Alunos")

        # Título da tabela
        self.titulo = tk.Label(root, text="Tabela de Alunos", font=("Helvetica", 16))
        self.titulo.pack(pady=10)

        # Criar a grade (grid) para exibir os dados
        self.tabela = ttk.Treeview(root, columns=("Nome", "Matrícula", "Data de Nascimento", "Disciplinas"), show="headings")
        self.tabela.heading("#1", text="Nome", anchor="w")  # Alinhar à esquerda
        self.tabela.heading("#2", text="Matrícula", anchor="w")  # Alinhar à esquerda
        self.tabela.heading("#3", text="Data de Nascimento", anchor="w")  # Alinhar à esquerda
        self.tabela.heading("#4", text="Disciplinas", anchor="w")  # Alinhar à esquerda
        self.tabela.pack(fill="both", expand=True)  # Preencher toda a janela

        alunos = AlunoRepositorio.Busca_Todos_Alunos()
        if  alunos != None:
            for aluno in alunos:
                self.atualiza_tabela(aluno)

        # Botões
        self.botao_adicionar = tk.Button(root, text="Adicionar", command=self.tela_adicionar_aluno)
        self.botao_editar = tk.Button(root, text="Editar", command=self.tela_editar_aluno)
        self.botao_deletar = tk.Button(root, text="Deletar", command=self.deletar_aluno)
        self.botao_voltar = tk.Button(root, text="Voltar", command=self.tela_voltar)
        
        
        self.botao_adicionar.pack(side="left", padx=10)
        self.botao_editar.pack(side="left", padx=10)
        self.botao_deletar.pack(side="left", padx=10)
        self.botao_voltar.pack(side="left", padx=10)

    def atualiza_tabela(self, aluno):
        if not isinstance(aluno, Aluno):
            raise ValueError("A variável 'aluno' deve ser uma instância da classe Aluno.")
        aluno.BuscaDisciplinas()
        self.tabela.insert("", "end", values=(aluno.GetNome(), aluno.GetMatricula(), aluno.GetData(), aluno.GetDisciplinas()))

    def deletar_aluno(self):
        item_selecionado = self.tabela.selection()
        if item_selecionado:
            # Obtém os valores das colunas para o item selecionado
            matricula = self.tabela.item(item_selecionado, "values")[1]
            aluno = AlunoRepositorio.Busca_Aluno_Matricula(matricula=matricula)
            
            #Deleta todas as relações do aluno
            aluno.BuscaDisciplinas()
            for disciplina in aluno.GetDisciplinas():
                aluno.RemoveDisciplina(disciplina=disciplina)
            
            #Deleta o aluno
            AlunoRepositorio.Deleta_Aluno(aluno=aluno)
            
            #Renicia a pagina
            Utilidades.mudar_de_tela(self.root, TelaAlunoTabela)
                   

    def tela_editar_aluno(self):
        item_selecionado = self.tabela.selection()
        if item_selecionado:
            from telas.telas_aluno.telaAlunoEditar import TelaAlunoEditar
            
            # Obtém os valores das colunas para o item selecionado
            matricula = self.tabela.item(item_selecionado, "values")[1]
            
            # Muda de tela
            Utilidades.mudar_de_tela_com_dados(self.root ,TelaAlunoEditar, matricula)
    
    def tela_voltar(self):
        from telaInicial import TelaInicial
        Utilidades.mudar_de_tela(self.root, TelaInicial)

    def tela_adicionar_aluno(self):
        from telas.telas_aluno.telaAlunoAdicionar import TelaAlunoAdicionar
        Utilidades.mudar_de_tela(self.root, TelaAlunoAdicionar)

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaAlunoTabela(root)
    # Definir o tamanho da janela com base nas dimensões da tela
    root.geometry("800x600")  # Ajuste conforme necessário
    root.mainloop()
