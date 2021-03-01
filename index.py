from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
"""
   Script feito para cadeira de engenharia de software 
"""
#rodar a parte do html que a gente precisa pegar na maquina ( usei a extensão do vscode live server)
#dai ela roda o html na porta 5500
html = urlopen("http://127.0.0.1:5500/")
bs = BeautifulSoup(html, 'html.parser')

#essas listas vão servir pra criar as linhas do csv //
#nome do aluno- string, resp - 1 (só tem os alunos que fizeram a atividade)
#conc -> int (quantidade de pessoas que concordaram com a resposta) // o valor default é 99999 pq na hora de criar o dataset as colunas precisam ter o msm num de linhas 

nome = []
resp = []
conc = []

#esse for vai pegar o nome de todos os alunos que responderam a atividade e add o valor 1 pra futura coluna resposta
for author in bs.findAll('div',{'class':'author'}):
   nome.append(author.text.strip())
   resp.append('1')

#esse for vai colocar o num de curtidas em cada resposta ( a class tem q ser vazia pra ele não pegar outras tags span naquela parte do código )
for concord in bs.findAll('span',{'class':''}):
   if len(concord.text.strip()) > 9:
      conc.append(concord.text.strip()[9:])
   else: 
      conc.append('99999999')

# print(conc)
# print(resp)
#cria o dataframe
df = pd.DataFrame({'Nome':nome,'Resp':resp,'Conc':conc})

#gera o arquivo .csv 
df.to_csv('questao_1_inv_emp.csv')


## proximos passos :
# concatenar os csv de cada questão do dona deda 
# colocar na planilha do professor as pessoas que responderam a atividade 

#o que pode otimizar mais :

   # melhorar a forma de pegar os dados lá na plataforma 
   # (pq temos que ir em cada questão do kit carregar todos os comentários e após isso colocar em um html pra pegar as informações que precisamos)