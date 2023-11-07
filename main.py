# importar do arquivo como DB
from lib import Transaction

db = Transaction()

# dados = db.getAll()
# print(dados)

db.insert("pedrão", "15999888777", "Lorem Ipsum is simply dummy text", 5,8,10,6)

