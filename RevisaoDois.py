num = int(input("Digite um número qualquer: "))
if num%2==1 and num>0:
    print("O resultado é ímpar e positivo")
elif num%2==1 and num<0:
    print("O resultado é ímpar e negativo")
elif num%2==0 and num>0:
    print("O resultado é par e positivo")
elif num%2==0 and num < 0:
    print("O resultado é par e negativo")

# if num > 0 :
#  if num%2==0:
#      print("Par positivo")
#  else:
#     print("impar positivo)
# else:
#    if num%2==0:
#       print("Par negativo")
#    else:
#         print("Impar negativo)