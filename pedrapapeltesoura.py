import random

#pedir para escolher 0,1 ou 2
# o computador escolhe tb 1

# 0

escolha_user = int(input("Escolha um nº:"))
opcoes = ["pedra","papel","tesoura"]

if not escolha_user > 2:
    escolha_user = opcoes[escolha_user]
else:
    print("Escolha errada")


escolha_pc = random.choice(["pedra","papel","tesoura"])
print(escolha_pc)






#if escolha_user == 0:
#    escolha_user = opcoes[escolha_user]
#elif escolha_user == 1:
#    escolha_user = "papel"
#elif escolha_user == 2:
#    escolha_user = "tesoura"
#else:
#    print("Opção errada!")

print(escolha_user)

if escolha_user == escolha_pc:
    print("Empataram")
elif escolha_user == "pedra":
    if escolha_pc == "papel":
        print("PC ganhou")
    else:
        print("User ganhou")
elif escolha_user == "papel":
    if escolha_pc == "pedra":
        print("User ganhou")
    else:
        print("Pc ganhou")
elif escolha_user == "tesoura":
    if escolha_pc == "pedra":
        print("Pc ganhou")
    else:
        print("User ganhou")
