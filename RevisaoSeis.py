salMinimo = float(input("Qual é o salário minímo?"))
while True:
    salUsuario = float(input("Digite seu salário ou zero pra encerrar."))
    if salUsuario == 0:
        print("Programa encerrado")
        break
    divisao = salUsuario/salMinimo
    print(f"Você recebe {divisao}x salários minímos")



