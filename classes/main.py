from funcionarios import Funcionario
from pessoa import Pessoa
from estoque import Estoque
import os

def escolhaFuncionario(idFuncionario, funcList):

    for i in funcList:
        if idFuncionario == i.id:
            return i  
    print("ID inexistente!")


def listFuncionarios(funcList):

    os.system('clear'or 'cls')

    print("**************** LISTA FUNCIONARIOS *******************")
    for i in funcList:
        print(f"ID: {i.id}-- Nome: {i.pessoa.nome}")
    
    esc = int(input("Selecione um funcionário pelo ID: "))

    return esc

def cadPessoa():
    
    os.system('clear'or 'cls')

    print("**************** CADASTRO DE FUNCIONARIO *******************")
    print("------------------------------------------------------------")
    nome = input("------------- NOME: ")
    cpf = input("------------- CPF: ")
    end = input("------------- ENDEREÇO: ")
    telefone = int(input("------------- TELEFONE: "))
    idade = int(input("------------- IDADE: "))
    email = input("------------- E-MAIL: ")

    p = Pessoa(nome,cpf,end,telefone,idade,email)

    return p
    
def menuFuncionario():

    os.system('clear'or 'cls')

    print("*********** MENU FUNCIONÁRIO ************")
    print("-----------------------------------------")
    print("------- 1 - CADASTRAR CLIENTE -----------")
    print("------- 2 - LISTAR CLIENTES -------------")
    print("------- 3 - CADASTRAR PRODUTO -----------")
    print("------- 4 - VENDER PRODUTO --------------")
    print("------- 5 - LISTAR PRODUTOS -------------")
    print("------- 0 - VOLTAR ----------------------")
    print("-----------------------------------------")
    print("*****************************************")
    
    esc = int(input("Escolha uma das opções: "))

    return esc

def menuPrincipal():

    os.system('clear'or 'cls')

    print("**************** MENU *******************")
    print("-----------------------------------------")
    print("------- 1 - CADASTRAR FUNCIONÁRIO -------")
    print("------- 2 - ENTRAR ----------------------")
    print("------- 3 - SAIR ------------------------")
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
            p1 = cadPessoa()
            f1 = Funcionario(p1)
            funcList.append(f1)
        elif (esc == 2):

            if(len(funcList) == 0):
                print('Sem funcionários cadastrados!')
                _ = input()
            else:
                idF = listFuncionarios(funcList)
                FuncLogado = escolhaFuncionario(idF,funcList)

                escF = menuFuncionario()

                if(escF == 1)

        elif (esc == 3):
            break
        else:
            main()

if __name__ == "__main__":
    main()