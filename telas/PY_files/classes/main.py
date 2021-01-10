from .funcionarios import Funcionario
from .pessoa import Pessoa
from .estoque import Estoque
from .cliente import Cliente
import os

def escolhaFuncionario(idFuncionario, funcList):

    for i in funcList:
        if idFuncionario == i.id:
            return i  
    print("ID inexistente!")


def listFuncionarios(funcList):

    print("**************** LISTA FUNCIONARIOS *******************")
    for i in funcList:
        print(f"ID: {i.id} -- Nome: {i.pessoa.nome}")
    
    esc = int(input("Selecione um funcionário pelo ID: "))

    return esc

def cadPessoa():

    print("**************** CADASTRO DA PESSOA *******************")
    print("------------------------------------------------------------")
    nome = input("------------- NOME: ")
    cpf = input("------------- CPF: ")
    end = input("------------- ENDEREÇO: ")
    telefone = int(input("------------- TELEFONE: "))
    idade = int(input("------------- IDADE: "))
    email = input("------------- E-MAIL: ")

    p = Pessoa(nome,cpf,end,telefone,idade,email)

    return p

def venda(funcionario,estoque):
    funcionario.listarClientes()
    idclient = int(input("Selecione um cliente pelo ID: "))
    print('Estoque: ')
    estoque.listar()
    print('-------------')
    nomeProduto = input("Nome do produto a ser vendido: ")
    qtd = int(input("quantidade: "))
    funcionario.venderProduto(nomeProduto,qtd,estoque, idclient)

def cadProduto(funcionario,estoque):

    print("**************** CADASTRO DE PRODUTO *******************")
    print("------------------------------------------------------------")
    nome = input("------------- NOME: ")
    descricao = input("------------- DESCRIÇAO: ")
    preco = input("------------- PREÇO: ")
    qtd = int(input("------------- QUANTIDADE: "))

    funcionario.cadastroProduto(nome,descricao,preco,qtd,estoque)
    
def menuFuncionario():

    print("\n*********** MENU FUNCIONÁRIO ************")
    print("-----------------------------------------")
    print("------- 0 - VOLTAR ----------------------")
    print("------- 1 - CADASTRAR CLIENTE -----------")
    print("------- 2 - LISTAR CLIENTES -------------")
    print("------- 3 - CADASTRAR PRODUTO -----------")
    print("------- 4 - VENDER PRODUTO --------------")
    print("------- 5 - LISTAR PRODUTOS -------------")
    print("------- 6 - HISTORICO DO ESTOQUE --------")
    print("-----------------------------------------")
    print("*****************************************")
    
    esc = int(input("Escolha uma das opções: "))

    return esc

def menuPrincipal():

    print("\n**************** MENU *******************")
    print("-----------------------------------------")
    print("------- 0 - SAIR ------------------------")
    print("------- 1 - CADASTRAR FUNCIONÁRIO -------")
    print("------- 2 - ENTRAR ----------------------")
    print("-----------------------------------------")
    print("*****************************************")
    
    esc = int(input("Escolha uma das opções: "))

    return esc

def main():

    funcList = []
    estoque = Estoque()

    while(True):
        esc = menuPrincipal()

        if (esc == 1 ):
            os.system('clear'or 'cls')
            p1 = cadPessoa()
            f1 = Funcionario(p1)
            funcList.append(f1)

        elif (esc == 2):
            os.system('clear'or 'cls')
            if(len(funcList) == 0):
                print('Sem funcionários cadastrados!')
                _ = input()
            else:
                idF = listFuncionarios(funcList)
                FuncLogado = escolhaFuncionario(idF,funcList)
                while(True):
                    
                    escF = menuFuncionario()

                    if(escF == 1):
                        os.system('clear'or 'cls')
                        print('Cadastrando cliente: ')
                        p2 = cadPessoa()
                        c1 = Cliente(p2)
                        FuncLogado.cadastrarCliente(c1)
                    elif(escF == 2):
                        os.system('clear'or 'cls')
                        FuncLogado.listarClientes()
                    elif(escF == 3):
                        os.system('clear'or 'cls')
                        cadProduto(FuncLogado,estoque)
                    elif(escF == 4):
                        os.system('clear'or 'cls')
                        if( len(FuncLogado.listaClientes) > 0 and len(estoque.produtos) > 0):
                            venda(FuncLogado,estoque)
                        else:
                            print("Sem clientes ou produtos cadastrados no sistema")
                    elif(escF == 5):
                        os.system('clear'or 'cls')
                        print("Produtos cadastrados")
                        estoque.listar()
                    elif(escF == 6):
                        os.system('clear'or 'cls')
                        estoque.mostraHistorico()
                    else:
                        break

        else:
            break


if __name__ == "__main__":
    main()