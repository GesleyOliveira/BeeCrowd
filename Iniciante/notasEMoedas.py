"""Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal."""

valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    numero_nota = int(valor / nota)
    print(f"{numero_nota} nota(s) de R$ {nota:.2f}")
    valor -= numero_nota * nota
    
print("MOEDAS:")
for moeda in moedas:
    numero_moedas = int(round(valor, 2) / moeda)
    print(f"{numero_moedas} nota(s) de R$ {moeda:.2f}")
    valor -= numero_moedas * moeda
    
    
"""Em Python 3"""

valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    numero_nota = int(valor / nota)
    print("{} nota(s) de R$ {:.2f}".format(numero_nota, nota))
    valor -= numero_nota * nota
    
print("MOEDAS:")
for moeda in moedas:
    numero_moedas = int(round(valor, 2) / moeda)
    print("{} moeda(s) de R$ {:.2f}".format(numero_moedas, moeda))
    valor -= numero_moedas * moeda