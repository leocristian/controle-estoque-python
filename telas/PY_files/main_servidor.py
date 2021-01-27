import socket
import json
from classes.pessoa import Pessoa
from classes.produto import Produto
from classes.estoque import Estoque

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

listaFuncionarios = []
listaClientes = []

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

            if(qtdprod == 0):
                print("Estoque vazio..")
                conn.send("vazia".encode())
            else:
                
                for i in estoque.produtos:
                    prodDict = {"nome": i.nome, "preco": i.preco, "qtd": i.qtd}
                    prodDict = json.dumps(prodDict)
                    listaProdutos.append(prodDict)
                    print(i.nome)

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
                
            #conn.send("test".encode())
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
                
                confirmRemocao = estoque.remover(nomeProduto, qtdprod)

                print("Confirm Remocao: ", confirmRemocao)
                if(confirmRemocao == 1):
                    conn.send("produtoVendido".encode())
                else:
                    conn.send("erroVenda".encode())

            elif tipo == "produto":
                nome = dataFormated["nome"]
                desc = dataFormated["desc"]
                preco = dataFormated["preco"]
                qtd = dataFormated["qtd"]

                prod = Produto(nome, desc, preco, qtd)

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

                    listaFuncionarios.append(pessoa)
            
                    conn.send("funcionarioCadastrado".encode())

                elif tipo == "cliente":  # Mostra que a pessoa enviada é um cliente
                    pessoa = Pessoa(nome, cpf, end, tel, idade, email)

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
conn.close()

