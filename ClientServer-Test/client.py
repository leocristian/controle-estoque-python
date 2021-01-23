import socket
import sys
import json

HOST, PORT = "localhost", 4444
sockObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def menuPrincipal():

    print("\n**************** MENU *******************")
    print("-----------------------------------------")
    print("------- 1 - Entrar ----------------------")
    print("------- 2 - Cadastrar funcionario -------")
    print("--------0 - Sair-------------------------")
    print("*****************************************")
    
    esc = int(input("Escolha uma das opções: "))

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

    msg = {"id": 1, "nome": nome, "cpf": cpf, "end": end, "tel": telefone, "idade": idade, "email": email}

    return msg

def main():

    sockObj.connect((HOST, PORT))
    print("Conexao estabelecida.")
    
    while True:
        opMenu = menuPrincipal()

        if opMenu == 0:
            print("Fechando servidor..")
            sockObj.close()
            break

        elif opMenu == 1:
            sockObj.send("1".encode())

        elif opMenu == 2:
            # recebe os dados vindos da função cadPessoa em forma de dicionario
            dataDict = cadPessoa()

            # converte os dados em um objeto JSON para enviar pro servidor
            dataJson = json.dumps(dataDict)
            sockObj.sendall(bytes(dataJson, encoding="utf-8"))
            
            # Resposta do servidor
            received = sockObj.recv(1024)
            received = received.decode("utf-8")

            print(f"Dado enviado: {dataJson}")
            print(f"Dado recebido: {received}")


if __name__ == "__main__":
    main()