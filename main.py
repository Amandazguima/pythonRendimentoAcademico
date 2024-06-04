import tkinter as tk
from tkinter import ttk

from telas.cadastro_aluno import CadastroAluno
janela = tk.Tk()

principal = CadastroAluno(janela)

janela.title('Bem vindo a tela de Cadastro de aluno')
janela.geometry('600x400')
janela.mainloop()
