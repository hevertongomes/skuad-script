from urllib.request import urlretrieve as retrive
from random import randint

print('Insira um data no formato - YYYYMM: ')
data = input()

url = 'http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_'+data+'.csv'


retrive(url, 'dados.csv')