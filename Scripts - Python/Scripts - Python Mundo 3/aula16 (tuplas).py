#Tuplas
#toda variável é um espaço na memória
#é possível reservar mais de um espaço na memória para uma variável através das tuplas
#a variável que armazena mais de um espaço memória é a variável composta
#variáveis compostas podem ser feitas com tuplas, listas e dicionários.
#as tuplas são IMUTÁVEIS, uma vez definida, não tem como mudar enquanto o programa estiver rodando, somente na declaração no código
#(): tuplas
#[]: listas
#{}: dicionários
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche[:3])
print(lanche[3:])
print(lanche[3])
print(lanche[-3])
print(f'Organizados: {sorted(lanche)}')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!\n')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!\n')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!\n')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
#contar quantos elementos iguais tem na tupla
print(c.count(2))
#mostra em que posição na tupla está o elemento (mostra a primeira que aparece)
print(c.index(8))
#As tuplas, ao contrário dos vetores em java, aceitam mais de um tipo de variável
pessoa = ('Kadu', '38', 'M', '74kg')
print(pessoa)
#você pode apagar a tupla através do comando del(nome da tupla)

