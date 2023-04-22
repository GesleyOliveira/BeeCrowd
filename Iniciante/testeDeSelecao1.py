"""Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

Entrada
Quatro números inteiros A, B, C e D.

Saída
Mostre a respectiva mensagem após a validação dos valores."""

x = str(input())
lista = x.split(" ")
valores = []
for i in lista:
    valores.append(int(i))
a = valores

cond1= (a[1] > a[2])
cond2= (a[3] > a[0])
cond3= ((a[2] + a[3]) > (a[0] + a[1]))
cond4= (a[2]>0)
cond5= (a[3]>0)
cond6= ((a[0]%2)==0)

if cond1 and cond2 and cond3 and cond4 and cond5 and cond6:
    print("Valores aceitos")
else:   
    print("Valores nao aceitos")
