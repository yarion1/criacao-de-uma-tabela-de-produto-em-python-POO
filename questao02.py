from moduloq02 import *
from IPython.display import clear_output

opcao=0
while(opcao!=6):
    #clear_output(wait=True) 
    clear_output() #serve para limpar a tela
    print("-------Menu Principal---------")
    print("1-Incluir Nova Produto")
    print("2-Listar Todas os Produtos")
    print("3-Adicionar ao Estoque")
    print("4-Retirar do Estoque")
    print("5-Excluir Produto")
    print("6-Sair")
    opcao=int(input("Digitar a Opcao Desejada ==>"))
    
    new = produto()

    if(opcao == 1):
        new.NovoProduto()
    elif(opcao == 2):
        new.listaProdutos()
    elif(opcao == 3):
        new.AdcEstoque()
    elif(opcao == 4):
        new.RetiraEstoque()
    elif(opcao == 5):
        new.ExcluirProduto()
    elif(opcao == 6):
        new.Sair()