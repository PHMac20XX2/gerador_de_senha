import time
from random import choice
import string

print ("Gerador de Senha by PHMac20XX2")

def pull():
    print("")

pull()

t_senha = int(input("Quantidade de Caracteres: "))
carac = string.ascii_letters + string.digits + string.punctuation
sec_senha = ''
for i in range(t_senha):
    sec_senha += choice (carac)

print("Gerando senha...")
time.sleep(1.5)
print(f'''
             Senha Gerada!
                ( {sec_senha} )          ''')


