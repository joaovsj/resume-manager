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
        
        command = f"SELECT candidates.id, candidates.name, candidates.telephone, candidates.description, grades.interview as interview, grades.theory, grades.practice, grades.softSkill FROM candidates LEFT JOIN grades ON candidates.id = grades.id_candidate" 
        data = cursor.execute(command)
        print(data) 
        exit()
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



    

    