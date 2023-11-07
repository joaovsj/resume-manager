# importar do arquivo como DB
from lib import Transaction

db = Transaction()

# dados = db.getAll()
# print(dados)

# INSERT 
db.insert("pedrão", "15999888777", "Lorem Ipsum is simply dummy text", 5,8,10,6)

interview =  int(input("Qual nota necessária da entrevista: "))
theory    =  int(input("Qual nota necessária da prova teórica: "))
practice  =  int(input("Qual nota necessária da prova prática: "))
softkill  =  int(input("Qual nota necessária das Soft Skill: "))


db.select(interview, theory, practice, softSkill)