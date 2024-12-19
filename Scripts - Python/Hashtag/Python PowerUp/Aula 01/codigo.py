# Passo 1 - Entrar no sistema da empresa
# Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2 - Fazer login
# Passo 3 - Pegar/Importar a base de dados
# Passo 4 - Cadastrar um produto
# Passo 5 - Repetir o passo 4 até cadastrar todos os produtos

import pyautogui
import time
import pandas
# pyautogui.click - clicar com o mouse
# pyautogui.write - escrever um texto
# pyautogui.press - apertar 1 tecla
# pyautogui.hotkey - combinação de teclas (Ctrl C)
# pyautogui.scroll - rolar a tela para cima ou para baixo
6.5
pyautogui.PAUSE = 0.9

# Passo 1 - Entrar no sistema
# Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# Passo 2 - Fazer login
# pyautogui.position(x=274, y=355)
pyautogui.press("tab")
pyautogui.hotkey("ctrl", "a")
pyautogui.write("kadu_dev@gmail.com")

# Passar para o campo de senha
pyautogui.press("tab")
pyautogui.write("minhasenha")

pyautogui.press("tab")
pyautogui.press("enter")
#
#   pyautogui.click(x=397, y=495)

time.sleep(3)

# Passo 3 - Pegar/Importar a base de dados

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# Passo 4 - Cadastrar um produto
# Para cada linha da minha tabela:
for linha in tabela.index:
    # codigo
    pyautogui.click(x=247, y=251)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

    # marca
    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)

    # tipo
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)

    # categoria
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    # preco_unitario
    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    # custo
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    # obs
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    # enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    # voltar para o início da tela
    pyautogui.scroll(5000)

# Passo 5 - Repetir o passo 4 até cadastrar todos os produtos