# Passo a passo
# Título: Hashzap
# Botão: Iniciar Chat
    # popup/modal/alerta
        # Título: Bem vindo ao Hashzap
        # Campo de Texto: Escreva seu nome no chat
        # Botão: Entrar no chat
            # Sumir com o Título e o Botão Inicial
            # Fechar o popup
            # Criar o chat (com a mensagem de "nome do usuario entrou no chat")
            # Embaixo do chat:
                # Campo de texto: Digite sua mensagem
                # Botão: Enviar
                    # Vai aparecer a mensagem no chat com o nome do usuário
                    # Lira: Coe galera

# frameworks mais usados:
# flask: instagram
# django: spotify

# fast api
# tornado
# flet: ferramenta nova, com o mesmo código roda sites, app e software

# importar o flet
import flet as ft

# criar uma função principal do seu sistema, obrigatoriamente tem que receber a página do seu app como parâmetro
def main(pagina):
    # criar alguma coisa
    # criar o título
    titulo = ft.Text("Hashzap")

    # criar um túnel de comunicação (socket) entre todos os usuários de nosso site
    # cria a função do túnel
    def enviar_mensagem_tunel(mensagem):
        chat.controls.append((ft.Text(mensagem)))
        pagina.update()

    # cria o túnel
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    titulo_janela = ft.Text("Bem vindo ao Hashzap")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no Chat")

    def enviar_mensagem(evento):
        # enviar mensagem no chat (Usuario: mensagem)
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"

        # enviar uma mensagem no túnel
        pagina.pubsub.send_all(texto)

        # limpar o campo de mensagem
        texto_mensagem.value = ""
        pagina.update()

    # arquivo = ft.FilePicker() -> para adicionar imagem

    texto_mensagem = ft.TextField(label="Digite sua Mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    # criar colunas e linhas
    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])

    # criar o chat
    chat = ft.Column()

    # toda função de botão tem que receber um evento como parâmetro
    def entrar_chat(evento):
        # tirar o título da página
        pagina.remove(titulo)
        # tirar o botao_iniciar
        pagina.remove(botao_iniciar)
        # fechar o popup/janela
        janela.open = False
        # adicionar o chat
        pagina.add(chat)
        # adicionar a linha de mensagem
        pagina.add(linha_mensagem)

        # escrever a mensagem: "Usuario Entrou no Chat"
        # dentro da função pois só será executada nessa função
        texto_entrou_chat = f"{campo_nome_usuario.value} Entrou no Chat"
        pagina.pubsub.send_all(texto_entrou_chat)

        pagina.update()

    botao_entrar = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)

    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome_usuario,
        actions=[botao_entrar]
    )

    # toda função de botão tem que receber um evento como parâmetro
    def abrir_popup(evento):
        # janela é diferente, não é apenas add e remove como os outros
        pagina.dialog = janela
        janela.open = True
        # toda vez que uma função sua editar sua página visualmente, atualize
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    # colocar essa coisa na página
    # adicionar o título na página
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# executar o seu sistema
ft.app(main, view=ft.WEB_BROWSER)
# ft.app(main, view=ft.WEB_BROWSER)