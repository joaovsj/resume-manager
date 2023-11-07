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
	softSkill INT(2),
	id_candidate INT,
	FOREIGN KEY(id_candidate) REFERENCES candidates(id)
);

/*
	REGISTERS
*/

insert into candidates (name, telephone, description) values ('Becky Peegrem', '2317857230', 'dignissim vestibulum vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae nulla dapibus');
insert into candidates (name, telephone, description) values ('Gracia Lygoe', '2114995032', 'a ipsum integer a nibh in quis justo maecenas rhoncus');
insert into candidates (name, telephone, description) values ('Jasmin Hastings', '4516675712', 'aenean sit amet justo morbi ut odio cras mi pede malesuada in imperdiet et commodo vulputate justo in blandit ultrices');
insert into candidates (name, telephone, description) values ('Nessy Bagenal', '6051260676', 'sit amet sem fusce consequat nulla nisl nunc nisl duis bibendum felis sed interdum venenatis turpis enim blandit');
insert into candidates (name, telephone, description) values ('Randal Blything', '42416682020', 'pede lobortis ligula sit amet eleifend pede libero quis orci nullam molestie nibh in lectus');
insert into candidates (name, telephone, description) values ('Cedric Chinge', '7113059606', 'rhoncus aliquet pulvinar sed nisl nunc rhoncus dui vel sem sed sagittis nam');
insert into candidates (name, telephone, description) values ('Boone Gotcliff', '48425660709', 'nibh ligula nec sem duis aliquam convallis nunc proin at turpis a pede posuere nonummy');
insert into candidates (name, telephone, description) values ('Osbourn Defraine', '98489386349', 'orci pede venenatis non sodales sed tincidunt eu felis fusce posuere felis sed lacus morbi');
insert into candidates (name, telephone, description) values ('Giffard Robard', '28499378739', 'elementum in hac habitasse platea dictumst morbi vestibulum velit id pretium');
insert into candidates (name, telephone, description) values ('Arron Stuckford', '61468525649', 'auctor sed tristique in tempus sit amet sem fusce consequat nulla nisl nunc nisl duis bibendum felis sed');
insert into candidates (name, telephone, description) values ('Kalli Seggie', '93436902509', 'luctus et ultrices posuere cubilia curae duis faucibus accumsan odio');
insert into candidates (name, telephone, description) values ('Dewie Allaway', '254627414', 'fusce congue diam id ornare imperdiet sapien urna pretium nisl ut volutpat');
insert into candidates (name, telephone, description) values ('Mellie Canadas', '11499541509', 'lobortis convallis tortor risus dapibus augue vel accumsan tellus nisi eu');
insert into candidates (name, telephone, description) values ('Norrie Oherlihy', '20467916459', 'morbi ut odio cras mi pede malesuada in imperdiet et commodo vulputate justo in');
insert into candidates (name, telephone, description) values ('Allsun Drysdall', '74435171659', 'dolor vel est donec odio justo sollicitudin ut suscipit a feugiat et');
insert into candidates (name, telephone, description) values ('Douglass Cooke', '14439334189', 'bibendum felis sed interdum venenatis turpis enim blandit mi in');
insert into candidates (name, telephone, description) values ('Zsa zsa Cannavan', '42474039979', 'enim in tempor turpis nec euismod scelerisque quam turpis adipiscing lorem vitae mattis nibh');
insert into candidates (name, telephone, description) values ('Kristal Gurley', '34413616399', 'sit amet turpis elementum ligula vehicula consequat morbi a ipsum integer a nibh in quis');
insert into candidates (name, telephone, description) values ('Caritta Sealeaf', '69434603969', 'nisl nunc rhoncus dui vel sem sed sagittis nam congue risus semper porta volutpat quam pede lobortis');
insert into candidates (name, telephone, description) values ('Jodi Sappson', '23451662069', 'tincidunt in leo maecenas pulvinar lobortis est phasellus sit amet erat nulla tempus');

insert into grades (interview, theory, practice, softSkill, id_candidate ) values (12, 8, 8, 1, 1);
insert into grades (interview, theory, practice, softSkill, id_candidate ) values (8, 8, 14, 18, 2);
insert into grades (interview, theory, practice, softSkill, id_candidate ) values (19, 20, 11, 6, 3);
insert into grades (interview, theory, practice, softSkill, id_candidate ) values (18, 10, 5, 15, 4);
insert into grades (interview, theory, practice, softSkill, id_candidate ) values (7, 8, 4, 7, 5);
insert into grades (interview, theory, practice, softSkill, id_candidate ) values (14, 4, 17, 15, 6);
insert into grades (interview, theory, practice, softSkill, id_candidate ) values (10, 7, 17, 12, 7);
insert into grades (interview, theory, practice, softSkill, id_candidate ) values (11, 7, 16, 11, 8);
insert into grades (interview, theory, practice, softSkill, id_candidate ) values (17, 16, 11, 17, 9);
insert into grades (interview, theory, practice, softSkill, id_candidate ) values (17, 12, 19, 17, 10);
insert into grades (interview, theory, practice, softSkill, id_candidate ) values (12, 20, 5, 20, 11);
insert into grades (interview, theory, practice, softSkill, id_candidate ) values (14, 6, 12, 20, 12);
insert into grades (interview, theory, practice, softSkill, id_candidate ) values (13, 11, 15, 11, 13);
insert into grades (interview, theory, practice, softSkill, id_candidate ) values (1, 16, 11, 18, 14);
insert into grades (interview, theory, practice, softSkill, id_candidate ) values (15, 10, 16, 10, 15);
insert into grades (interview, theory, practice, softSkill, id_candidate ) values (13, 16, 8, 17, 16);
insert into grades (interview, theory, practice, softSkill, id_candidate ) values (9, 7, 16, 14, 17);
insert into grades (interview, theory, practice, softSkill, id_candidate ) values (12, 7, 5, 19, 18);
insert into grades (interview, theory, practice, softSkill, id_candidate ) values (1, 20, 2, 1, 19);
insert into grades (interview, theory, practice, softSkill, id_candidate ) values (18, 1, 16, 18, 20);



/*
	GET METHOD 
*/

SELECT 
    candidates.id,
    candidates.name, 
    candidates.telephone,
    candidates.description,
    grades.interview, 
    grades.theory, 
    grades.practice, 
    grades.softkill 
FROM 
    candidates 
LEFT JOIN grades 
ON candidates.id = grades.id_candidate;


/*
	WHEN GET HAS PARAMETERS
*/


SELECT 
    candidates.id,
    candidates.name, 
    candidates.telephone,
    candidates.description,
    grades.interview, 
    grades.theory, 
    grades.practice, 
    grades.softkill 
FROM 
    candidates 
LEFT JOIN grades 
ON candidates.id = grades.id_candidate
WHERE 
	grades.interview = valor
AND 
	grades.theory = valor
AND 
	grades.practice = valor
AND 
	grades.softSkill = valor


