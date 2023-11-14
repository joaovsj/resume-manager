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





    