import tkinter as tk
from tkcalendar import Calendar
from modelo.professor import Professor
from repositorio.professorRepositorio import ProfessorRepositorio
from repositorio.disciplinaRepositorio import DisciplinaRepositorio
import suporte.Utilidades as Utilidades

class TelaProfessorEditar:
    def __init__(self, root, matricula):
        self.root = root
        self.root.title("Editar Professor")
        self.root.geometry("600x400")  # Largura x Altura
        
        self.matricula_professor = matricula

        self.criar_campos()
        self.criar_botoes()

    def criar_campos(self):
        professor = ProfessorRepositorio.Busca_Professor_Matricula(matricula=self.matricula_professor)
        professor.BuscarDisciplinas()
        
        self.label_titulo = tk.Label(self.root, text="Editar Professor", font=("Helvetica", 16))
        
        self.label_matricula = tk.Label(self.root, text="Matrícula:", font=("Arial", 14))
        self.label_matricula2 = tk.Label(self.root,text=professor.GetMatricula(), font=("Arial", 14))

        self.label_nome = tk.Label(self.root, text="Nome:", font=("Arial", 14))
        self.entry_nome = tk.Entry(self.root, font=("Arial", 14))
        self.entry_nome.insert(0, professor.GetNome())

        # Campo de data com calendário
        self.label_data_nascimento = tk.Label(self.root, text="Data de Nascimento:", font=("Arial", 14))
        self.calendario = Calendar(self.root, selectmode="day", date_pattern="yyyy-mm-dd", font=("Arial", 14))
        self.calendario.selection_set(professor.GetData())


        # Campo para adicionar disciplinas
        self.label_cod_disciplinas_matriculadas = tk.Label(self.root, text="Cód. Disciplinas Matriculadas:", font=("Arial", 14))
        self.entry_cod_disciplinas_matriculadas = tk.Entry(self.root, font=("Arial", 14))
        self.entry_cod_disciplinas_matriculadas.insert(0, Utilidades.juntar_os_cod_discilinas(professor.GetDisciplinas()))

        # Posicionando os widgets na janela

        self.label_titulo.grid(row=0, column=0, pady=10)

        self.label_nome.grid(row=1, column=0, padx=10, pady=10)
        self.entry_nome.grid(row=1, column=1, padx=10, pady=10)
        
        self.label_matricula.grid(row=2, column=0, padx=10, pady=10)
        self.label_matricula2.grid(row=2, column=1, padx=10, pady=10)
        
        self.label_data_nascimento.grid(row=3, column=0, padx=10, pady=10)
        self.calendario.grid(row=3, column=1, padx=10, pady=10)

        self.label_cod_disciplinas_matriculadas.grid(row=4, column=0, padx=10, pady=10)
        self.entry_cod_disciplinas_matriculadas.grid(row=4, column=1, padx=10, pady=10, columnspan=2, sticky="w")

    def criar_botoes(self):
        self.btn_adicionar = tk.Button(self.root, text="Editar", font=("Arial", 14), command=self.editar_professor)
        self.btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 14), command=self.tela_voltar)

        # Posicionando os botões lado a lado
        self.btn_adicionar.grid(row=5, column=0, padx=10, pady=10)
        self.btn_voltar.grid(row=5, column=1, padx=10, pady=10)

    def editar_professor(self):
        if not self.confirma_campos_obrigatorio():
            return
        matricula = self.matricula_professor
        nome = self.entry_nome.get()
        data_nascimento = self.calendario.get_date()  # Obtém a data selecionada
        codigosNaoValidados = self.entry_cod_disciplinas_matriculadas.get()

        professor = Professor(matricula=matricula, nome=nome, data=data_nascimento)
        ProfessorRepositorio.Edita_Professor(professor=professor)

        codigos = Utilidades.formata_codigos(codigosNaoValidados)
        professor.atualisar_disciplinas(codigos_disciplinas=codigos)

        self.tela_voltar()
     
    def tela_voltar(self):
        from telas.telas_professor.telaProfessorTabela import TelaProfessorTabela
        Utilidades.mudar_de_tela(self.root, TelaProfessorTabela)

    def iniciar_aplicacao(self):
        self.root.mainloop()
        
    def confirma_campos_obrigatorio(self):
        camposObrigatorios = {
            self.entry_nome : "Nome",
        }
        if Utilidades.valida_campos_obrigatorios(campos=camposObrigatorios) and \
        Utilidades.valida_nome_pessoa(nome=self.entry_nome.get()):
            return True
        else:
            return False

if __name__ == "__main__":
    app = TelaProfessorEditar()
    app.iniciar_aplicacao()