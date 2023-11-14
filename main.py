import tkinter as tk
 
# importar do arquivo como DB
from lib import Transaction

db = Transaction()

def exibir_mensagem():
    label.config(text="Ola, mundo!")
 
# def abrir_janela():

#     janela2 = tk.Toplevel()
#     janela2.geometry("300x200")

#     label = tk.Label(janela2, text= "Cadastro realizado com sucesso!")
#     label.pack(pady=10)

#     botao_voltar = tk.Button(janela2, text="OK", command=janela2.destroy)
#     botao_voltar.pack(pady=10)


def searchCandidates():

    janela3 = tk.Toplevel()
    janela3.geometry("500x500")

    label = tk.Label(janela3, text= "Procure candidatos")
    label.pack(pady=10)

    showInputsCandidates(janela3)

    botao_voltar = tk.Button(janela3, text="Voltar", command=janela3.destroy)
    botao_voltar.pack(pady=10)

def showInputsCandidates(janela3):
    
    ###################################################
    label = tk.Label(janela3, text= "Prova Intrevista: ")
    label.pack(pady=2)

    interviewSearch = tk.Text(janela3, height = 1, width = 10)
    interviewSearch.pack(pady=2) 


    ###################################################
    label = tk.Label(janela3, text= "Prova Teórica: ")
    label.pack(pady=2)

    theorySearch = tk.Text(janela3, height = 1, width = 10)
    theorySearch.pack(pady=2) 


    ###################################################
    label = tk.Label(janela3, text= "Prova Prática: ")
    label.pack(pady=2)

    practiceSearch = tk.Text(janela3, height = 1, width = 10)
    practiceSearch.pack(pady=2) 


    ###################################################
    label = tk.Label(janela3, text= "Prova de Soft Skill: ")
    label.pack(pady=2)

    softSkillSearch = tk.Text(janela3, height = 1, width = 10)
    softSkillSearch.pack(pady=2) 


    botao_buscar = tk.Button(janela3, text="Buscar", command=takeInputsSearch)
    botao_buscar.pack(pady=10)

def takeInputsSearch():
    
    interview_search = interviewSearch.get("1.0", "end-1c")
    theory_search = theorySearch.get("1.0", "end-1c")
    practice_search = practiceSearch.get("1.0", "end-1c")
    softSkill_search = softSkillSearch.get("1.0", "end-1c")

    print(interview_search, theory_search, practice_search, softSkill_search)

def take_input():
    nameRegister = name.get("1.0", "end-1c")
    telephoneRegister = telephone.get("1.0", "end-1c")
    descriptionRegister = description.get("1.0", "end-1c")
    interviewRegister = interview.get("1.0", "end-1c")
    theoryRegister = theory.get("1.0", "end-1c")
    practiceRegister = practice.get("1.0", "end-1c")
    softSkillRegister = softSkill.get("1.0", "end-1c")

    db.insert(nameRegister, telephoneRegister, descriptionRegister, interviewRegister, theoryRegister, practiceRegister, softSkillRegister)
    abrir_janela()


janela = tk.Tk()
# make a window
janela.geometry("500x500")
label = tk.Label(janela, text= "Cadastre os candidatos")
label.pack(pady=10)

###################################################
label = tk.Label(janela, text= "Nome: ")
label.pack(pady=2)

name = tk.Text(janela, height = 1, width = 10)
name.pack(pady=2) 

###################################################
label = tk.Label(janela, text= "Telefone: ")
label.pack(pady=2)

telephone = tk.Text(janela, height = 1, width = 10)
telephone.pack(pady=2) 

###################################################
label = tk.Label(janela, text= "Descrição: ")
label.pack(pady=2)

description = tk.Text(janela, height = 1, width = 10)
description.pack(pady=2) 

###################################################
label = tk.Label(janela, text= "Prova Intrevista: ")
label.pack(pady=2)

interview = tk.Text(janela, height = 1, width = 10)
interview.pack(pady=2) 


###################################################
label = tk.Label(janela, text= "Prova Teórica: ")
label.pack(pady=2)

theory = tk.Text(janela, height = 1, width = 10)
theory.pack(pady=2) 


###################################################
label = tk.Label(janela, text= "Prova Prática: ")
label.pack(pady=2)

practice = tk.Text(janela, height = 1, width = 10)
practice.pack(pady=2) 


###################################################
label = tk.Label(janela, text= "Prova de Soft Skill: ")
label.pack(pady=2)

softSkill = tk.Text(janela, height = 1, width = 10)
softSkill.pack(pady=2) 


botao1 = tk.Button(janela, text='Cadastrar', command=take_input)
botao1.pack(pady=15)

botao1 = tk.Button(janela, text='Procurar candidatos', command=searchCandidates)
botao1.pack(pady=15)


 
# botao2 = tk.Button(janela, text="Ir para nova janela", command=abrir_janela)
# botao2.pack(pady=17)
 
janela.mainloop()

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