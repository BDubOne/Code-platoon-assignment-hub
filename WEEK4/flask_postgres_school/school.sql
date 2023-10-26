DROP TABLE IF EXISTS students, teachers, subjects;

CREATE TABLE subjects(
    id serial PRIMARY KEY,
    subject VARCHAR(25)
);
COPY subjects FROM '/Users/bryanbartell/Desktop/code-platoon/Assignments/WEEK4/flask_postgres_school/data/subjects.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE students(
    id serial PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    age INT,
    subject_id INT,
    FOREIGN KEY(subject_id) REFERENCES subjects(id)
);
COPY students FROM '/Users/bryanbartell/Desktop/code-platoon/Assignments/WEEK4/flask_postgres_school/data/students.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE teachers(
    id serial PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    age INT,
    subject_id INT,
    FOREIGN KEY(subject_id) REFERENCES subjects(id)
);
COPY teachers FROM '/Users/bryanbartell/Desktop/code-platoon/Assignments/WEEK4/flask_postgres_school/data/teachers.csv' DELIMITER ',' CSV HEADER;







