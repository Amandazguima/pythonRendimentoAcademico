import tkinter as tk

from data.context.postgre_sql_context import Postgre_Sql_Context

class CadastroAluno:
    def __init__(self,win):
        #Componentes:
        self.lbId = tk.Label(win,text='id do Aluno')
        self.lblNome = tk.Label(win, text='Nome do Aluno')

        self.txtId = tk.Entry(bd=3)
        self.txtNome= tk.Entry()
        self.txtNomeDisciplina = tk.Entry()
        self.txtNota1 = tk.Entry()
        self.txtNota2 = tk.Entry()

        self.btnCadastrar = tk.Button(win,text='Cadastrar', command=self.functionCadastrarAluno)
        self.btnAtualizar = tk.Button(win,text='Atualizar', command=self.functionAtualizarBanco)
        self.btnExcluir = tk.Button(win,text='Excluir', command=self.functionExcluirAluno)
        self.btnLimpar = tk.Button(win,text='Limpar', command=self.functionLimparTela)

    def functionCadastrarAluno(self):
        try:
            id, nome, nomeDisciplina, nota1, nota2 = self.functionLerCampos()

            self.inserirDados(id, nome, nomeDisciplina, nota1, nota2)

            self.functionLimparTela()
            print('Aluno Cadastrado com Sucesso')

        except Exception as e:
            print('Não foi possivel realizar o cadastro.', e)

    def functionLimparTela(self):
        try:
            self.txtId.delete(0,tk.END)
            self.txtNome.delete(0,tk.END)
            print('Os campos foram limpos')
        except Exception as e:
            print('Não foi possivel limpar os campos.', e)

    def funtionLerCampos(self):
        try:
            id = self.txtId.get()
            nome = self.txtNome.get()
            print('Leitura dos dados com sucesso')
        except Exception as e: 
            print('Não foi possivel ler os dados.', e)
        
        return nome, id 
    
    def functionAtualizarBanco(self):
        try:
            id, nome, nomeDisciplina, nota1, nota2 = self.funtionLerCampos()

            query= "f * UPDATE public.alunos SET nome='{nome}', id = '{id}''"

            self.db_pg_context.conectar()

            self.db_pg_executar_update_sql(query)

            self.db_pg_context.descontectar()

            self.functionLimparTela()

        except Exception as e:
            print('Não foi possivel atualiza o cadastro do aluno', e)
        
    def functionExcluirAluno(self):
        try:
            id = self.txtId.get()

            query = "f* DELETE FROM public.alunos"
            
            self.db_pg_context.conectar()

            self.db_pg_executar_update_sql(query)

            self.db_pg_context.descontectar()

            self.functionLimparTela()

        except Exception as e:
            print('Não foi possivel deletar o aluno',e)