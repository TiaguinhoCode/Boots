from selenium import webdriver # Vai abrir drive do google do drive vai permite que nosso robo acessa internet
from selenium.webdriver.common.keys import Keys # Biblioteca que vai da acessor ao nosso teclado e mouse sem a gente precisar move um dedo
from selenium.webdriver.common.by import By
import time
import xlrd # Biblioteca que vai ler nosso arquivo no excel

workbook = xlrd.open_workbook(r'E:\Tiago Backup\Progamas Em Python\Curso de Boot\excel.xls') # Comando para acessar nosso arquivo em excel, esse r é um rString para aceita caracteries expecial
sheet = workbook.sheet_by_name('Plan1') # Variavel resposanvel para abrir qual pagina da planilha 
rows = sheet.nrows # Variavel para contagem de número de linhas
columns =  sheet.ncols # Variavel para contagem de número de colunas

options = webdriver.ChromeOptions()
options.add_argument("--disable-logging") 
options.add_argument("--log-level=3")


# Vou criar variavel onde vou mostra o maquina onde deixei chormedrive
driver = webdriver.Chrome('E:/Tiago Backup/Progamas Em Python/Curso de Boot/chromedriver', options=options)
# Agora ele vai pega o site que eu quero acessar 
driver.get("https://registro.br")

print("Iniciando robo")
# Criando arquivo tanto txt como word é o w e o Write "Escrever"
arq = open("resultado.txt", "w")
for curr_row in range(0, rows):
    x = sheet.cell_value(curr_row, 0)
    # Fazer computador clikar na barra de pesquisa, ele vai pega id do site
    pesquisa = driver.find_element(By.ID ,"is-avail-field") 
    time.sleep(2)
    # Tiver qual quer coisa escrita ele vai limpa
    pesquisa.clear()
    time.sleep(2)
    pesquisa.send_keys(x)
    time.sleep(2)
    # Esse comando agente vai manda computador digita "Enter"
    pesquisa.send_keys(Keys.RETURN)
    # Tempo de pesquisar
    time.sleep(2)
    # Caminho do código do navegador que ele vai pega no xpath
    driver.find_element(By.XPATH ,'//*[@id="app"]/main/section/div[2]/div/p/span/strong')
    time.sleep(2)
    # Escrever qual dominio não estar disponivel, %s é para declara uma variavel é outro para dizer se tá disponivel ou não
    # È o % para definir qual valores é como ser fosser um format
    texto = "Dominio %s %s\n" %(x, driver.find_element(By.XPATH ,'//*[@id="app"]/main/section/div[2]/div/p/span/strong').text)
    # arquivo que ele vai escrever
    arq.write(texto)
# Fechar o arquivo
arq.close()
print('=-' * 30)

# Tempo para fechar a maquina
print("Fechando robo")
driver.close()