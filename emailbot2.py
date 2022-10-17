import smtplib # Biblioteca de envio de E-mail - Simple Mail Transfer Protocol
from email.mime.multipart import MIMEMultipart # MIME seria normas - Seria para criar menssagem em multipart
from email.mime.text import MIMEText # Envio De menssagem de texto
from email.mime.base import MIMEBase # Algo em anexo
from email import encoders # Para codificar a menssagem

# Variavel para colocar meu e-mail
fromaddr = "email@gmail.com"
# Variavel para receber menssagem
toaddr = "email@gmail.com"  # "irineu@gmail.com" - Para envia para mais pessoas

msg = MIMEMultipart()

# Variavel para evia 
msg['From'] = fromaddr
# Variavel para receber
msg['To'] = toaddr
# Variavel para titulo do e-mail
msg['Subject'] = "É essa peça que você queria?"


# Variavel pro corpo do texto do e-mail
body = """" title """
body = """" menssager """

# Envia tudo q tiver no corpo do e-mail
msg.attach(MIMEText(body, 'plain'))
# Anexo

filename = "arquivo"
# Variavel para abrir o arquivo, rb reader ele vai ler
anexo = open("arquivo", "rb")

p = MIMEBase('application', 'octet-stream')
# Esse comando ele vai ler o arquivo e salva nosso arquivo na mémoria 
p.set_payload((anexo).read())

# Comando para codificar nosso anexo baseado em 64
encoders.encode_base64(p)
# onde vai ter nosso anexo para envia
p.add_header('Content-Disposition', "attachement; filename= %s" % filename)

msg.attach(p)

# Variavel para conectar no servidor e-mail
s = smtplib.SMTP('smtp.gmail.com', 587)
# Conexão segura com e-mail
s.starttls()

# Acessar meu e-mail
s.login(fromaddr, 'daqgvzwovsymqfij')

# Converter codigo em string
text = msg.as_string()

# qual meu acesso? para quem vou envia? qual é a menssagem?
s.sendmail(fromaddr, toaddr, text)

# Fecha nossa conexão 
s.quit()