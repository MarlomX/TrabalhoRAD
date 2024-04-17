import tkinter as tk
from modelo.disciplina import Disciplina
from repositorio.disciplinaRepositorio import DisciplinaRepositorio
import suporte.Utilidades as Utilidades

class TelaDisciplinaEditar:
    def __init__(self, root, codigo):
        self.root = root
        self.root.title("Editar Disciplina")
        self.root.geometry("600x400")  # Largura x Altura
        
        self.codigo_disciplina = codigo

        self.criar_campos()
        self.criar_botoes()

    def criar_campos(self):
        disciplina = DisciplinaRepositorio.Busca_Disciplina_Codigo(self.codigo_disciplina)
        
        self.label_titulo = tk.Label(self.root, text="Editar Disciplina", font=("Helvetica", 16))

        self.label_codigo = tk.Label(self.root, text="Codigo:", font=("Arial", 14))
        self.label_codigo2 = tk.Label(self.root,text=disciplina.GetCodigo(), font=("Arial", 14))

        self.label_nome = tk.Label(self.root, text="Nome:", font=("Arial", 14))
        self.entry_nome = tk.Entry(self.root, font=("Arial", 14))
        self.entry_nome.insert(0, disciplina.GetNome())
        
        # Posicionando os widgets na janela
        
        self.label_titulo.grid(row=0, column=0, pady=10)
        
        self.label_nome.grid(row=1, column=0, padx=10, pady=10)
        self.entry_nome.grid(row=1, column=1, padx=10, pady=10)
        
        self.label_codigo.grid(row=2, column=0, padx=10, pady=10)
        self.label_codigo2.grid(row=2, column=1, padx=10, pady=10)
        

    def criar_botoes(self):
        self.btn_Editar = tk.Button(self.root, text="Editar", font=("Arial", 14), command=self.editar_disciplina)
        self.btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 14), command=self.tela_voltar)

        # Posicionando os botões lado a lado
        self.btn_Editar.grid(row=4, column=0, padx=10, pady=10)
        self.btn_voltar.grid(row=4, column=1, padx=10, pady=10)

    def editar_disciplina(self):
        if not self.confirma_campos_obrigatorio():
            return
        codigo = self.codigo_disciplina
        nome = self.entry_nome.get()

        disciplina = Disciplina(codigo=codigo, nome=nome)
        DisciplinaRepositorio.Edita_Disciplina(disciplina=disciplina)

        self.tela_voltar()
        
    def tela_voltar(self):
        from telas.telas_disciplina.telaDisciplinaTabela import TelaDisciplinaTabela
        Utilidades.mudar_de_tela(self.root, TelaDisciplinaTabela)

    def iniciar_aplicacao(self):
        self.root.mainloop()
    
    def confirma_campos_obrigatorio(self):
        camposObrigatorios = {
            self.entry_nome : "Nome",
        }
        if Utilidades.valida_campos_obrigatorios(campos=camposObrigatorios) and \
        Utilidades.valida_nome_disciplina(nome=self.entry_nome.get()):
            return True
        else:
            return False

if __name__ == "__main__":
    app = TelaDisciplinaEditar()
    app.iniciar_aplicacao()