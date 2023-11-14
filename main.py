
 
# importar do arquivo como DB
from lib import Transaction, Screen

db = Transaction()
screen = Screen()

screen.firstWindow()
screen.register()

screen.close()


# def exibir_mensagem():
#     label.config(text="Ola, mundo!")
 


# def abrir_janela():

#     janela2 = tk.Toplevel()
#     janela2.geometry("300x200")

#     label = tk.Label(janela2, text= "Cadastro realizado com sucesso!")
#     label.pack(pady=10)

#     botao_voltar = tk.Button(janela2, text="OK", command=janela2.destroy)
#     botao_voltar.pack(pady=10)


# def searchCandidates():

#     janela3 = tk.Toplevel()
#     janela3.geometry("500x500")

#     label = tk.Label(janela3, text= "Procure candidatos")
#     label.pack(pady=10)

#     showInputsCandidates(janela3)

#     botao_voltar = tk.Button(janela3, text="Voltar", command=janela3.destroy)
#     botao_voltar.pack(pady=10)

# def showInputsCandidates(janela3):
    
#     ###################################################
#     label = tk.Label(janela3, text= "Prova Intrevista: ")
#     label.pack(pady=2)

#     interviewSearch = tk.Text(janela3, height = 1, width = 10)
#     interviewSearch.pack(pady=2) 
#     interview_search = interviewSearch.get("1.0", "end-1c")

#     ###################################################
#     label = tk.Label(janela3, text= "Prova Teórica: ")
#     label.pack(pady=2)

#     theorySearch = tk.Text(janela3, height = 1, width = 10)
#     theorySearch.pack(pady=2) 
#     theory_search = theorySearch.get("1.0", "end-1c")


#     ###################################################
#     label = tk.Label(janela3, text= "Prova Prática: ")
#     label.pack(pady=2)

#     practiceSearch = tk.Text(janela3, height = 1, width = 10)
#     practiceSearch.pack(pady=2) 
#     practice_search = practiceSearch.get("1.0", "end-1c")

#     ###################################################
#     label = tk.Label(janela3, text= "Prova de Soft Skill: ")
#     label.pack(pady=2)

#     softSkillSearch = tk.Text(janela3, height = 1, width = 10)
#     softSkillSearch.pack(pady=2) 
#     softSkill_search = softSkillSearch.get("1.0", "end-1c")


#     botao_buscar = tk.Button(janela3, text="Buscar", command=lambda:takeInputsSearch(interview_search, theory_search, practice_search, softSkill_search))
#     botao_buscar.pack(pady=10)

# def takeInputsSearch(interview_search, theory_search, practice_search, softSkill_search):
    # print(interview_search, theory_search, practice_search, softSkill_search)



 
# botao2 = tk.Button(janela, text="Ir para nova janela", command=abrir_janela)
# botao2.pack(pady=17)
 


# dados = db.getAll()
# print(dados)

# INSERT 
# db.insert("carlinhos", "15999888777", "Lorem Ipsum is simply dummy text", 5,8,10,6)

# interview =  int(input("Qual nota necessária da entrevista: "))
# theory    =  int(input("Qual nota necessária da prova teórica: "))
# practice  =  int(input("Qual nota necessária da prova prática: "))
# softSkill  =  int(input("Qual nota necessária das Soft Skill: "))


# person = db.select(interview, theory, practice, softSkill)
# print(person)