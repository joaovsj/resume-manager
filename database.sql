DROP DATABASE IF EXISTS resumes;

CREATE DATABASE resumes;
USE resumes;

CREATE TABLE candidates(

	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(255),
	telephone BIGINT(14),
	description VARCHAR(255)
);


CREATE TABLE grades(
	id INT PRIMARY KEY AUTO_INCREMENT,	
	interview INT(2),
	theory INT(2),
	practice INT(2),
	softkill INT(2),
	id_candidate INT,
	FOREIGN KEY(id_candidate) REFERENCES candidates(id)
);


/*
	GET METHOD 
*/

SELECT 
    candidates.id,
    candidates.name, 
    candidates.telehone,
    candidates.description,
    grades.interview, 
    grades.theory, 
    grades.practice, 
    grades.softkill 
FROM 
    candidates 
LEFT JOIN grades 
ON candidates.id = grades.id_candidate;
