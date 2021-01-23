import socket
import json
from pessoa import Pessoa

HOST, PORT = "localhost", 4444

socketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketObj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

addr = ((HOST, PORT))

socketObj.bind(addr)
socketObj.listen(10)

listaPessoas = []

print("Servidor iniciado!")
print("Aguardando um cliente...")

conn, ender = socketObj.accept()

print(f"Conectado no endereço: {ender}")

while True:
    data = conn.recv(1024)
    print("Mensagem recebida: ", data.decode())

    if not data:
        break
    elif (data.decode() == "1"):
        print("entrou")
    elif (data.decode() == "2"):

        dataFormated = json.loads(data.decode())

        nome = dataFormated["nome"]
        cpf = dataFormated["cpf"]
        end = dataFormated["end"]
        tel =  dataFormated["tel"]
        idade = dataFormated["idade"]
        email = dataFormated["email"]

        pessoa = Pessoa(nome, cpf, end, tel, idade, email)

        listaPessoas.append(pessoa)

        conn.send(data)

        print("--------lista-------")

        for i in listaPessoas:
            print(i.nome)

    print("--------------------")
    print("Aguardando dados do cliente.")

print("Fechando conexao...")
conn.close()
