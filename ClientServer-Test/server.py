import socket
import json
from pessoa import Pessoa

import sqlite3

database = sqlite3.connect("database.db")

cursor = database.cursor()

HOST, PORT = "localhost", 4444

socketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketObj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

addr = ((HOST, PORT))

socketObj.bind(addr)
socketObj.listen(10)

listaPessoas = []
try:
    cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas(id integer PRIMARY KEY, nome text NOT NULL, cpf text NOT NULL, endereco text, telefone text, idade integer, email text)''')
    print("Tabela Pessoas Criada")
except:
    print("Erro ao criar tabela.")

print("Servidor iniciado!")
print("Aguardando um cliente...")

conn, ender = socketObj.accept()

print(f"Conectado no endereço: {ender}")

while True:
    data = conn.recv(1024)
    print("Mensagem recebida: ", data.decode())
    listaNomes = []

    if not data:
        break
    elif (data.decode() == "1"):
        print("entrou")

        if  len(listaPessoas) >= 1:
            for i in listaPessoas:
                nome = i.nome
                listaNomes.append(nome)
            dataSend = ",".join(listaNomes)
            print("Data Sent: ", dataSend)
            conn.send(dataSend.encode())
        else:
            conn.send("Lista vazia!!".encode())

    else:

        dataFormated = json.loads(data.decode())

        nome = dataFormated["nome"]
        cpf = dataFormated["cpf"]
        end = dataFormated["end"]
        tel =  dataFormated["tel"]
        idade = dataFormated["idade"]
        email = dataFormated["email"]

        pessoa = Pessoa(nome, cpf, end, tel, idade, email)

        cursor.execute("INSERT INTO pessoas (nome, cpf, endereco, telefone, idade, email) VALUES (?, ?, ?, ?, ?, ?)", (nome, cpf, end, tel, idade, email))

        listaPessoas.append(pessoa)

        conn.send(data)

        print("--------lista-------")

        for i in listaPessoas:
            print(i.nome)

    print("Aguardando dados do cliente.")
    print("--------------------")
    print("Tabela pessoas:")

    cursor.execute('SELECT * FROM pessoas')

    for x in cursor:
        print(x)
    
    database.commit()



print("Fechando conexao...")
database.close()
conn.close()
