from mysql.connector import (connection)


DBhost = "localhost"
DBuser = "root"
DBpassword = ""
DBname = "resumes"


db_conexao = connection.MySQLConnection(host=DBhost,user=DBuser,password=DBpassword,database=DBname)
cursor = db_conexao.cursor()


class Transaction():


    def getAll(self):

        command = "SELECT candidates.id,candidates.name, candidates.telephone,candidates.description, grades.interview as interview, grades.theory, grades.practice, grades.softkill FROM candidates LEFT JOIN grades ON candidates.id = grades.id_candidate"
        cursor.execute(command)
        dados = cursor.fetchall()
        return dados

    def insert(self,name, telephone, description, interview, theory, practice, softkill):        

        try: 

            command = f"INSERT INTO candidates (name, telephone, description) VALUES ('{name}', '{telephone}', '{description}')"
            cursor.execute(command)
            candidate_id = cursor.lastrowid
            self.save()

            command = f"INSERT INTO grades (interview, theory, practice, softkill, id_candidate) VALUES ('{interview}', '{theory}', '{practice}', '{softkill}', {candidate_id})"
            cursor.execute(command)
            self.save()

        except Error:
            print("Ocorreu um ao executar a ação") 
        
    def select(self, interview, theory, practice, softSkill):
        
        try:
            command = f"SELECT candidates.id,candidates.name, candidates.telephone,candidates.description, grades.interview as interview, grades.theory, grades.practice, grades.softkill FROM candidates LEFT JOIN grades ON candidates.id = grades.id_candidate" 
            
        except Error:
            print("Ocorreu um ao executar a ação") 



    def save(self):
        db_conexao.commit()
    
    def close(self):    
        db_conexao.close()




    