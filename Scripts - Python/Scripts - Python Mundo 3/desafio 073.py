#Crie uma tupla preenchida com os 20 primeiros colocados
#da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
#Depois mostre:
#A) Apenas os 5 primeiros colocados.
#B) Os últimos 4 colocados
#C) Uma lista com os times em ordem alfabética
#D) Em que posição na tabela está o time do São Paulo
times = ('São Paulo', 'Vitória', 'Grêmio', 'Flamengo', 'Botafogo', 'Palmeiras', 'Athletico-PR', 'Cruzeiro', 'Fortaleza',
          'Bragantino', 'Internacional', 'Atlético-MG', 'Juventude', 'Criciúma', 'Cuiabá', 'Vasco', 'Atlético-GO',
          'Fluminense', 'Corinthians', 'Bahia')

print(f'Os 5 Primeiros Colocados são: {times[:5]}')
print(f'Os últimos 4 Colocados são: {times[-4:]}') # ou {times[16:]}
print(f'Os times em ordem alfabética: {sorted(times)}')
time = 'São Paulo'
print(f'O time do São Paulo está na {times.index(time) + 1}ª Posição')
p = 0
for t in times:
    p += 1
    print(f'{p}º - {t}')
