import socket
import json
import sqlite3

from classes.pessoa import Pessoa
from classes.produto import Produto
from classes.estoque import Estoque

HOST, PORT = "localhost", 5000

socketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketObj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

addr = ((HOST, PORT))

socketObj.bind(addr)
socketObj.listen(10)

print("Servidor iniciado!")
print("Aguardando um cliente...")

conn, ender = socketObj.accept()

database = sqlite3.connect("database.sqlite")
cursor = database.cursor()

print(f"Conectado no endereço: {ender}")

listaFuncionarios = []
listaClientes = []

cursor.execute('''CREATE TABLE IF NOT EXISTS funcionarios(id integer PRIMARY KEY, nome text NOT NULL, cpf text NOT NULL, endereco text, telefone text, idade integer, email text)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS clientes(id integer PRIMARY KEY, nome text NOT NULL, cpf text NOT NULL, endereco text, telefone text, idade integer, email text)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS estoque(id integer PRIMARY KEY, nome text NOT NULL, desc text, preco real NOT NULL, qtd integer NOT NULL)''')

estoque = Estoque()

qtdprod = 0

while True:

    data = conn.recv(1024)

    if not data:
        print("Nenhum dado recebido...")
        break
    else:
        print("Mensagem recebida: ", data.decode())

#-------------------------------Comandos para enviar uma lista para exibir na no client-------------------

        if (data.decode() == "mostrarFuncionario"):
            print("Enviando funcionarios...")
            nomesFunc = []

            print("for listafunc")
            cursor.execute("SELECT * FROM funcionarios")
            for f in cursor:
                print(f[1])
                #nomesFunc.append(f[1])

            if len(listaFuncionarios) == 0:
                print("Lista vazia...")
                conn.send("vazia".encode())
            else:
                for i in listaFuncionarios:
                    print(i.nome)
                    nomesFunc.append(i.nome)
                
                conn.send(",".join(nomesFunc).encode())

        elif(data.decode() == "mostrarEstoque"):
            listaProdutos = []

            print("quantidade de produtos: ", qtdprod)
            cursor.execute("SELECT * FROM estoque")

            print("Produtos---------")
    
            if(qtdprod == 0):
                print("Estoque vazio..")
                conn.send("vazia".encode())
            else:
                for i in cursor:
                    prodDict = {"nome": i[1], "preco": i[3], "qtd": i[4]}
                    print(prodDict)
                    prodDict = json.dumps(prodDict)
                    listaProdutos.append(prodDict)
                    print(i)

                print("Enviando estoque...")
                conn.send(";".join(listaProdutos).encode())
                

        elif(data.decode() == "mostrarClientes"):
            print("enviando clientes...")

            nomesClientes = []

            print("for listacli")

            if len(listaClientes) == 0:
                print("Lista vazia...")
                conn.send("vazia".encode())
            else:
                for i in listaClientes:
                    print(i.nome)
                    nomesClientes.append(i.nome)
                
                conn.send(",".join(nomesClientes).encode())

        elif(data.decode() == "mostrarHistorico"):
    
            listaHist = []

            print("entrou historico")

            if len(estoque.historico) == 0:
                print("Historico vazio...")
                conn.send("vazio".encode())
            else:

                for i in estoque.historico:
                    print(i)
                    listaHist.append(i)
            
                conn.send(";".join(listaHist).encode())

    #--------------------------------Comandos para realizar alguma operação no servidor (cadastro, remoção, venda)--------
        else:
            print("entrou else")
            dataFormated = json.loads(data.decode()) # Converte dado recebido (str) em um dicionário

            tipo = dataFormated["tipo"]

            print("Tipo: ", tipo)

            if tipo == "venderProduto": # significa que o usuário quer realizar uma venda
        
                idCliente = int(dataFormated["idCliente"])
                nomeProduto = dataFormated["nomeProduto"]
                qtdprod = int(dataFormated["qtdProd"])

                print("id cli: ", idCliente)
                print("Nome prod: ", nomeProduto)
                print("qtd: ", qtdprod)

                cursor.execute("SELECT qtd FROM estoque WHERE nome=?", (nomeProduto, ))

                for x in cursor:
                    qtdAtual = x[0]

                print("qtdAtual: ", qtdAtual)
                print(type(qtdAtual))

                cursor.execute("UPDATE estoque SET qtd=? WHERE nome=?", ((qtdAtual - qtdprod), nomeProduto))
                database.commit()

                estoque.historico.append("Remocao de {} efetuada. quantidade atual: {}".format(nomeProduto,(qtdAtual-qtdprod)))

                print("cursor: ", cursor)
                if(cursor):
                    conn.send("produtoVendido".encode())
                else:
                    conn.send("erroVenda".encode())

            elif tipo == "produto":
                nome = dataFormated["nome"]
                desc = dataFormated["desc"]
                preco = dataFormated["preco"]
                qtd = dataFormated["qtd"]

                prod = Produto(nome, desc, preco, qtd)

                cursor.execute("INSERT INTO estoque (nome, desc, preco, qtd) VALUES (?, ?, ?, ?)", (nome, desc, preco, qtd))
                database.commit()

                estoque.armazenar(prod)
                qtdprod += 1

                conn.send("produtoCadastrado".encode())

            else: # significa que o dado enviado é de uma pessoa

                nome = dataFormated["nome"]
                cpf = dataFormated["cpf"]
                end = dataFormated["end"]
                tel =  dataFormated["tel"]
                idade = dataFormated["idade"]
                email = dataFormated["email"]
        
                if tipo == "funcionario" : # Mostra que a pessoa enviada é um funcionário

                    pessoa = Pessoa(nome, cpf, end, tel, idade, email)

                    cursor.execute("INSERT INTO funcionarios (nome, cpf, endereco, telefone, idade, email) VALUES (?, ?, ?, ?, ?, ?)", (nome, cpf, end, tel, idade, email))
                    database.commit()
    
                    listaFuncionarios.append(pessoa)
            
                    conn.send("funcionarioCadastrado".encode())

                elif tipo == "cliente":  # Mostra que a pessoa enviada é um cliente
                    pessoa = Pessoa(nome, cpf, end, tel, idade, email)

                    cursor.execute("INSERT INTO clientes (nome, cpf, endereco, telefone, idade, email) VALUES (?, ?, ?, ?, ?, ?)", (nome, cpf, end, tel, idade, email))
                    database.commit()

                    listaClientes.append(pessoa)

                    conn.send("clienteCadastrado".encode())

            #conn.send(data)

    print("--------lista funcionarios-------")

    for i in listaFuncionarios:
        print(i.nome)

    print("---------------------------------")
    print("--------lista clientes-------")

    for i in listaClientes:
        print(i.nome)

    print("---------------------------------")
    print("Aguardando dados do cliente.")

    print("-----------Estoque''''''''''''''")

    estoque.listar()

    print("---------------------------------")


print("Fechando conexao...")    
database.commit()
database.close()
conn.close()

