import win32com.client as win32


# criar a integracao do outlook 
outlook = win32.Dispatch('outlook.application')

#criar mail
mail = outlook.CreateItem(0)

# configurar as informacoes do mail

pessoa = input("Qual é o destinatario? ")
quemenvia = input("Quem envia? ")
emaildapessoa = input("Digite o e-mail para qual será enviado a mensagem: ")

mail.To = f'{emaildapessoa}'
mail.Subject =  "Teste Envio E-mail" #titulo do mail
mail.HTMLBody = f"""
<p>Olá, {pessoa}. Aqui quem fala é o {quemenvia}.</p>
<p>Boa noite!</p>
<p>Abs, {pessoa}.</p>"""
mail.Send()

print("e-mail enviado!")


