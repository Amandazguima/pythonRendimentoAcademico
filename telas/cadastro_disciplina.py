import tkinter as tk

from data.context.postgre_sql_context import Postgre_Sql_Context

class CadastroDisciplina:
    def __init__(self,win):
        #Componentes:
        self.lbId = tk.Label(win,text='id da Disciplina')
        self.lblNomeProfessor = tk.Label(win, text='Nome do Professor')
        self.lblNomeDaDisciplina = tk.Label(win, text='Nome da Disciplina')
  

        self.txtId = tk.Entry(bd=3)
        self.txtNomeProfessor= tk.Entry()
        self.txtNomeDisciplina = tk.Entry()
        self.txtNota1 = tk.Entry()
        self.txtNota2 = tk.Entry()

        self.btnCadastrar = tk.Button(win,text='Cadastrar', command=self.functionCadastrarDisciplina)
        self.btnAtualizar = tk.Button(win,text='Atualizar', command=self.functionAtualizarDisciplina)
        self.btnExcluir = tk.Button(win,text='Excluir', command=self.functionExcluirDisciplina)
        self.btnLimpar = tk.Button(win,text='Limpar', command=self.functionLimparTela)

    #Inicio e conexão com o banco de dados: 
    self.db_pg_context = Postgre_Sql_Context()

    def functionCadastrarDisciplina(self):
        try:
            id, nomeProfessor, nomeDisciplina, nota1, nota2 = self.functionLerCampos()

            self.inserirDados(id, nomeProfessor, nomeDisciplina, nota1, nota2)

            self.functionLimparTela()
            print('Aluno Cadastrado com Sucesso')

        except Exception as e:
            print('Não foi possivel realizar o cadastro.', e)

    def functionLimparTela(self):
        try:
            self.txtId.delete(0,tk.END)
            self.txtNomeProfessor.delete(0,tk.END)
            self.txtNomeDisciplina(0,tk.END)
            print('Os campos foram limpos')
        except Exception as e:
            print('Não foi possivel limpar os campos.', e)

    def funtionLerCampos(self):
        try:
            id = self.txtId.get()
            nomeProfessor = self.txtNomeProfessor.get()
            nomeDisciplica = self.txtNomeDisciplina.get()

            print('Leitura dos dados com sucesso')
        except Exception as e: 
            print('Não foi possivel ler os dados.', e)
        
        return nomeProfessor , nomeDisciplica, 
    
    def functionAtualizarDisciplina(self):
        try:
            id, nomeProfessor, nomeDisciplina = self.funtionLerCampos()

            query= f"* UPDATE public.disciplinas SET nome='{nomeProfessor}', id = '{id}', nomeDisciplina= '{nomeDisciplina}'"

            self.db_pg_context.conectar()

            self.db_pg_executar_update_sql(query)

            self.db_pg_context.descontectar()

            self.functionLimparTela()

        except Exception as e:
            print('Não foi possivel atualiza o cadastro do aluno', e)
        
    def functionExcluirDisciplina(self):
        try:
            id = self.txtId.get()

            query = f"DELETE FROM public.disciplina WHERE id ='{int(id)}'"
            
            self.db_pg_context.conectar()

            self.db_pg_executar_update_sql(query)

            self.db_pg_context.descontectar()

            self.functionLimparTela()

        except Exception as e:
            print('Não foi possivel deletar a disciplina',e)