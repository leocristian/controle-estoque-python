import socket
import json
from classes.pessoa import Pessoa

HOST, PORT = "localhost", 5000

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

    listaFuncionarios = []
    listaClientes = []

    data = conn.recv(1024)
    print("Mensagem recebida: ", data.decode())

    dataFormated = json.loads(data.decode())

    tipo = dataFormated["tipo"]
    nome = dataFormated["nome"]
    cpf = dataFormated["cpf"]
    end = dataFormated["end"]
    tel =  dataFormated["tel"]
    idade = dataFormated["idade"]
    email = dataFormated["email"]

    pessoa = Pessoa(nome, cpf, end, tel, idade, email)

    if(tipo == "funcionario"): # Mostra que a pessoa cadastrada é um funcionário
        listaFuncionarios.append(pessoa)
    elif tipo == "cliente":  # Mostra que a pessoa cadastrada é um cliente
        listaClientes.append(pessoa)

    conn.send(data)

    print("--------lista funcioanrios-------")

    for i in listaFuncionarios:
        print(i.nome)

    print("---------------------------------")
    print("--------lista clientes-------")

    for i in listaClientes:
        print(i.nome)

    print("---------------------------------")
    print("Aguardando dados do cliente.")

print("Fechando conexao...")
conn.close()

