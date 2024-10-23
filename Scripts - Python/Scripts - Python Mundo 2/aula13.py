'''i = int(input('INÍCIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')'''

s = 0
for c in range(0, 4):
    n = int(input('Valor: '))
    s += n
print(f'A soma desses valores é {s}')
