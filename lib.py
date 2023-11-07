from mysql.connector import (connection)


DBhost = "localhost"
DBuser = "root"
DBpassword = ""
DBname = "resumes"


db_conexao = connection.MySQLConnection(host=DBhost,user=DBuser,password=DBpassword,database=DBname)
cursor = db_conexao.cursor()


class Transaction():


    def getAll(self):

        cursor.execute("SELECT candidates.id,candidates.name, candidates.telephone,candidates.description, grades.interview as interview, grades.theory, grades.practice, grades.softkill FROM candidates LEFT JOIN grades ON candidates.id = grades.id_candidate")
        dados = cursor.fetchall()
        return dados

    def insert(self,name, telephone, description, interview, theory, practice, softkill):        

        command = f"INSERT INTO candidates (name, telephone, description) VALUES ('{name}', '{telephone}', '{description}')"
        cursor.execute(command)
        candidate_id = cursor.lastrowid
        self.save()

        command = f"INSERT INTO grades (interview, theory, practice, softkill, id_candidate) VALUES ('{interview}', '{theory}', '{practice}', '{softkill}', {candidate_id})"
        cursor.execute(command)
        self.save()

    def save(self):
        db_conexao.commit()
    
    def close(self):    
        db_conexao.close()




    