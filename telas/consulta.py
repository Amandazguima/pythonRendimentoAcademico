import tkinter as tk
from tkinter import ttk

from data.context.postgre_sql_context import Postgre_Sql_Context
class Consulta(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Consultar Rendimento Academico")
        self.geometry("600x400")

        self.label =ttk.Label(self, text="Consultar Rendimento Academico")
        self.label.place(x=20, y=40)

        self.back_button = ttk.Button(self, text="Voltar para a Tela Principal", command= self.cadastroAluno)
        self.back_button.pack(pady= 20)

        self.dados =[]

        self.tree = ttk.Treeview(self, columns=("ID","Nome do Aluno","Nome Disciplina","Nota 1", "Nota 2"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome do Aluno", text="Nome do Aluno")
        self.tree.heading("Nome Disciplina", text="Nome Disciplina")
        self.tree.heading("Nota 1", text="Nota 1")
        self.tree.heading("Nota 2", text="Nota 2")

        self.tree.column("ID", width=50)
        self.tree.column("Nome do Aluno", width=100)
        self.tree.column("Nome Disciplina", width=100)
        self.tree.column("Nota 1", width=50)
        self.tree.column("Nota 2", width=50)

        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.tree.place(x=20, y=80, width=560, height=300)
        self.scrollbar.place(x=580, y=80, height=300)

        self.db_pg_context= Postgre_Sql_Context()

        self.obterDados()

    def obterDados(self):
        try:
            query = "SELECT  a.nome AS nome, d.nomedisciplina AS NomeDisciplina, ad.notaum AS NotaUm, ad.notadois AS NotaDois, ad.id AS id FROM alunos a JOIN alunodisciplina ad ON a.id = ad.aluno_id JOIN disciplinas d ON ad.disciplina_id = d.id;"
            self.db_pg_context.conectar()
            result = self.db_pg_context.executar_query_sql(query)
            self.db_pg_context.desconectar()

            print("Resultado da consulta:")
            for row in result:
                print(row)

            self.dados = [{"id": row[4], "nome": row[0], "nomedisciplina": row[1],"notaum": row[2], "notadois": row[3]} for row in result]
            self.inserirDadosTabela()

        except Exception as e:
            print("Não foi possível obter os dados:", e)

    def inserirDadosTabela(self):
        try:
            for aluno in self.dados:
                print(aluno)  # Debugging
                self.tree.insert("", "end", values=(aluno["id"], aluno["nome"], aluno["nomedisciplina"], aluno["notaum"], aluno["notadois"]))

        except Exception as e:
            print(e)

    def cadastroAluno(self):
        self.destroy()
        self.master.deiconify()
