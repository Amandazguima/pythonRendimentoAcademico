import tkinter as tk
from tkinter import ttk

from data.context.postgre_sql_context import Postgre_Sql_Context


class CadastroDisciplina(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Cadastro de Disciplina")
        self.geometry("500x300")
        self.transient(master)
        self.grab_set()

        #Componentes:
        self.lbId = tk.Label(master, text='id da Disciplina')
        self.lblNomeDaDisciplina = tk.Label(master, text='Nome da Disciplina')
        self.lblprofessor = tk.Label(master, text='Nome do Professor')

        self.txtId = tk.Entry(bd=3)
        self.txtNomeDisciplina = tk.Entry()
        self.txtprofessor = tk.Entry()

        self.btnCadastrar = tk.Button(master, text='Cadastrar', command=self.functionCadastrarDisciplina)
        self.btnAtualizar = tk.Button(master, text='Atualizar', command=self.functionAtualizarDisciplina)
        self.btnExcluir = tk.Button(master, text='Excluir', command=self.function_excluir)
        self.btnLimpar = tk.Button(master, text='Limpar', command=self.functionLimparTela)

        self.back_button = ttk.Button(master, text="Voltar para o cadastro de alunos", command=self.cadastroAluno)
        self.back_button.pack(pady=20)

        #Posicionamento dos componentes
        self.lbId.place(x=100, y=50)
        self.txtId.place(x=250, y=50)
        self.lblNomeDaDisciplina.place(x=100, y=100)
        self.txtNomeDisciplina.place(x=250, y=100)
        self.lblprofessor.place(x=100, y=150)
        self.txtprofessor.place(x=250, y=150)
        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnLimpar.place(x=300, y=200)
        self.btnExcluir.place(x=400, y=200)

        #Inicio e conexão com o banco de dados: 
        self.db_pg_context = Postgre_Sql_Context()

    def functionCadastrarDisciplina(self):
        try:
            id, nomeDisciplina, professor, = self.functionLerCampos()

            self.inserirDados(id, nomeDisciplina, professor)

            self.functionLimparTela()

            print('Disciplina Cadastrada com Sucesso')

        except Exception as e:
            print('Não foi possivel realizar o cadastro.', e)

    def functionLimparTela(self):
        try:
            self.txtId.delete(0, tk.END)

            self.txtNomeDisciplina.delete(0, tk.END)

            self.txtprofessor.delete(0, tk.END)

            print('Os campos foram limpos')

        except Exception as e:
            print('Não foi possivel limpar os campos.', e)

    def functionLerCampos(self):
        try:
            id = int(self.txtId.get())

            nomeDisciplina = self.txtNomeDisciplina.get()

            professor = self.txtprofessor.get()

            print('Leitura dos dados com sucesso')
        except Exception as e:
            print('Não foi possivel ler os dados.', e)

        return id, nomeDisciplina, professor

    def inserirDados(self, id, nomeDisciplina, professor):
        try:
            query = f"INSERT INTO public.disciplinas (id, nomeDisciplina, professor) VALUES({id},'{nomeDisciplina}', '{professor}')"

            self.db_pg_context.conectar()

            self.db_pg_context.executar_update_sql(query)

            self.db_pg_context.desconectar()

        except Exception as e:
            print("Não foi possível fazer o cadastro", e)

    def functionAtualizarDisciplina(self):
        try:
            id, nomeDisciplina, professor = self.functionLerCampos()

            query = f"UPDATE public.disciplinas SET nomedisciplina = '{nomeDisciplina}', professor = '{professor}' WHERE id= {id}"

            self.db_pg_context.conectar()

            self.db_pg_context.executar_update_sql(query)

            self.db_pg_context.desconectar()

            self.functionLimparTela()

        except Exception as e:
            print('Não foi possivel atualiza o cadastro da disciplina', e)

    def function_excluir(self):
        try:
            id = self.txtId.get()

            query = f"DELETE FROM public.disciplinas WHERE id ={id}"

            self.db_pg_context.conectar()

            self.db_pg_context.executar_update_sql(query)

            self.db_pg_context.desconectar()

            self.functionLimparTela()

            print("A disciplina foi deletada com sucesso")

        except Exception as e:
            print('Não foi possivel deletar a disciplina', e)

    def cadastroAluno(self):
        self.destroy()
        self.master.deiconify()
