# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

print('-' * 35)
print('Programa - Analisador de Triângulos')
print('-' * 35)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Esses segmentos de reta PODEM formar um triângulo', end=' ')
    if s1 == s2 and s2 == s3:
        print('EQUILÁTERO!')
    elif s1 != s2 and s2 != s3 and s1 != s3:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Esses segmentos de reta NÃO podem formar um triângulo')
