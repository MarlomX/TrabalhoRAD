import re
import tkinter as tk
from tkinter import messagebox

def mudar_de_tela(root, tela_a_mudar):
    root.destroy()
    # Criar a Janela 2
    root2 = tk.Tk()
    root2.attributes("-fullscreen", True)
    tela_a_mudar(root2)

def mudar_de_tela_com_dados(root, tela_a_mudar, dados):
    root.destroy()
    # Criar a Janela 2
    root2 = tk.Tk()
    root2.attributes("-fullscreen", True)
    tela_a_mudar(root2,dados)
    
def valida_campos_obrigatorios(campos):
    for campo, nome  in campos.items():
        if not campo.get():
            messagebox.showwarning(title="Campo obrigatorio não prenchido",
                                   message=f"O campo {nome} é o brigatorio")
            return False
    return True

def divide_os_cod_disciplinas(codigos):
        # Remove todos os espaços
        disciplinas_sem_espacos= codigos.replace(" ", "")

        # Divide o texto por ","
        lista_disciplinas = disciplinas_sem_espacos.split(",")

        return lista_disciplinas

def juntar_os_cod_discilinas(codigos):
        codigos_disciplinas = ""
        atual = 1
        for disciplina in codigos:
            codigos_disciplinas+=disciplina.GetCodigo()
            if atual < len(codigos):
                codigos_disciplinas+=","
            atual+=1
        return codigos_disciplinas

def formata_codigos(codigosAVerificar):
    from repositorio.disciplinaRepositorio import DisciplinaRepositorio   
    disciplinasPosiveis= DisciplinaRepositorio.Busca_Todas_Disciplinas()
    codigosValidos = []
    codigosVerificados = []
    codigoInvalido =False
    
    if codigosAVerificar and codigosAVerificar!= "Separe os códigos com \",\"":
        for disciplina in disciplinasPosiveis:
            codigosValidos.append(disciplina.GetCodigo())
            
        cod_separados = divide_os_cod_disciplinas(codigos=codigosAVerificar)
        
        for codigo in cod_separados:
            if codigo in codigosValidos:
                codigosVerificados.append(codigo)
            else:
                codigoInvalido = True
    if codigoInvalido:
        messagebox.showwarning(title="Codgio Invalido",
                                   message="Algum(s) codigo(s) de disciplina estava errado!!")
    return codigosVerificados

def valida_nome_pessoa(nome):
    nome = str(nome)
    valido = False
    if len(nome) > 50:
        messagebox.showwarning(title="Nome muito grande",
            message=f"O nome pode ter no maximo 50 caractheres")
    elif re.search(r'\d', nome):
        messagebox.showwarning(title="Numero no nome",
                        message=f"O nome não pode conter numeros")
    else: valido = True
    return valido

def valida_matricula(matricula, pessoa):
    strMatricula = str(matricula)
    valido = False
    if len(strMatricula) != 12:
        messagebox.showwarning(title="Tamanho da matricula Errado",
            message=f"A matricula deve conter 12 numeros")
    elif not re.match(r'^\d+$', matricula):
        messagebox.showwarning(title="Letras na Matricula",
                        message=f"A matricula não pode conter letras")
    else:
        match pessoa:
            case "Aluno":
                from repositorio.alunoRepositorio import AlunoRepositorio
                matriculas_existentes_aluno = AlunoRepositorio.Busca_Todas_Matriculas()
                
                if str(matricula) in matriculas_existentes_aluno:
                    messagebox.showwarning(title="Matricula já existe",
                        message=f"Já existe um aluno com essa matricula")
                else: valido = True
                
            case "Professor":
                from repositorio.professorRepositorio import ProfessorRepositorio
                matriculas_existentes_professor = ProfessorRepositorio.Busca_Todas_Matriculas()
                
                if str(matricula) in matriculas_existentes_professor:
                    messagebox.showwarning(title="Matricula já existe",
                        message=f"Já existe um professor com essa matricula")   
                else: valido = True  
    return valido 
        
def valida_nome_disciplina(nome):
    nome = str(nome)
    valido = False
    if len(nome) > 50:
        messagebox.showwarning(title="Nome muito grande",
            message=f"O nome pode ter no maximo 50 caractheres")
    elif re.search(r'\d', nome):
        messagebox.showwarning(title="Numero no nome",
                        message=f"O campo Nome não pode conter numeros")
    else: valido = True
    return valido

def valida_codigo_disciplina(codigo):
    from repositorio.disciplinaRepositorio import DisciplinaRepositorio
    codigos_existentes = DisciplinaRepositorio.Busca_Todao_Codigos()
    valido = False
    if len(codigo) != 10:
        messagebox.showwarning(title="Tamanho do codigo Errada",
            message=f"O Codigo tem que ter 10 caracteres")
    elif re.search(r'\d', codigo[:5]):
        messagebox.showwarning(title="Formatação do codigo Errada",
            message=f"Os primeiros 5 caracteres tem que ser letras")
    elif not re.match(r'^\d+$',  codigo[5:]):
        messagebox.showwarning(title="Formatação do codigo Errada",
            message=f"Os ultimos 5 caracteres tem que ser numeros")
    elif codigo in codigos_existentes:
        messagebox.showwarning(title="Codigo já existe",
            message=f"Já existe uma disciplina com esse codigo")
    else: valido = True
    return valido