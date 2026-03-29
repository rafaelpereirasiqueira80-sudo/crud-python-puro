from time import sleep

print("-------------------------------------------------------------------")
print("---------------------------NOTAS UNIP------------------------------")
print("-------------------------------------------------------------------")

list_nome = []
list_notanp1 = []
list_notanp2 = []
list_notapim = []
list_notamedia = []

def tempo() :
    sleep(0.5)

def tempo_longo() :
    sleep(1.5)

def menu() :
    tempo()
    print("\n1.Inserir Nota")
    print("2.Ver Aluno")
    print("3.Alterar Nota")
    print("4.Excluir Aluno")
    print("5.Critério de Nota")
    print("6.Criador")
    print("7.Sair")

menu()
escolha = input("Escolha(1,2,3,4,5,6,7): ")

while escolha != "7" and escolha != "sete" :
    if escolha == "1" or escolha == "um" :
        add_nome = input("\nEscreva o seu nome: ")
        add_notanp1 = float(input("\nEscreva a sua nota NP1: "))
        add_notanp2 = float(input("\nEscreva a sua nota NP2: "))
        add_notapim = float(input("\nEscreva a sua nota PIM: "))
        add_media = (add_notanp1 * 4 + add_notanp2 * 4 + add_notapim * 2) / 10

        tempo_longo()
        list_nome.append(add_nome)
        list_notanp1.append(add_notanp1)
        list_notanp2.append(add_notanp2)
        list_notapim.append(add_notapim)
        list_notamedia.append(add_media)

        tempo()
        print("Adicionado com sucesso")

        menu()
        escolha = input("Escolha(1,2,3,4,5,6,7): ")

    elif escolha == "2" or escolha == "dois" :
        if len(list_nome) > 0 :
            for index in range(len(list_nome)) :
                print("\n--------------------------------------------")
                print(f"------------Aluno UNIP {index + 1}-------------")
                print(f"----------Nome: {list_nome[index]}---------")
                print(f"------NotaNP1 : {list_notanp1[index]}------")
                print(f"------NotaNP2 : {list_notanp2[index]}------")
                print(f"------NotaPIM : {list_notapim[index]}------")
                print(f"----Nota Média: {list_notamedia[index]}----")
                print("--------------------------------------------\n")

            menu()
            escolha = input("Escolha(1,2,3,4,5,6,7): ")
        else :
            tempo()
            print("\n\nNão foi adicionado alunos a esta lista!!!\n\n")

            tempo()
            menu()
            escolha = input("Escolha(1,2,3,4,5,6,7): ")


    elif escolha == "3" or escolha == "três" :
        for index in range(len(list_nome)) :
            print("\n--------------------------------------------")
            print(f"------------Aluno UNIP {index + 1}-------------")
            print(f"----------Nome: {list_nome[index]}---------")
            print(f"------NotaNP1 : {list_notanp1[index]}------")
            print(f"------NotaNP2 : {list_notanp2[index]}------")
            print(f"------NotaPIM : {list_notapim[index]}------")
            print(f"----Nota Média: {list_notamedia[index]}----")
            print("--------------------------------------------\n")

        editar = int(input("Qual aluno você quer alterar?: ")) - 1

        tempo_longo()
        if editar >= 0 and editar < len(list_nome) :
            list_nome[editar] = input(f"\nMude o nome do aluno {list_nome[editar]} para: ")
            list_notanp1[editar] = float(input(f"\nMude a nota NP1 do aluno {list_nome[editar]} de {list_notanp1[editar]} para: "))
            list_notanp2[editar] = float(input(f"\nMude a nota NP2 do aluno {list_nome[editar]} de {list_notanp2[editar]} para: "))
            list_notapim[editar] = float(input(f"\nMude a nota do PIM do aluno {list_nome[editar]} de {list_notapim[editar]} para: "))
            list_notamedia[editar] = (list_notanp1[editar] * 4 + list_notanp2[editar] * 4 + list_notapim[editar] * 2) / 10

        print(f"\n O aluno {list_nome[editar]} foi modificado com sucesso")

        menu()
        escolha = input("Escolha(1,2,3,4,5,6,7): ")

    elif escolha == "4" or escolha == "quatro" :
        if len(list_nome) > 0 :
            for index in range(len(list_nome)) :
                print("\n--------------------------------------------")
                print(f"------------Aluno UNIP {index + 1}-------------")
                print(f"----------Nome: {list_nome[index]}---------")
                print(f"------NotaNP1 : {list_notanp1[index]}------")
                print(f"------NotaNP2 : {list_notanp2[index]}------")
                print(f"------NotaPIM : {list_notapim[index]}------")
                print(f"----Nota Média: {list_notamedia[index]}----")
                print("--------------------------------------------\n")

            deletar = int(input("Qual aluno você deseja deletar?(Número) : ")) - 1

            nome_antigo = list_nome[deletar]

            if deletar >= 0 and deletar < len(list_nome) :
                list_nome.pop(deletar)
                list_notanp1.pop(deletar)
                list_notanp2.pop(deletar)
                list_notapim.pop(deletar)
                list_notamedia.pop(deletar)

            tempo_longo()
            print(f"O aluno {nome_antigo} foi deletado com sucesso!!: ")

            menu()
            escolha = input("Escolha(1,2,3,4,5,6,7): ")


    elif escolha == "5" or escolha == "cinco" :
        print("\n----------------------------------------------------------------------")
        print("-----O Critério da Nota: (NotaNP1*4 + NotaNP2*4 + NotaPIM*2) / 10-----")
        print("-----------------------------------------------------------------------\n")

        menu()
        escolha = input("Escolha(1,2,3,4,5,6,7): ")

    elif escolha == "6" or escolha == "seis" :
        print("\n----------------------------------------------------------------------")
        print("----------------------CRIADO POR: RADMIN VPN--------------------------")
        print("----------------------------------------------------------------------\n")

        menu()
        escolha = input("Escolha(1,2,3,4,5,6,7): ")

    else :
        print("Você escreveu o valor errado!!!")

        menu()
        escolha = input("Escolha(1,2,3,4,5,6,7): ")