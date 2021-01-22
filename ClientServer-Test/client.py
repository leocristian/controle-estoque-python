import socket
import sys
import json

HOST, PORT = "localhost", 6666
sockObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():

    sockObj.connect((HOST, PORT))
    print("conexao estabelecida.")
    
    while True:
        op = int(input("Cadastrar pessoa (1-sim | 0-Nao): "))

        if op == 1:

            print("**************** CADASTRO DA PESSOA *******************")
            print("------------------------------------------------------------")
            nome = input("------------- NOME: ")
            cpf = input("------------- CPF: ")
            end = input("------------- ENDEREÇO: ")
            telefone = int(input("------------- TELEFONE: "))
            idade = int(input("------------- IDADE: "))
            email = input("------------- E-MAIL: ")


            msg = {"id": 2, "nome": nome, "cpf": cpf, "end": end, "tel": telefone, "idade": idade, "email": email}
            data = json.dumps(msg)

            sockObj.sendall(bytes(data, encoding="utf-8"))
            received = sockObj.recv(1024)
            received = received.decode("utf-8")

        elif op == 0:
            print("Fechando servidor..")
            sockObj.close()
            break

        print(f"Dado enviado: {data}")
        print(f"Dado recebido: {received}")


if __name__ == "__main__":
    main()