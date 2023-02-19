
# 40. Faça um programa que leia um número inteiro e, verifique se o número digitado é primo
#O que é número primo?
# São os números naturais que têm apenas dois (2) divisores diferentes: o 1 e ele mesmo, por exemplo,
#  5 é primo, pois dividi apenas por 1 e por ele

#6 não é primo, pois dividi por 2 e por 3


Numero = int(input("Digite um Numero para Verificar se o numero é primo: "))
mult=0

for count in range(2,Numero):
    if (Numero % count == 0):
        print("Múltiplo de",count)
        mult += 1

if(mult==0):
    print("É primo")
else:
    print("Não primmo, pois tem",mult,"Numeros múltiplos acima de 2 e abaixo de",Numero)