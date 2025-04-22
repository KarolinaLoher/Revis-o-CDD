novaTentativa = "SIM"
while novaTentativa == "SIM":
 num = int(input("Digite um número qualquer: "))
 if num%2==1 and num>0:
    print("O resultado é ímpar e positivo")
 elif num%2==1 and num<0:
    print("O resultado é ímpar e negativo")
 elif num%2==0 and num>0:
    print("O resultado é par e positivo")
 else:
    print("O resultado é par e negativo")
 novaTentativa = input("Deseja fazer uma nova tentativa?")