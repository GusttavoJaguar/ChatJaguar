# Botão de iniciar chat
# Pop-up para entrar no chat
# Quando entrar no chat : Aparece para todo mundo
    # A mensagem que você entrou no chat
    # O campo e o botão de enviar mensagem
# A cada mensagem que você envia : Aparece para todo mundo
    # Nome: Texto da mensagem
import flet as ft 

def main(pagina):

    texto = ft.Text(" JaguarChat ")

    chat = ft.Column()
    
    nome_usuario = ft.TextField(label="Digite seu nome")


    
    def enviar_mensagem_tunel(mensagem):

        tipo = mensagem["tipo"]

        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            # adicionar mensagem no chat
            chat.controls.append(ft.Text(f"{usuario_mensagem }: {texto_mensagem}"))
        else: 
             usuario_mensagem = mensagem["usuario"]
             chat.controls.append(ft.Text(f"{usuario_mensagem } entrou no chat", size=15, italic=True,  color=ft.colors.YELLOW_600))
        pagina.update()


    # PUBLISH
    # SUBSCRIBE
    # PUBSUB
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto" : campo_mensagem.value, "usuario" : nome_usuario.value, "tipo": "mensagem"} )
        # limpar campo da mensagem
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem= ft.TextField(label="Digite sua mensagem")

    botoa_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    
    def entrar_popup(evento):
        pagina.pubsub.send_all({"usuario" : nome_usuario.value, "tipo":"entrada"} )
        # adicionar o chat
        pagina.add(chat)
        # fechar o popup
        popup.open = False
        pagina.update()
    
        # remover o botão de iniciar o chat
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        # criar o campo da mensagem do usuário 
        pagina.add(ft.Row(
            [
                campo_mensagem, botoa_enviar_mensagem
            ]

        ))
        pagina.add(campo_mensagem)

        # criar o botão de enviar mensagem do usuário
        pagina.add(botoa_enviar_mensagem)
        pagina.update()

    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=ft.Text("Bem vindo ao nosso chat"),
        content=nome_usuario, 
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)], 
    )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update() 

    
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=entrar_chat)



    pagina.add(texto)
    pagina.add(botao_iniciar)
    

ft.app(target=main, view=ft.WEB_BROWSER, port=8000)