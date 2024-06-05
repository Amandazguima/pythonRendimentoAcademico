import tkinter as tk
from tkinter import ttk

from data.context.postgre_sql_context import Postgre_Sql_Context


class CadastroAlunoDisciplina(tk.Toplevel):
    def __init__(self, master=None):

        super().__init__(master)
        self.master = master
        self.title("Cadastro de Notas")
        self.geometry("600x400")

        #Componentes:
        self.lbId = tk.Label(self, text='id Aluno Disciplina')
        self.lblAluno = tk.Label(self, text='id do Aluno')
        self.lblDisciplina = tk.Label(self, text='id da Disciplina')
        self.lblnotaUm = tk.Label(self, text='Nota 1')
        self.lblnotaDois = tk.Label(self, text='Nota 2')
        self.lblMedia = tk.Label (self, text="")


        self.txtId = tk.Entry(self)
        self.txtIdAluno = tk.Entry(self)
        self.txtIdDisciplina = tk.Entry(self)
        self.txtnotaUm = tk.Entry(self)
        self.txtnotaDois = tk.Entry(self)

        self.btnCadastrar = tk.Button(self, text='Cadastrar', command=self.functionCadastrarNotas)
        self.btnAtualizar = tk.Button(self, text='Atualizar', command=self.functionAtualizarNotas)
        self.btnExcluir = tk.Button(self, text='Excluir', command=self.functionExcluirNotas)
        self.btnLimpar = tk.Button(self, text='Limpar', command=self.functionLimparTela)
        self.btnCalcular = tk.Button(self, text='Calcular Média', command=self.exibirRendimento)
        self.back_button = ttk.Button(self, text="Voltar para o cadastro de alunos", command=self.cadastroAluno)
        self.back_button.pack(pady=10)


        #Posicionamento dos componentes
        self.lbId.place(x=100, y=50)
        self.txtId.place(x=250, y=50)
        self.lblAluno.place(x=100, y=100)
        self.txtIdAluno.place(x=250, y=100)
        self.lblDisciplina.place(x=100, y=150)
        self.txtIdDisciplina.place(x=250, y=150)
        self.lblnotaUm.place(x=100, y=200)
        self.txtnotaUm.place(x=250, y=200)
        self.lblnotaDois.place(x=100, y=250)
        self.txtnotaDois.place(x=250, y=250)
        self.btnCadastrar.place(x=100, y=350)
        self.btnAtualizar.place(x=200, y=350)
        self.btnLimpar.place(x=300, y=350)
        self.btnExcluir.place(x=400, y=350)
        self.btnCalcular.place(x=100, y=300)
        self.lblMedia.place(x=250, y=300)


        #Inicio e conexão com o banco de dados: 
        self.db_pg_context = Postgre_Sql_Context()



    def functionCadastrarNotas(self):
        try:
            id, aluno, disciplina, notaUm, notaDois, = self.functionLerCampos()

            self.inserirDados(id, aluno, disciplina, notaUm, notaDois)

            self.functionLimparTela()

            print('Notas Cadastrada com Sucesso')

            self.rendimentoEscolar()

        except Exception as e:
            print('Não foi possivel realizar o cadastro.', e)

    def functionLimparTela(self):
        try:
            self.txtId.delete(0, tk.END)

            self.txtIdAluno.delete(0, tk.END)

            self.txtIdDisciplina.delete(0, tk.END)

            self.txtnotaUm.delete(0, tk.END)

            self.txtnotaDois.delete(0, tk.END)

            self.lblMedia.config(text="")

            print('Os campos foram limpos')

        except Exception as e:
            print('Não foi possivel limpar os campos.', e)

    def functionLerCampos(self):
        try:
            id = int(self.txtId.get())

            aluno = int(self.txtIdAluno.get())

            disciplina = int(self.txtIdDisciplina.get())

            notaUm = float(self.txtnotaUm.get())

            notaDois = float(self.txtnotaDois.get())

            print('Leitura dos dados com sucesso')
        except Exception as e:
            print('Não foi possivel ler os dados.', e)
        return id, aluno, disciplina, notaUm, notaDois

    def inserirDados(self, id, aluno, disciplina, notaUm, notaDois):
        try:
            query = f"INSERT INTO public.alunodisciplina(id, aluno_id, disciplina_id, notaUm, notaDois) VALUES({id},{aluno},{disciplina}, {notaUm}, {notaDois});"

            self.db_pg_context.conectar()

            self.db_pg_context.executar_update_sql(query)

            self.db_pg_context.desconectar()

        except Exception as e:
            print("Não foi possível fazer o cadastro", e)

    def functionAtualizarNotas(self):
        try:
            id, aluno, disciplina, notaUm, notaDois = self.functionLerCampos()

            query = f"UPDATE public.alunodisciplina SET notaUm = {notaUm}, notaDois = {notaDois} WHERE aluno_id = {aluno} AND disciplina_id = {disciplina} ;"

            self.db_pg_context.conectar()

            self.db_pg_context.executar_update_sql(query)

            self.db_pg_context.desconectar()

            print('Notas atualizadas com sucesso')

        except Exception as e:
            print("Não foi possível atualizar as notas", e)

    def functionExcluirNotas(self):
        try:
            id = self.txtId.get()

            query = f"DELETE FROM public.alunodisciplina WHERE id ={id}"

            self.db_pg_context.conectar()

            self.db_pg_context.executar_update_sql(query)

            self.db_pg_context.desconectar()

            self.functionLimparTela()

            print("A disciplina foi deletada com sucesso")

        except Exception as e:
            print('Não foi possivel deletar a disciplina', e)

    def rendimentoEscolar(self):

        notaUm = float(self.txtnotaUm.get())
        notaDois = float(self.txtnotaDois.get())

        media = (notaUm + notaDois)/ 2

        if media < 6:
             return "Reprovado"
        else:
            return "Aprovado"

    def exibirRendimento(self):
        resultado = self.rendimentoEscolar()
        self.lblMedia.config(text=resultado)

    def cadastroAluno(self):
        self.destroy()
        self.master.deiconify()