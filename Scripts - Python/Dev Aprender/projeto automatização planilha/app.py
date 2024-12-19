import openpyxl
import pyperclip
import pyautogui

#entrar na planilha
workbook = openpyxl.load_workbook('produtos_ficticios.xlsx')
sheet_produtos = workbook['Produtos']
#copiar informação de um campo e colar no seu campo correspondente
for linha in sheet_produtos.iter_rows(min_row=2):
    nome_produto = linha[0].value
    pyperclip.copy(nome_produto)
    pyautogui.click(818,189, duration=1)
    pyautogui.hotkey('ctrl', 'v')
    

#repetir esses passos para outros campos até preencher campos daquela página
#clicar em próxima
#repetir os mesmos passos e ir para a próxima página (página 2)
#repetir os mesmos passos e finalizar o cadastro daquele produto e clicar em concluir
#clicar em ok para finalizar o processo
#clicar no ok mais uma vez na mensagem de confirmação de salvamento no banco de dados
#clicar em "adicionar mais um e repetir o proceso até finalizar a planilha"
#site usado para automação: https://cadastro-produtos-devaprender.netlify.app/
# pyautogui (automação de clicks e teclado)
# openpyxl (leitura e automação de planilhas)