n1 = int(input('Um número: '))
n2 = int(input('Outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
di = n1 // n2
r = n1 % n2
print(f'A soma é {s}; \nO produto é {m}; \nA divisão é {d:.2f};')
print(f'A divisão inteira é {di} restando {r} dessa divisão;')
print(f'A potência é {e:=^20}.')



