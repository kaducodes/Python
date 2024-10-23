frase = '     Curso em Vídeo Python    '
print(frase[::2])
print('''oi, tudo bem?
vamos lá!!
Sabe quantas vezes aparece o "o" maiúsculo??''')
print(frase.upper().count('O'))
print('Sabe quantas letras tem nessa frase?')
print(len(frase.strip()))
print('Sabe que curso podemos ter também?')
print(frase.strip().replace('Python', 'Android'))
print('Será que a palavra "Curso" está dentro da frase?')
print('Curso' in frase)
print('Será que existe a palavra "Vídeo" na frase? Em qual posição?')
print(frase.find('Vídeo'))
print('E a palavra "vídeo"?')
print(frase.find('vídeo'))
print('Mas se eu transformar essa string toda pra minúscula...')
print(frase.lower().find('vídeo'))
print('Pois agora quero uma lista com as palavras dessa frase!')
print(frase.split())
print('Hum... quero só a primeira palavra dessa lista')
dividido = frase.split()
print(dividido[0])
print('E agora a terceira letra da terceira palavra dessa frase!')
print(dividido[2] [2])


