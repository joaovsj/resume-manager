import tkinter as tk
from mysql.connector import (connection)


DBhost = "localhost"
DBuser = "root"
DBpassword = ""
DBname = "resumes"


db_conexao = connection.MySQLConnection(host=DBhost,user=DBuser,password=DBpassword,database=DBname)
cursor = db_conexao.cursor()


class Transaction():


    def getAll(self):

        command = "SELECT candidates.id,candidates.name, candidates.telephone,candidates.description, grades.interview as interview, grades.theory, grades.practice, grades.softSkill FROM candidates LEFT JOIN grades ON candidates.id = grades.id_candidate"
        cursor.execute(command)
        data = cursor.fetchall()
        return data

    def insert(self,name, telephone, description, interview, theory, practice, softSkill):        

        command = f"INSERT INTO candidates (name, telephone, description) VALUES ('{name}', '{telephone}', '{description}')"
        cursor.execute(command)
        candidate_id = cursor.lastrowid
        self.save()

        command = f"INSERT INTO grades (interview, theory, practice, softSkill, id_candidate) VALUES ('{interview}', '{theory}', '{practice}', '{softSkill}', {candidate_id})"
        cursor.execute(command)
        self.save()
        
    def select(self, interview, theory, practice, softSkill):
        
        command = f"SELECT candidates.id, candidates.name, candidates.telephone, candidates.description, grades.interview as interview, grades.theory, grades.practice, grades.softSkill FROM candidates LEFT JOIN grades ON candidates.id = grades.id_candidate WHERE grades.interview >= {interview} AND grades.theory >= {theory} AND grades.practice >= {practice} AND grades.softSkill >= {softSkill}"
        cursor.execute(command)
        data = cursor.fetchall()
        return data
            
    def save(self):
        db_conexao.commit()
    
    def close(self):    
        db_conexao.close()


# janela = tk.Tk()
# janela.geometry("500x500")
# label = tk.Label(janela, text= "Cadastre os candidatos")
# label.pack(pady=10)

class Screen(Transaction): 

    def firstWindow(self):
        self.janela = tk.Tk() 
        self.janela.geometry("500x500")
        label = tk.Label(self.janela, text= "Cadastre os candidatos")
        label.pack(pady=10)


    def register(self):
        ###################################################
        label = tk.Label(self.janela, text= "Nome: ")
        label.pack(pady=2)

        self.name = tk.Text(self.janela, height = 1, width = 10)
        self.name.pack(pady=2) 

        ###################################################
        label = tk.Label(self.janela, text= "Telefone: ")
        label.pack(pady=2)

        self.telephone = tk.Text(self.janela, height = 1, width = 10)
        self.telephone.pack(pady=2) 

        ###################################################
        label = tk.Label(self.janela, text= "Descrição: ")
        label.pack(pady=2)

        self.description = tk.Text(self.janela, height = 1, width = 10)
        self.description.pack(pady=2) 

        ###################################################
        label = tk.Label(self.janela, text= "Prova Intrevista: ")
        label.pack(pady=2)

        self.interview = tk.Text(self.janela, height = 1, width = 10)
        self.interview.pack(pady=2) 


        ###################################################
        label = tk.Label(self.janela, text= "Prova Teórica: ")
        label.pack(pady=2)

        self.theory = tk.Text(self.janela, height = 1, width = 10)
        self.theory.pack(pady=2) 


        ###################################################
        label = tk.Label(self.janela, text= "Prova Prática: ")
        label.pack(pady=2)

        self.practice = tk.Text(self.janela, height = 1, width = 10)
        self.practice.pack(pady=2) 


        ###################################################
        label = tk.Label(self.janela, text= "Prova de Soft Skill: ")
        label.pack(pady=2)

        self.softSkill = tk.Text(self.janela, height = 1, width = 10)
        self.softSkill.pack(pady=2) 


        botao1 = tk.Button(self.janela, text='Cadastrar', command=self.take_input)
        botao1.pack(pady=15)

        botao1 = tk.Button(self.janela, text='Procurar Candidatos', command=self.searchCandidates)
        botao1.pack(pady=15)


        # botao1 = tk.Button(janela, text='Procurar candidatos', command=searchCandidates)
        # botao1.pack(pady=15)

    def take_input(self):

        nameRegister = self.name.get("1.0", "end-1c")
        telephoneRegister = self.telephone.get("1.0", "end-1c")
        descriptionRegister = self.description.get("1.0", "end-1c")
        interviewRegister = self.interview.get("1.0", "end-1c")
        theoryRegister = self.theory.get("1.0", "end-1c")
        practiceRegister = self.practice.get("1.0", "end-1c")
        softSkillRegister = self.softSkill.get("1.0", "end-1c")

        self.insert(nameRegister, telephoneRegister, descriptionRegister, interviewRegister, theoryRegister, practiceRegister, softSkillRegister)
        # abrir_janela()


    def close(self):
        self.janela.mainloop()

    
    def searchCandidates(self):

        self.janela2 = tk.Toplevel()
        self.janela2.geometry("500x500")

        label = tk.Label(self.janela2, text= "Procure candidatos")
        label.pack(pady=10)

        ###################################################
        label = tk.Label(self.janela2, text= "Prova Intrevista: ")
        label.pack(pady=2)

        self.interview = tk.Text(self.janela2, height = 1, width = 10)
        self.interview.pack(pady=2) 


        ###################################################
        label = tk.Label(self.janela2, text= "Prova Teórica: ")
        label.pack(pady=2)

        self.theory = tk.Text(self.janela2, height = 1, width = 10)
        self.theory.pack(pady=2) 


        ###################################################
        label = tk.Label(self.janela2, text= "Prova Prática: ")
        label.pack(pady=2)

        self.practice = tk.Text(self.janela2, height = 1, width = 10)
        self.practice.pack(pady=2) 


        ###################################################
        label = tk.Label(self.janela2, text= "Prova de Soft Skill: ")
        label.pack(pady=2)

        self.softSkill = tk.Text(self.janela2, height = 1, width = 10)
        self.softSkill.pack(pady=2) 


        botao1 = tk.Button(self.janela2, text='Procurar', command=self.getInputsSearch)
        botao1.pack(pady=15)

        botao_voltar = tk.Button(self.janela2, text="Voltar", command=self.janela2.destroy)
        botao_voltar.pack(pady=10)


    def getInputsSearch(self):
        interviewRegister = self.interview.get("1.0", "end-1c")
        theoryRegister = self.theory.get("1.0", "end-1c")
        practiceRegister = self.practice.get("1.0", "end-1c")
        softSkillRegister = self.softSkill.get("1.0", "end-1c")

        data = self.select(interviewRegister, theoryRegister, practiceRegister, softSkillRegister)
        self.showList(data)
        


    def showList(self, data):
        
        self.janela3 = tk.Tk()
        self.janela3.title("Listbox")
        self.janela3.geometry('250x250')

        lb = tk.Listbox(self.janela3, height=3)
        lb.grid(row=0, column=0)

        # print(data)
        for i in range(len(data)):
            lb.insert(i, data[i])
            # print(data[i])

        # for i in data:           
        #     print(data[i])
            # person = data[i]
            # print(f"person \n")
           

    

    