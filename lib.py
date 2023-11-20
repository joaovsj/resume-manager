import tkinter as tk
from reportlab.pdfgen import canvas
from mysql.connector import (connection)

DBhost = "localhost"
DBuser = "root"
DBpassword = ""
DBname = "resumes"

db_conexao = connection.MySQLConnection(host=DBhost,user=DBuser,password=DBpassword,database=DBname)
cursor = db_conexao.cursor()

#  classe referente as transasções do BANCO DE DADOS
class Transaction():

    # pega todos os valores
    def getAll(self):

        command = "SELECT candidates.id,candidates.name, candidates.telephone,candidates.description, grades.interview as interview, grades.theory, grades.practice, grades.softSkill FROM candidates LEFT JOIN grades ON candidates.id = grades.id_candidate"
        cursor.execute(command)
        data = cursor.fetchall()
        return data

    #  insere um valor no banco
    def insert(self, name, telephone, description, interview, theory, practice, softSkill):        

        if name == "" or telephone == "" or description == "" or interview == "" or theory == "" or practice == "" or softSkill == "":
            return False
        else:     

            command = f"INSERT INTO candidates (name, telephone, description) VALUES ('{name}', '{telephone}', '{description}')"
            cursor.execute(command)
            candidate_id = cursor.lastrowid
            self.save()

            command = f"INSERT INTO grades (interview, theory, practice, softSkill, id_candidate) VALUES ('{interview}', '{theory}', '{practice}', '{softSkill}', {candidate_id})"
            cursor.execute(command)
            self.save()
        
    # pega todos dados referente pesquisa 
    def selectSearch(self, interview, theory, practice, softSkill):
        
        if interview == "":
            interview = 0

        if theory == "":
            theory = 0
    
        if practice == "":
            practice = 0
        
        if softSkill == "":
            softSkill = 0

        command = f"SELECT candidates.name, grades.interview  AS entrevista, grades.theory AS teorica, grades.practice AS pratica, grades.softSkill AS softSkill FROM candidates LEFT JOIN grades ON candidates.id = grades.id_candidate WHERE grades.interview >= {interview} AND grades.theory >= {theory} AND grades.practice >= {practice} AND grades.softSkill >= {softSkill}"
        cursor.execute(command)
        data = cursor.fetchall()
        return data

    # pega apenas as notas e o nome referente pesquisa 
    def select(self, interview, theory, practice, softSkill):
        
        if interview == "":
            interview = 0

        if theory == "":
            theory = 0
    
        if practice == "":
            practice = 0
        
        if softSkill == "":
            softSkill = 0

        command = f"SELECT candidates.id, candidates.name, candidates.telephone, candidates.description, grades.interview  AS entrevista, grades.theory AS teorica, grades.practice AS pratica, grades.softSkill AS softSkill FROM candidates LEFT JOIN grades ON candidates.id = grades.id_candidate WHERE grades.interview >= {interview} AND grades.theory >= {theory} AND grades.practice >= {practice} AND grades.softSkill >= {softSkill}"
        cursor.execute(command)
        data = cursor.fetchall()
        return data

    # salva a conexao 
    def save(self):
        db_conexao.commit()
    
    # fecha a conexao 
    def close(self):    
        db_conexao.close()

# classe referente ao PDF
class PDF():
    
    # gera o PDF(dados, titulo no documento, nome do arquivo, indices dentro do documento)
    def generate(self,lista, titulo, nameFile, indices):
        
        nome_pdf = nameFile
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))

        y = 720
        for item in lista:
            y -= 20
            pdf.drawString(10,y, '{}'.format(item))
        pdf.setTitle(nome_pdf)
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(245,750, titulo)
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(10,724, indices)
        pdf.save()

        self.message('PDF criado com sucesso!')

