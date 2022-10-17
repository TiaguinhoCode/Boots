from requests import options
from selenium import webdriver # Bilioteca para usar boot
from selenium.webdriver.common.keys import Keys # Biblioteca para dar acesso ao teclado e mouse pro pc
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

print("Iniciando robô")
time.sleep(1)

# Dados que usuario quer pesquisar
pesquisa = input("Digite a pesquisa:")

# Comando para n aparecer menssagem de erro
options = webdriver.ChromeOptions()
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")

# Instalando chormeDriver nas nuvens
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)
# Site da onde maquina vai pega informação
driver.get("https://www.google.com")

# Variavel para pesquisar
campo = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
# Mostrando dados que usario digitou pro computador
campo.send_keys(pesquisa)
# Comando para computador aperta ENTER
campo.send_keys(Keys.ENTER)

# Criando um variavel que mostra tanto de pagina é tempo de pesquisar que tem no google
resultados = driver.find_element(By.XPATH, "//*[@id='result-stats']").text
print(resultados)

# Vou criar variavel para dizer número de pagina
numero_resultados = float(resultados.split("Aproximadamente ")[1].split(' resultados')[0].replace('.',''))
# vou pega resultado paginal e dividir por 10 porque em uma pagina tem 10 elementos
maximo_paginas = numero_resultados / 10
print("Número de páginas: %s" % (maximo_paginas))
# Criando uma variavel para navegar entre pagina, é criar atributo get para ele acessa hrfe
url_pagina = driver.find_element(By.XPATH, "//a[@aria-label='Page 2']").get_attribute("href")
# Ele vai começar na primeira pagina
pagina_atual = 0
# Ele vai pula 10 em 10, porque dentro de 1 pagina do google tem 10 elementos
start = 10
# Vamos criar uma lista
lista_resultado = []
while pagina_atual <= 10:
        # para evitar de pular pagina 2
    if not pagina_atual == 0: 
        # Vou criar variavel que start vai substuir para saber que pagina tá tipo pagina 2 é pagina 1 + 10 = 20 
        url_pagina = url_pagina.replace("start=%s" % start, "start=%s" % (start + 10))
        # ele vai incrementar então ele vai recerber 10
        start = start + 10
    pagina_atual = pagina_atual + 1
    driver.get(url_pagina) 
    # Vou criar variavel que vai ter div=g
    divs = driver.find_elements(By.XPATH, "//*[@id='rso']/div[8]")
    divs = divs + driver.find_elements(By.XPATH, "//div[contains(@class, 'g ')]")
    for div in divs:
        try:
            # Vou criar tag_name tanto para link como para nome, div pq a gente vai pega as informações na variaveavel div
            nome = div.find_element(By.TAG_NAME, "h3") # Tag_name pq encontramos ponto em comum esses a, h3 são tags
            link = div.find_element(By.TAG_NAME, "a")
            # nome.text pq o .text para convernter em texto, é o link vai ter get_atribute pq a gente quer pega atributo hrfe
            resultado = "Title:%s Link:%s" % (nome.text, link.get_attribute("href"))
            print(resultado)
            # Vamos chamar nossa variavel, o .append ele vai adicionar cada titulo é cada link
            lista_resultado.append(resultado)
        except:
            print("Informações não encontradas")

    pagina_atual = pagina_atual + 1
# Agora vamos criar arquivo txt
with open("resultadosrobo.txt", "w") as arquivo:
    # agora vamos criar uma laço para escrever resultado
    for resultado in lista_resultado:
        arquivo.write("%s \n" %resultado)
    arquivo.close()

# Quantos resultados foi escrito é salvo
print("%s resultados encontrados do Google e salvos no arquivo resultado.txt" %len(lista_resultado))