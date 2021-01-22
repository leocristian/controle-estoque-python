import socket
import json
from pessoa import Pessoa

HOST, PORT = "localhost", 6666

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

    if not data:
        break

    print("Mensagem recebida: ", data.decode())

    print(type(data.decode()))


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

print("Fechando conexao...")
conn.close()
