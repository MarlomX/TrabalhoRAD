from telaInicial import TelaInicial
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaInicial(root)
    # Definir o tamanho da janela com base nas dimensões da tela
    root.geometry("800x600")  # Ajuste conforme necessário
    root.mainloop()