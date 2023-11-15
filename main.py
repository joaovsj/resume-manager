# importar do arquivo como DB
from lib import Transaction, Screen, PDF

db = Transaction()
screen = Screen()
pdf = PDF()


screen.firstWindow()  # abre a primeira janela
screen.register()     # exibi os inputs do registro 


# lista = {'Rafaela': '19', 'Jose': '15', 'Maria': '22','Eduardo':'24'}

# pdf.generate(lista)

screen.close() 