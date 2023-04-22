"""Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem"""

from math import sqrt
x = str(input())
lista = x.split(" ")
valores = []
for i in lista:
    valores.append(float(i))
a = valores[0]
b = valores[1]
c = valores[2]

if (a==0 or a<0) or (b==0 or b<0) or (c==0 or c<0) or ((b**2)<(4*a*c)):
    print("Impossivel calcular")
else:
    r1 = ((-b) + (sqrt((b**2) - (4*a*c)))) / (2*a)
    r2 = ((-b) - (sqrt((b**2) - (4*a*c)))) / (2*a)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")


    
