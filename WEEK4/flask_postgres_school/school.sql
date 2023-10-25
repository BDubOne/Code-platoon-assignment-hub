DROP TABLE IF EXISTS student, teachers, subjects;

CREATE TABLE subjects(
    id serial PRIMARY KEY,
    subject VARCHAR(25)
);

CREATE TABLE student(
    id serial PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    age INT,
    student_subject INT
    -- FOREIGN KEY(student_subject) REFERENCES subjects(id)
);

CREATE TABLE teachers(
    id serial PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    age INT,
    subject INT
    -- FOREIGN KEY(subject) REFERENCES subjects(id)
);

COPY student FROM '/Users/bryanbartell/Desktop/code-platoon/Assignments/WEEK4/flask_postgres_school/data/student.csv' DELIMITER ',' CSV HEADER;

COPY teachers FROM '/Users/bryanbartell/Desktop/code-platoon/Assignments/WEEK4/flask_postgres_school/data/teachers.csv' DELIMITER ',' CSV HEADER;


COPY subjects FROM '/Users/bryanbartell/Desktop/code-platoon/Assignments/WEEK4/flask_postgres_school/data/subjects.csv' DELIMITER ',' CSV HEADER;
