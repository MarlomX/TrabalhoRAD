import tkinter as tk
from tkcalendar import Calendar
from modelo.disciplina import Disciplina
from repositorio.disciplinaRepositorio import DisciplinaRepositorio
import suporte.Utilidades as Utilidades

class TelaDisciplinaAdicionar:
    def __init__(self, root):
        self.root = root
        self.root.title("Adicionar Disciplina")
        self.root.geometry("600x400")  # Largura x Altura

        self.criar_campos()
        self.criar_botoes()

    def criar_campos(self):
        
        self.label_titulo = tk.Label(self.root, text="Adicionar Disciplina", font=("Helvetica", 16))
        
        self.label_nome = tk.Label(self.root, text="Nome:", font=("Arial", 14))
        self.entry_nome = tk.Entry(self.root, font=("Arial", 14))
        
        self.label_codigo = tk.Label(self.root, text="Codigo:", font=("Arial", 14))
        self.entry_codigo = tk.Entry(self.root, font=("Arial", 14))

        # Posicionando os widgets na janela
        self.label_titulo.grid(row=0, column=0, pady=10)
        
        self.label_nome.grid(row=1, column=0, padx=10, pady=10)
        self.entry_nome.grid(row=1, column=1, padx=10, pady=10)
        
        self.label_codigo.grid(row=2, column=0, padx=10, pady=10)
        self.entry_codigo.grid(row=2, column=1, padx=10, pady=10)
        
    def criar_botoes(self):
        self.btn_adicionar = tk.Button(self.root, text="Adicionar", font=("Arial", 14), command=self.adicionar_disciplina)
        self.btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 14), command=self.tela_voltar)

        # Posicionando os botões lado a lado
        self.btn_adicionar.grid(row=4, column=0, padx=10, pady=10)
        self.btn_voltar.grid(row=4, column=1, padx=10, pady=10)

    def adicionar_disciplina(self):
        if not self.confirma_campos_obrigatorio():
            return
        codigo = self.entry_codigo.get()
        nome = self.entry_nome.get()
        
        disciplina = Disciplina(nome=nome, codigo=codigo)
        DisciplinaRepositorio.Adiciona_Disciplina(disciplina=disciplina)
        
        self.tela_voltar()
    
    def tela_voltar(self):
        from telas.telas_disciplina.telaDisciplinaTabela import TelaDisciplinaTabela
        Utilidades.mudar_de_tela(self.root, TelaDisciplinaTabela)


    def iniciar_aplicacao(self):
        self.root.mainloop()

    def confirma_campos_obrigatorio(self):
        camposObrigatorios = {
            self.entry_nome : "Nome",
            self.entry_codigo : "Codigo"
        }
        if Utilidades.valida_campos_obrigatorios(campos=camposObrigatorios) and \
        Utilidades.valida_nome_disciplina(nome=self.entry_nome.get()) and\
            Utilidades.valida_codigo_disciplina(self.entry_codigo.get()):
            return True
        else:
            return False
    
if __name__ == "__main__":
    app = TelaDisciplinaAdicionar()
    app.iniciar_aplicacao()
