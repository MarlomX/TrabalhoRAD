import tkinter as tk
from suporte import Utilidades

class TelaInicial:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("600x600")#seve para dimenciona e redimenciona a tela
        self.root.title("Main Page") 

        #Cabechalho
        cabecalho = tk.Label(root, text="Escolha uma tabela", font=("Arial", 16))
        cabecalho.pack(pady=20)  # Espaçamento entre o cabeçalho e o restante da interface
        
            
        #Criar os botões
        tabela_aluno_button = tk.Button(root, text="Tabela Aluno", command=self.tela_tabela_aluno)
        tabela_professor_button = tk.Button(root, text="Tabela Professor", command=self.tela_tabela_professor)
        tabela_disciplina_button = tk.Button(root, text="Tabela Disciplina", command=self.tela_tabela_disciplina)
        sair_button = tk.Button(root, text="Sair", command=self.sair)

        # Ajusta o tamanho dos botões
        tabela_aluno_button.config(width=25, height=5)  # Largura em caracteres
        tabela_professor_button.config(width=25, height=5)
        tabela_disciplina_button.config(width=25, height=5)
        sair_button.config(width=25, height=5)


        tabela_aluno_button.pack(side="top", padx=10)
        tabela_professor_button.pack(side="top", padx=10)
        tabela_disciplina_button.pack(side="top", padx=10)
        sair_button.pack(side="top", padx=10)
    
    def tela_tabela_aluno(self):
        from telas.telas_aluno.telaAlunoTabela import TelaAlunoTabela
        Utilidades.mudar_de_tela(root=self.root, tela_a_mudar=TelaAlunoTabela)
    
    def tela_tabela_professor(self):
        from telas.telas_professor.telaProfessorTabela import TelaProfessorTabela
        Utilidades.mudar_de_tela(root=self.root, tela_a_mudar=TelaProfessorTabela)
    
    def tela_tabela_disciplina(self):
        from telas.telas_disciplina.telaDisciplinaTabela import TelaDisciplinaTabela
        Utilidades.mudar_de_tela(root=self.root, tela_a_mudar=TelaDisciplinaTabela)
    
    def sair(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaInicial(root)
    # Definir o tamanho da janela com base nas dimensões da tela
    root.geometry("800x600")  # Ajuste conforme necessário
    root.mainloop()