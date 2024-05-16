import tkinter as tk

from telas.cadastro_aluno import CadastroAluno

janela = tk.Tk()

principal = CadastroAluno(janela)

janela.title('Bem vinto a tela de Cadastro de aluno')
janela.geometry('600x600')
janela.mainloop()