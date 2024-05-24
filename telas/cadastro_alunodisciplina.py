import tkinter as tk
from tkinter import ttk

from data.context.postgre_sql_context import Postgre_Sql_Context

class CadastroAlunoDisciplina:
    def __init__(self,win):
        #Componentes:
        self.lbId = tk.Label(win,text='id Aluno Disciplina')
        self.lblnotaUm = tk.Label(win, text='Nota 1')
        self.lblnotaDois = tk.Label(win, text='Nota 2')
        self.lblAluno = tk.Label(win, text='Nome do Aluno')
        self.lblDisciplina = tk.Label(win, text='Nome da Disciplina')

        #Combobox alunos e disciplinas
        self.aluno_var = tk.StringVar(win)
        self.combobox_alunos = ttk.Combobox(win, textvariable=self.aluno_var)
        self.disciplina_var = tk.StringVar(win)
        self.combobox_disciplinas = ttk.Combobox(win, textvariable=self.disciplina_var)

        self.txtId = tk.Entry(bd=3)
        self.txtnotaUm = tk.Entry()
        self.txtnotaDois= tk.Entry()

        
        self.btnCadastrar = tk.Button(win,text='Cadastrar', command=self.functionCadastrarNotas)
        self.btnAtualizar = tk.Button(win,text='Atualizar', command=self.functionAtualizarNotas)
        self.btnExcluir = tk.Button(win,text='Excluir', command=self.functionExcluirNotas)
        self.btnLimpar = tk.Button(win,text='Limpar', command=self.functionLimparTela)
        
        
        #Posicionamento dos componentes
        self.lbId.place(x=100, y=50)
        self.txtId.place(x=250, y=50)
        self.lblAluno.place(x=100, y=100)
        self.combobox_alunos.place(x=250, y=100)
        self.lblDisciplina.place(x=100, y=150)
        self.combobox_disciplinas.place(x=250, y=150)
        self.lblnotaUm.place(x=100, y=200)
        self.txtnotaUm.place(x=250, y=200)
        self.lblnotaDois.place(x=100, y=250)
        self.txtnotaDois.place(x=250, y=250)
        self.btnCadastrar.place(x=100, y=300)
        self.btnAtualizar.place(x=200, y=300)
        self.btnLimpar.place(x=300, y=300)
        self.btnExcluir.place(x=400, y=300)
        
        
        
        #Inicio e conexão com o banco de dados: 
        self.db_pg_context = Postgre_Sql_Context()

    def functionCadastrarNotas(self):
        try:
            id, notaUm, notaDois, = self.functionLerCampos()

            self.inserirDados(id, notaUm, notaDois)

            self.functionLimparTela()
            
            print('Disciplina Cadastrada com Sucesso')

        except Exception as e:
            print('Não foi possivel realizar o cadastro.', e)

    def functionLimparTela(self):
        try:
            self.txtId.delete(0,tk.END)

            self.combobox_alunos.current(0)

            self.combobox_disciplinas.current(0)       
            
            self.txtnotaUm.delete(0,tk.END)
            
            self.txtnotaDois.delete(0,tk.END)     

            print('Os campos foram limpos')

        except Exception as e:
            print('Não foi possivel limpar os campos.', e)

    def functionLerCampos(self):
        try:
            id = int(self.txtId.get())

            aluno = self.combobox_aluno.get().split(" - ")[0]

            disciplina = self.combobox_disciplina.get().split(" - ")[0]

            notaUm = float(self.txtnotaUm.get())

            notaDois = float(self.txtnotaDois.get())

            print('Leitura dos dados com sucesso')
        except Exception as e: 
            print('Não foi possivel ler os dados.', e)
        return id, aluno, disciplina, notaUm, notaDois

    def inserirDados(self, aluno, disciplina, notaUm, notaDois):
        try:
            query = f"INSERT INTO public.alunodisciplina(aluno_id, disciplina_id, notaUm, notaDois) VALUES({aluno}, {disciplina}, {notaUm}, {notaDois} );"
           
            self.db_pg_context.conectar()

            self.db_pg_context.executar_update_sql(query)

            self.db_pg_context.desconectar()

        except Exception as e:
            print("Não foi possível fazer o cadastro", e)

    def functionAtualizarNotas(self):  
        try:
            id, nomeDisciplina, professor = self.functionLerCampos()

            query= f"UPDATE public.disciplinas SET nomedisciplina = '{nomeDisciplina}', professor = '{professor}' WHERE id = {id}"

            self.db_pg_context.conectar()

            self.db_pg_context.executar_update_sql(query)

            self.db_pg_context.desconectar()

            self.functionLimparTela()

        except Exception as e:
            print('Não foi possivel atualiza o cadastro da disciplina', e)
        
    def functionExcluirNotas(self):
        try:
            id = self.txtId.get()

            query = f"DELETE FROM public.disciplinas WHERE id ={id}"
            
            self.db_pg_context.conectar()

            self.db_pg_context.executar_update_sql(query)

            self.db_pg_context.desconectar()

            self.functionLimparTela()

            print("A disciplina foi deletada com sucesso")

        except Exception as e:
            print('Não foi possivel deletar a disciplina',e)
    
    def buscar_alunos(self):
        try:
            self.db_pg_context.conectar()
           
            query = "SELECT nome FROM alunos"
            
            resultado = self.db_pg_context.executar_update_sql(query)
            
            self.db_pg_context.desconectar()
            
            self.functionLimparTela()
        except Exception as e:
            print('Não foi possivel achar o aluno',e)
        return [linha[0] for linha in resultado]
    
    def buscar_disciplinas(self):
        try:
            self.db_pg_context.conectar()
            
            resultado = query = "SELECT nomedisciplina FROM disciplinas"
            
            self.db_pg_context.executar_update_sql(query)
            
            self.db_pg_context.desconectar()
            
            self.functionLimparTela()
        except Exception as e:
            print('Não foi possivel achar a disciplina',e)
        return [linha[0] for linha in resultado]
    
    def carregar_alunos(self):
        try:
            alunos = self.buscar_alunos()

            print("Alunos carregados:", alunos)

            self.combobox_alunos['values'] = [f"{aluno[0]} - {aluno[1]}" for aluno in alunos]
        except Exception as e:
            print('Não foi possível carregar os alunos.', e)

    def carregar_disciplinas(self):
        try:
            disciplinas = self.buscar_disciplinas()
            
            self.combobox_disciplinas['values'] = [f"{disciplina[0]} - {disciplina[1]}" for disciplina in disciplinas]
        except Exception as e:
            print('Não foi possível carregar as disciplinas.', e)