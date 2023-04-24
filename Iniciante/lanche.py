valor = str(input())
valor = valor.split(" ")
item = valor[0].lower()
preco = valor[1]

if item == "1":
    cod1 = 4.00 * int(preco)
    print(f"Total: R$ {cod1:.2f}")
elif item == "2": 
    cod2 = 4.50 * int(preco)
    print(f"Total: R$ {cod2:.2f}")
elif item == "3": 
    cod3 = 5.00 * int(preco)
    print(f"Total: R$ {cod3:.2f}")
elif item == "4": 
    cod4 = 2.00 * int(preco)
    print(f"Total: R$ {cod4:.2f}")
elif item == "5": 
    cod5 = 1.50 * int(preco)
    print(f"Total: R$ {cod5:.2f}")