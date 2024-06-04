import tkinter as tk
from data.context.postgre_sql_context import Postgre_Sql_Context
from telas.cadastro_disciplina import CadastroDisciplina


class CadastroAluno:
    def __init__(self, win):

        self.win = win

        #Componentes:
        self.lbId = tk.Label(win,text='id do Aluno')
        self.lblNome = tk.Label(win, text='Nome do Aluno')

        self.txtId = tk.Entry(bd=3)
        self.txtNome= tk.Entry()

        self.btnCadastrar = tk.Button(win,text='Cadastrar', command=self.functionCadastrarAluno)
        self.btnAtualizar = tk.Button(win,text='Atualizar', command=self.functionAtualizarBanco)
        self.btnExcluir = tk.Button(win,text='Excluir', command=self.functionExcluirAluno)
        self.btnLimpar = tk.Button(win,text='Limpar', command=self.functionLimparTela)
        self.btnDisciplina = tk.Button(win, text="Cadastrar Disciplina", command= self.proximaPagina)
        self.btnDisciplina.pack()

        #Posicionamento dos componentes
        self.lbId.place(x=100, y=50)
        self.txtId.place(x=250, y=50)
        self.lblNome.place(x=100, y=100)
        self.txtNome.place(x=250, y=100)
        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnLimpar.place(x=300, y=200)
        self.btnExcluir.place(x=400, y=200)
        self.btnDisciplina.place(x=100, y=250)

        #Inicio e conexão com o banco de dados: 
        self.db_pg_context = Postgre_Sql_Context()

    def functionCadastrarAluno(self):
        try:
            id, nome = self.functionLerCampos()

            self.inserirDados(id, nome)

            self.functionLimparTela()

            print('Aluno Cadastrado com Sucesso')

        except Exception as e:
            print('Não foi possivel realizar o cadastro.', e)

    def inserirDados(self, id, nome):
        try:
            query = f"INSERT INTO public.alunos(id, nome) VALUES({id}, '{nome}')"
           
            self.db_pg_context.conectar()

            self.db_pg_context.executar_update_sql(query)

            self.db_pg_context.desconectar()

        except Exception as e:
            print("Não foi possível fazer o cadastro", e)


    def functionLimparTela(self):
        try:
            self.txtId.delete(0, tk.END)

            self.txtNome.delete(0, tk.END)

            print('Os campos foram limpos')
        except Exception as e:
            print('Não foi possivel limpar os campos.', e)

    def functionLerCampos(self):
        try:
            id = self.txtId.get()

            nome = self.txtNome.get()

            print('Leitura dos dados com sucesso')
        except Exception as e: 
            print('Não foi possivel ler os dados.', e)
        
        return id, nome
    
    def functionAtualizarBanco(self):
        try:
            id, nome = self.functionLerCampos()

            query = f"UPDATE public.alunos SET nome='{nome}' WHERE id = {id}"

            self.db_pg_context.conectar()

            self.db_pg_context.executar_update_sql(query)

            self.db_pg_context.desconectar()

            self.functionLimparTela()

        except Exception as e:
            print('Não foi possivel atualiza o cadastro do aluno', e)
        
    def functionExcluirAluno(self):
        try:
            id = self.txtId.get()

            query = f"DELETE FROM public.alunos WHERE id={id}"
            
            self.db_pg_context.conectar()

            self.db_pg_context.executar_update_sql(query)

            self.db_pg_context.desconectar()

            self.functionLimparTela()

        except Exception as e:
            print('Não foi possivel deletar o aluno',e)

    def proximaPagina(self):
        self.win.withdraw()
        cadastro_disciplina = CadastroDisciplina(self.win)
        self.win.mainloop()

