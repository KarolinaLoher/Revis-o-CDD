numA = int(input("Digite um valor: "))
numB = int(input("Digite um valor: "))
numC = int(input("Digite um valor: "))

soma = numA + numB
print(soma)
if soma < numC:
    print(f"O valor {soma} é menor que {numC}")
else:
    print(f"O valor {soma} é maior que {numC}")