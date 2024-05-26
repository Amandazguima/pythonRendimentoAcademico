import tkinter as tk

from data.context.postgre_sql_context import Postgre_Sql_Context

class TelaPrincipal:
    def __init__(self, note):

        self.note = note

        #Componetes mude tudo com win para note
        self.lbNota1 = tk.Label(note, text='Primeiro Semestre')
        self.lblNota2 = tk.Label(note, text ='Segunda Semestre')
        self.lblNota3 = tk.Label(note, text='Terceiro Semestre ')

        self.txtNota1 = tk.Entry(bd=3)
        self.txtNota2 = tk.Entry()
        self.txtNota3 = tk.Entry()

        self.btnCadastrar = tk.Button(note, text='OK' , command=self.fCadastrarNota)
        self.btnAtualizar = tk.Button(note, text='Atualizar notas' , command=self.fAtualizarNota )
        self.btnExcluir = tk.Button(note, text='Excluir notas' , command=self.fExcluirNota) 
        self.btnLimpar = tk.Button(note, text='Limpar notas', command=self.fLimparNota)
        self.btnCalcular = tk.button(note, text='Calcular media', command=self.fMedia)

        self.btnListaDeNotas = tk.Button(note, text='Lista de Produtos',command=self.ListaProdutos)

            #Posição de elementos
            self.lbNota1.place (x=100, y=50)
            self.txtNota1.place (x=250, y=50)
            self.lblNota2.place (x=250 , y=100)
            self.txtNota2.place (x=350, y=100)
            self.lblNota3.place (x=100, y=150)
            self.txtNota3.place(x=250 , y=150)
	        self.btnCadastrar.place(x=100, y=200)
            self.btnAtualizar.place(x=200, y=200)
            self.btnExcluir.place(x=300, y=200)
            self.btnLimpar.place.(x=300, y=200)

            self.btnListaProdutos.place(x=100, y=300)
            self.db_pg_context= Postgre_Sql_Context()

        def fCadastrarNota(self):
                try:
                     codigo, nome, preço = self.LerCampos()

                     self.inserirDados(codigo, nome, preco)

                     self.flimparTela()
                     print('Produto Cadastro com Sucesso!')

                    except Exception as e:
                        print('Não foi possivel fazer o cadastro' e)

        def fAtualizarNota(self):
                try:
                      Nota1 , Nota2 , Nota3 = self.LerCampos()

                      query = f"Update public.produtos SET={Nota1}, codigo={Nota2}, preco={Nota3}"

                      self.db_pg_context.conectar()

                      self.db_pg_context.executar_query_sql()

                except Exception as e:
                      print('Não foi possivel atualizar  o cadastro'e)


        def inserirDados(self, Nota1 , Nota2 , Nota3):
                try:
                   query = f"INSERT INTO  public.produtos (nome,codigo, preco) VALUES( ' {Nota1}, {Nota2}, {Nota3}')"

                   self.db_pg-context.conectar()

                   self.db_pg-context.executar_updated_sql(query)

                   self.db_pg_context.desconectar()
                except Exception as e:
                     print('Não foi possivel fazer o cadastro.', e)

        def fLimparTela(self):
                try:
                    self.txtNota1.delete(first =0, tk.END)
                    self.txtNota2.delete(first0, tk.END)
                    self.txtNota3.delete(first0, tk.END)
                    print ('Campos Limpos! !)
                exception Exception as e:
                    print('Não foi possivel limpár os campos', e)

        def fLerCampos(self):
            try:
                Nota1 = self.txtNota1.get()
                Nota2 = self.txtNota2.get()
                Nota3 = self.txtNota3.get()

                print('Leitura dos Dados com Sucesso')
            except Exception as e:
                print ('Não foi possivel ler os dados', e)

            return codigo, nome, preco, id

        def fMedia(self, nota1 + nota2 + nota3):
            try:
          
            media = (nota1 + nota2 + nota3) / 3
            return media
            except Exception as e:
                print ('Erro sosu', e)

        def ListaNota(self)
             self.win.withdrawn()
             lista_de_nota = TelaSelecao(self.note)
             lista_de_nota.mainloop()
        