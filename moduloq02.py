import psycopg2

#Conexão com o banco
host = "127.0.0.1"
dbname = "Company"
user = "postgres"
password = "9103"

conn_string = "host={0} user ={1} dbname={2} password={3}".format(host, user, dbname, password)

conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

#Classe 

class produto:
    descricao = ''
    quantidade = 0

    def __init__(self, descricao = None, quantidade = None):
        self.descricao = descricao
        self.quantidade = quantidade
    
    #get e set
    def Getdescricao(self):
        return self.descricao
    def Setdescricao(self, nova):
        self.descricao = nova
    
    def Getquant(self):
        return self.quantidade
    def Setquant(self, nova):
        self.quantidade = nova
    
    def NovoProduto(self):
        #Dados do novo Produto
        self.descricao = input("Insira o nome do novo produto:\n")
        self.quantidade = int(input("Insira a quantida disponível em estoque do produto:\n"))

        #Inserção no banco de dados
        cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", (self.descricao, self.quantidade))
        conn.commit()
        print("Produto Inserido com sucesso!\n")
    
    def listaProdutos(self):
        #Busca no banco de dados
        __dados = []
        cursor.execute("SELECT * FROM inventory;")
        
        __dados = cursor.fetchall()

        #Impressão da busca
        for dado in __dados:
            print("------------------------")
            print("Produto:")
            print("Nome:", str(dado[1]))
            print("Quantidade:", str(dado[2]))
            print("-----------------------")
        conn.commit()
    
    def AdcEstoque(self):
        #dados do produto a ser atualizado
        self.descricao = input("insira o nome do produto: ")    
        self.quantidade = int(input("insira a quantia a ser adicionada em estoque: "))

        #Busca para verificar se produtor existe
        selecQuery = "SELECT quantity FROM inventory WHERE name = %s"
        cursor.execute(selecQuery, (self.descricao,))
        __aux = cursor.fetchall()
        
        #Incrementando estoque
        for a in __aux:
            __x = a[0]
        self.quantidade = self.quantidade + __x

        #Adicionando no estoque
        if(__aux):
            cursor.execute("UPDATE inventory SET quantity = %s WHERE name = %s;", (self.quantidade, self.descricao))
            conn.commit()
            print("Estoque Atualizado\n")
        else:
            print("Produto Inexistente\n")
    
    def RetiraEstoque(self):
        #dados do produto a ser retirado
        self.descricao = input("insira o nome do produto: ")    
        self.quantidade = int(input("insira a quantia que deseja retirar: "))

        selecQuery = "SELECT quantity FROM inventory WHERE name = %s"
        cursor.execute(selecQuery, (self.descricao,))
        __aux = cursor.fetchall()
         

        if(__aux):
            #Retirando do estoque se possível 
            for a in __aux:
                __x = a[0]
            nova = __x - self.quantidade
            if(nova >= 0):
                cursor.execute("UPDATE inventory SET quantity = %s WHERE name = %s", (nova, self.descricao))
                conn.commit()
                print("Retira do com sucesso.\n")
            else:
                print("Quantidade desejada de retirada excede a quantidade em estoque, verifique o estoque e tente novamente\n")
        else:
            print("Produto Inexistente\n")
        #if(aux):
    
    def ExcluirProduto(self):
        #dado do produtor a ser excluido
        self.descricao = input("Insira o Produto que deseja excluir:")

        #verificando se o produto existe
        selecQuery = "SELECT id FROM inventory WHERE name = %s"
        cursor.execute(selecQuery, (self.descricao,))
        __aux = cursor.fetchall()

        if(__aux):
            cursor.execute("DELETE FROM inventory WHERE name = %s", (self.descricao,))
            conn.commit()
            print("Produto Excluido\n")
        else:
            print("O Produto já não existe em estoque.\n")

    def Sair(self):
        #fecha conexão
        cursor.close()
        conn.close()


    

