num1 = []
while True :
    num = (int(input('Digite um número (digite 0 para parar): ')))
    num1.append(num)
    if num == 0:
        num1.remove(0)
        break

soma = sum(num1)
menor = min (num1)

print(f'Os números são {num1}')
print(f"Menor é: {menor}")
print(f'A soma é  {soma}')

