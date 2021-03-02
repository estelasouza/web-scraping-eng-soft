from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
"""
   Script feito para cadeira de engenharia de software 
"""

def getUsingUrl():
   """Essa função vai rodar o html que tem os dados com as informações que a gnt precisa 
   no arquivo index.html  
   ( usei a extensão do vscode live server)
   dai ela roda o html na porta 5500"""
   html = urlopen("http://127.0.0.1:5500/")
   bs = BeautifulSoup(html, 'html.parser')
   run(bs)

def getUsingHtmlFile(filePath):
   #Aqui abre um arquivo local, caso queira para testes.
   with open(filePath) as fp:
      bs = BeautifulSoup(fp, 'html.parser')
      print(bs)
      run(bs)

def run(bs):
   """ 
   A função run vai buscar as tags que precisamos para montar nosso csv 
   e extrair as informações contidas nessas tags
   """
   cont = 0 #esse contador vai servir para pegar os valores da variavel "concorda"
   concorda = bs.findAll('span',{'class':''}) 
   script_json = [] #irá armazenar uma lista de json com informações dos alunos 
   dataframe = {} #irá armazenar os valores para criar as linhas do csv 
   value = ''
   #esse for vai pegar o nome de todos os alunos que responderam e atividade e add o valor 1 para as respostas
   # e também vai pegar a quantidade de concorda, caso ninguém tenha concordado ele atribui um valor default 
   for author in bs.findAll('div',{'class':'author'}):
      dataframe = {}
      value = concorda[cont].text.strip()
      cont += 1
      if len(value) > 9:
         
         dataframe["nome"] = author.text.strip()
         dataframe["resp"] = "1"
         dataframe["conc"] = value[9:]
      else:
         dataframe["nome"] = author.text.strip()
         dataframe["resp"] = "1"
         dataframe["conc"] = "999999"

      script_json.append(dataframe)
   #cria o dataframe
   df = pd.DataFrame(script_json)

   #gera o arquivo .csv 
   df.to_csv('questao_1_inv_emp.csv')
   


# getUsingHtmlFile('index.html')
getUsingUrl()

## proximos passos :
# concatenar os csv de cada questão do dona deda 
# colocar na planilha do professor as pessoas que responderam a atividade 

#o que pode otimizar mais :

   # melhorar a forma de pegar os dados lá na plataforma 
   # (pq temos que ir em cada questão do kit carregar todos os comentários e após isso colocar em um html pra pegar as informações que precisamos)