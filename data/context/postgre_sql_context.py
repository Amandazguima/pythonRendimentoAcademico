import psycopg2

class Postgre_Sql_Context:

    parametros_conexao = None
    conexao = None
    cursor = None

    def __init__(self):
        #Parâmetros de conexão
        self.parametros_conexao = {
            'host':"127.0.0.1",
            'port':"5432",
            'database':"pythonRendimentoAcademico",
            'user':"postgres",
            'password':"1234567"
        }

    def conectar(self):
        try:
            self.conexao = psycopg2.connect(
                host = self.parametros_conexao.get('host'),
                port = self.parametros_conexao.get('port'),
                database = self.parametros_conexao.get('database'),
                user = self.parametros_conexao.get('user'),
                password = self.parametros_conexao.get('password'),
            )
        except Exception as e:
            print("Não foi possivel se conectar ao banco de dados")
            print("Erro ->", e)
    
    #Método responsável por fechar a conexão com o banco de dados.
    def desconectar(self):
        if self.conectar is not None:
            self.conexao.close()

    #Método de executar querys no banco de dados
    def executar_query_sql(self,query):
        #Obtém o ponteiro do banco de dados
        self.cursor = self.conexao.cursor()

        #Ecuta a query no banco de dados
        self.cursor.execute(query)

        rows = self.cursor.fetchall()

        #Fecha a executação do ponteiro do banco de dados
        self.cursor.close()

        return rows
    
    def executar_update_sql(self,query):

        #Obtém o ponteiro do banco de dados
        self.cursor = self.conexao.cursor()

        #Executar a query no banco de dados
        self.cursor.execute(query)

        #Confirma para o banco de dados a alteração dos dados:
        self.conexao.commit()

        #Fecha a excusão do ponteiro do banco de dados
        self.cursor.close()