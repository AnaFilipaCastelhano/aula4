#quando o utilizador diz q quer colocar o tesouro no 11, é na primeiro linha primeira coluna, se disser 31 é na terceita linha, primeira colluna, e tem q se trocar o quadrado por um X

row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]

map = [row1, row2, row3]


position = input("Where do you want to put the treasure?")

map[int(position[0])-1][int(position[1])-1] = "X"

print(f"{row1}\n{row2}\n{row3}")







