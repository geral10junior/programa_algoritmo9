#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada.

valor = int(input("Deseja ver a tabuada de qual número? "))
print('A tabuada de ' ,valor,' é:', sep="")
for i in range(1,11):
    print(valor,'X',i,'=', valor*i)