# classe referente a todas as Telas
class Screen(Transaction, PDF): 

    # exibi a primeira janela
    def firstWindow(self):
        self.janela = tk.Tk() 
        self.janela.geometry("500x500")
        label = tk.Label(self.janela, text= "Cadastre os candidatos")
        label.pack(pady=10)

    #  exibi todos os inputs da primeira janela
    def register(self):
        
        label = tk.Label(self.janela, text= "Nome: ")
        label.pack(pady=2)

        self.name = tk.Text(self.janela, height = 1, width = 50)
        self.name.pack(pady=2) 

        label = tk.Label(self.janela, text= "Telefone: ")
        label.pack(pady=2)

        self.telephone = tk.Text(self.janela, height = 1, width = 50)
        self.telephone.pack(pady=2) 

        label = tk.Label(self.janela, text= "Descrição: ")
        label.pack(pady=2)

        self.description = tk.Text(self.janela, height = 1, width = 50)
        self.description.pack(pady=2) 

        label = tk.Label(self.janela, text= "Prova Intrevista: ")
        label.pack(pady=2)

        self.interview = tk.Text(self.janela, height = 1, width = 50)
        self.interview.pack(pady=2) 

        label = tk.Label(self.janela, text= "Prova Teórica: ")
        label.pack(pady=2)

        self.theory = tk.Text(self.janela, height = 1, width = 50)
        self.theory.pack(pady=2) 

        label = tk.Label(self.janela, text= "Prova Prática: ")
        label.pack(pady=2)

        self.practice = tk.Text(self.janela, height = 1, width = 50)
        self.practice.pack(pady=2) 

        label = tk.Label(self.janela, text= "Prova de Soft Skill: ")
        label.pack(pady=2)

        self.softSkill = tk.Text(self.janela, height = 1, width = 50)
        self.softSkill.pack(pady=2) 


        botao1 = tk.Button(self.janela, text='Cadastrar', command=self.take_input)
        botao1.pack(pady=15)

        botao1 = tk.Button(self.janela, text='Procurar Candidatos', command=self.searchCandidates)
        botao1.pack(pady=15)

    # pega os inputs para cadastramento
    def take_input(self):

        nameRegister = self.name.get("1.0", "end-1c")
        telephoneRegister = self.telephone.get("1.0", "end-1c")
        descriptionRegister = self.description.get("1.0", "end-1c")
        interviewRegister = self.interview.get("1.0", "end-1c")
        theoryRegister = self.theory.get("1.0", "end-1c")
        practiceRegister = self.practice.get("1.0", "end-1c")
        softSkillRegister = self.softSkill.get("1.0", "end-1c")

        response = self.insert(nameRegister, telephoneRegister, descriptionRegister, interviewRegister, theoryRegister, practiceRegister, softSkillRegister)

        if response == False:
            self.message("Preencha todos os campos!")
        else:
            self.message("Cadastro realizado com sucesso!")

    # exibi uma mensagem(texto a ser exibido)
    def message(self, subject):
        self.mensagem = tk.Tk()
        self.mensagem.geometry("200x100")

        label = tk.Label(self.mensagem, text=subject)
        label.pack(pady=10)

        botao_voltar = tk.Button(self.mensagem, text="OK", command=self.mensagem.destroy)
        botao_voltar.pack(pady=10)
    
    # cria e exibi a janela de pesquisa
    def searchCandidates(self):

        self.janela2 = tk.Toplevel()
        self.janela2.geometry("500x500")

        label = tk.Label(self.janela2, text= "Procure candidatos")
        label.pack(pady=10)

        label = tk.Label(self.janela2, text= "Prova Intrevista: ")
        label.pack(pady=2)

        self.interview = tk.Text(self.janela2, height = 1, width = 50)
        self.interview.pack(pady=2) 

        label = tk.Label(self.janela2, text= "Prova Teórica: ")
        label.pack(pady=2)

        self.theory = tk.Text(self.janela2, height = 1, width = 50)
        self.theory.pack(pady=2) 

        label = tk.Label(self.janela2, text= "Prova Prática: ")
        label.pack(pady=2)

        self.practice = tk.Text(self.janela2, height = 1, width = 50)
        self.practice.pack(pady=2) 

        label = tk.Label(self.janela2, text= "Prova de Soft Skill: ")
        label.pack(pady=2)

        self.softSkill = tk.Text(self.janela2, height = 1, width = 50)
        self.softSkill.pack(pady=2) 


        botao1 = tk.Button(self.janela2, text='Procurar', command=self.getInputsSearch)
        botao1.pack(pady=15)

        botao2 = tk.Button(self.janela2, text='Gerar Relatório completo', command=self.generateReport)
        botao2.pack(pady=15)

        botao3 = tk.Button(self.janela2, text='Gerar Relatório da pesquisa', command=self.generateReportSearch)
        botao3.pack(pady=15)

        botao_voltar = tk.Button(self.janela2, text="Voltar", command=self.janela2.destroy)
        botao_voltar.pack(pady=10)

    # gera o relatório inteiro
    def generateReport(self):
        data = self.select("", "", "", "")
        self.generate(data, 'Lista de Candidatos', 'TodosCandidatos', 'ID - Nome - Telefone - Descrição - Intrevista - Prova Teórica - Prova Prática - Soft Skill')

    # pega os inputs para exibir todos os dados em uma tela
    def getInputsSearch(self):
        interviewRegister = self.interview.get("1.0", "end-1c")
        theoryRegister = self.theory.get("1.0", "end-1c")
        practiceRegister = self.practice.get("1.0", "end-1c")
        softSkillRegister = self.softSkill.get("1.0", "end-1c")

        data = self.select(interviewRegister, theoryRegister, practiceRegister, softSkillRegister)
        self.showList(data)
    
    # pega os inputs para gerar relatório parcial
    def generateReportSearch(self):

        interviewRegister = self.interview.get("1.0", "end-1c")
        theoryRegister = self.theory.get("1.0", "end-1c")
        practiceRegister = self.practice.get("1.0", "end-1c")
        softSkillRegister = self.softSkill.get("1.0", "end-1c")

        data = self.selectSearch(interviewRegister, theoryRegister, practiceRegister, softSkillRegister)
        self.generate(data, "Lista de Candidatos Referente a Pesquisa", "CandidatosPesquisa", 'Nome - Intrevista - Prova Teórica - Prova Prática - Soft Skill ')

    # exibi os valores referente a pesquisa
    def showList(self, data):
        
        self.janela3 = tk.Tk()
        self.janela3.title("Listbox")
        self.janela3.geometry('600x600')

        lengthData = len(data)
        
        for i in range(len(data)):

            label = tk.Label(self.janela3, text="Nome: ")
            label.grid(row=i, column=1, pady = 2)

            label = tk.Label(self.janela3, text=data[i][1])
            label.grid(row=i, column=2, pady = 2)

            label = tk.Label(self.janela3, text="Nota de Entrevista: ")
            label.grid(row=i, column=3, pady = 2)

            label = tk.Label(self.janela3, text=data[i][4])
            label.grid(row=i, column=4, pady = 2)

            label = tk.Label(self.janela3, text="Prova Teórica: ")
            label.grid(row=i, column=5, pady = 2)

            label = tk.Label(self.janela3, text=data[i][5])
            label.grid(row=i, column=6, pady = 2)

            label = tk.Label(self.janela3, text="Prova Prática: ")
            label.grid(row=i, column=7, pady = 2)

            label = tk.Label(self.janela3, text=data[i][6])
            label.grid(row=i, column=8, pady = 2)

            label = tk.Label(self.janela3, text="Soft Skill: ")
            label.grid(row=i, column=9, pady = 2)

            label = tk.Label(self.janela3, text=data[i][7])
            label.grid(row=i, column=10, pady = 2)

    # carrega janela completa
    def close(self):
        self.janela.mainloop()
    