import tkinter as tk
from tkinter import ttk

from telas.cadastro_alunodisciplina import CadastroAlunoDisciplina
janela = tk.Tk()

principal = CadastroAlunoDisciplina(janela)

janela.title('Bem vindo a tela de Cadastro de aluno')
janela.geometry('600x400')
janela.mainloop()