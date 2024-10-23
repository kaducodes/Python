#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('{:-^40}'.format(' PA '))
s = 0
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro , décimo + razão, razão):
    s += 1
    print(f'{s}º termo: {c}')
