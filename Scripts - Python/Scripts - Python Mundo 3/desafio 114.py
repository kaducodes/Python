#Crie um código em Python que teste se o site Pudim está acessível no computador usado.
#pudim.com.br

#Consegui acessar o site Pudim com sucesso! (amarelo)

#O site pudim não está acessível no momento. (vermelho)

import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com Sucesso!')
    print(site.read())
