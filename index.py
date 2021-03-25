import csv
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
   with open(filePath,newline="") as fp:
      bs = BeautifulSoup(fp, 'html.parser')
      print(bs)
      run(bs)

def run(bs):
    """ 
    A função run vai buscar as tags que precisamos para montar nosso csv 
    e extrair as informações contidas nessas tags
    """



    file = open('Planilha de ES.csv', 'w',newline="")   #abre o arquivo
    writer = csv.writer(file,delimiter=',')             #inicializa o writer
    
    writer.writerow(["sep=,"])                          #colunas serao separadas por virgulas
    writer.writerow(['Aluno', 'Respostas', 'Curtidas']) #poe o titulo em cada coluna
    

    cont = 0 #esse contador vai servir para pegar os valores da variavel "concorda"
    concorda = bs.findAll('span',{'class':''}) 
    script_json = [] #irá armazenar uma lista de json com informações dos alunos 
    dataframe = {} #irá armazenar os valores para criar as linhas do csv 
    value = ''
   
   #esse for vai pegar o nome de todos os alunos que responderam e atividade e add o valor 1 para as respostas
   # e também vai pegar a quantidade de concorda, caso ninguém tenha concordado ele atribui um valor default 
    #inicializa uma variavel para me auxiliar a guardar indicies
    i=0
    #inicializa as listas
    curtidas = []
    autor = []
    respostas = []
    for author in bs.findAll('div',{'class':'author'}):
        dataframe = {}
        value = concorda[cont].text.strip()
        cont += 1
        if len(value) > 9:
         
            dataframe["nome"] = author.text.strip()
            dataframe["resp"] = 1
            dataframe["conc"] = int(value[12:len(value)-1])
        else:
            dataframe["nome"] = author.text.strip()
            dataframe["resp"] = 1
            dataframe["conc"] = 0

        

        jatem = False               #essa variavel serve para checar se o aluno ja tem uma resposta
        for nome in range(len(autor)):
            if dataframe["nome"]==autor[nome]: jatem=True                   #encontrou um repetido
            i = nome                                                        #salvar o indice para aumentar as curtidas
        if jatem:
            #print("repetido ->" + dataframe["nome"])
            curtidas[i] += dataframe["conc"]    #soma a quantidade de curtidas de todas as suas respostas
            respostas[i] += 1                   #aumenta a quantidade de respostas que o aluno escreveu
        else:
            #se o aluno ainda nao tiver comentado, salva o comentario dele na lista
            curtidas.append(dataframe["conc"])      
            autor.append(dataframe["nome"])
            respostas.append(dataframe["resp"])
            
    
    
    #cria o csv com os dados armazenados na lista 
    for a in range (len(autor)):    
        writer.writerow([ autor[a], respostas[a], curtidas[a] ])

    #fecha o arquivo
    file.close
    

   


# getUsingHtmlFile('index.html')

 
getUsingUrl()

## proximos passos :
# concatenar os csv de cada questão do dona deda 
# colocar na planilha do professor as pessoas que responderam a atividade 

#o que pode otimizar mais :

   # melhorar a forma de pegar os dados lá na plataforma 
   # (pq temos que ir em cada questão do kit carregar todos os comentários e após isso colocar em um html pra pegar as informações que precisamos)
