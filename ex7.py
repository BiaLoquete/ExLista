vl = []

while True:
    num = (int(input('Digite um número: ')))
    if num in vl:
        vl.pop()
    vl.append(num)
    sr = str(input("Quer sair?"))
    if sr == "s":
        break
vl.sort()
print(vl)

