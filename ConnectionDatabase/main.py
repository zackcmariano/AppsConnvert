import sqlite3


TABLE1 = 'EMPREGADO'
TABLE2 = 'EMPREGADO_ENDERECO'

NOME = ''
SEXO = ''
IDADE = ''
DATA_CRIACAO = ''
SALARIO = ''

LOGRADO = ''
NUMERO = ''
BAIRRO = ''
CIDADE = ''
CEP = ''


banco = sqlite3.connect('DB _Prova.sqlite3')
cursor = banco.cursor()

def consult():
    cursor.execute('SELECT * FROM '+TABLE1+' ')
    print(cursor.fetchall())
    cursor.execute('SELECT * FROM '+TABLE2+' ')
    print(cursor.fetchall())

def insert_empregado():
    cursor.execute('INSERT INTO '+TABLE1+' VALUES('+NOME+', '+SEXO+', '+str(IDADE)+', '+str(DATA_CRIACAO)+', '+str(SALARIO)+')')

def insert_empregado_endereco():
    cursor.execute('INSERT INTO '+TABLE1+' VALUES('+str(LOGRADO)+', '+str(NUMERO)+','+BAIRRO+', '+CIDADE+', '+str(CEP)+')')