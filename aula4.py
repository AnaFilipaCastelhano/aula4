#condicionais

#if True:
#    print(2+2)

altura = 180
idade = 15
foto = "sim"
preço = 0

#até 12 anos - 10€
#acima paga 15€
# acima de 60 paga 8€

if not altura < 130:
    print("Pode entrar")
    if idade > 60 and idade < 80: #quando é and os 2 têm q ser true, quando é or só um deles é q tem q ser true
        preço = 8
    elif idade > 12:
        preço = 10
    else:
        preço = 15
    if foto == "sim":
        preço += 3
    print(f"O preço total é {preço}")
else:
    print("Não pode entrar")

# o utilizador digita o ano e o programa responde se é bissesto ou n
# um ano bissesto é divisivel por 4
# exceto se é divisivel por 100
# a menos que seja dividido por 400
#(se for divisivel por 4 e por 100 não é bissesto a menos que seja divisivel por 400 tb)

nome = "Ana Filipa Carrilho Castelhano"

print(nome.lower())
print(nome.count("a"))


