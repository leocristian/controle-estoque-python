def menuPrincipal():
    print("**************** MENU *******************")
    print("-----------------------------------------")
    print("------- 1 - CADASTRAR FUNCIONÁRIO -------")
    print("------- 2 - ENTRAR ----------------------")
    print("-----------------------------------------")
    print("*****************************************")
    
    esc = int(input("Escolha uma das opções: "))

    return esc

def main():

    esc = menuPrincipal()



if __name__ == "__main__":
    main()