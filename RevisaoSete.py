altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
IMC = peso/(altura)**2
if IMC < 18.6:
   print("Abaixo do peso")
elif 18.6>=IMC<=24.9:
    print("Peso ideal (Parabéns)")
elif 25>=IMC<29.9:
    print("Levemente acima do peso")
elif 30>=IMC<=34.9:
    print("Obesidade nível I")
elif 35>=IMC<=39.9:
    print("Obesidade II (severa)")
else:
    print("Obesidade grau III (mórbida)")