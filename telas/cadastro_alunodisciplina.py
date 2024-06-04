import tkinter as tk
from tkinter import ttk

from data.context.postgre_sql_context import Postgre_Sql_Context


class CadastroAlunoDisciplina:
    def __init__(self, win):
        #Componentes:
        self.lbId = tk.Label(win, text='id Aluno Disciplina')
        self.lblAluno = tk.Label(win, text='id do Aluno')
        self.lblDisciplina = tk.Label(win, text='id da Disciplina')
        self.lblnotaUm = tk.Label(win, text='Nota 1')
        self.lblnotaDois = tk.Label(win, text='Nota 2')
        self.lblMedia = tk.Label (win, text="")


        self.txtId = tk.Entry(bd=3)
        self.txtIdAluno = tk.Entry()
        self.txtIdDisciplina = tk.Entry()
        self.txtnotaUm = tk.Entry()
        self.txtnotaDois = tk.Entry()

        self.btnCadastrar = tk.Button(win, text='Cadastrar', command=self.functionCadastrarNotas)
        self.btnAtualizar = tk.Button(win, text='Atualizar', command=self.functionAtualizarNotas)
        self.btnExcluir = tk.Button(win, text='Excluir', command=self.functionExcluirNotas)
        self.btnLimpar = tk.Button(win, text='Limpar', command=self.functionLimparTela)
        self.btnCalcular = tk.Button(win, text='Calcular Média', command=self.exibirRendimento)


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
       try:
            notaUm = float(self.txtnotaUm.get())
            notaDois = float(self.txtnotaDois.get())

            media = (notaUm + notaDois)/ 2

            if media < 6:
                return "Reprovado"
            else:
                return "Aprovado"
       except Exception as e:
            print('Erro: Insira valores numéricos válidos nas notas.', e)

    def exibirRendimento(self):
        resultado = self.rendimentoEscolar()
        self.lblMedia.config(text=resultado)