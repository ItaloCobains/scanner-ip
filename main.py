import socket
import requests
import smtplib
from email.message import EmailMessage


class Script:
    def pegar_ip(self):
        ip_local = socket.gethostbyname(socket.gethostname())
        ip_publico = requests.get('https://api.ipify.org').text
        message_com_ip = f"ip local = {ip_local} e ip_puclico = {ip_publico}"
        message_com_ip = str(message_com_ip)
        return message_com_ip

    def enviar_email(self, mensagem):
        ENDERECO_DE_EMAIL = ''
        SENHA_DO_EMAIL = ''
        msg = EmailMessage()
        msg['Subject'] = ''
        msg['From'] = ''
        msg['To'] = ''
        msg.set_content(mensagem)
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(ENDERECO_DE_EMAIL,SENHA_DO_EMAIL)
            smtp.send_message(msg)


script = Script()
a = script.pegar_ip()
script.enviar_email(mensagem=a)
