DROP TABLE IF EXISTS student;

CREATE TABLE student(
    id serial PRIMARY KEY,
    first_name VARCHAR (20),
    last_name VARCHAR (20),
    age INT,
    grade CHAR (1)
);

-- COPY student FROM '/Users/bryanbartell/Desktop/code-platoon/Assignments/WEEK4/Day2/data.csv' DELIMITER ',' CSV HEADER;

INSERT INTO student(first_name, last_name, age, grade) VALUES
    ('John', 'Doe', 18, 'A'),
    ('Jane', 'Smith', 19, 'B'),
    ('Bob', 'Johnson', 20, 'C'),
    ('Emily','Williams', 18, 'A'),
    ('Michael', 'Brown', 19, 'B'),
    ('Bryan','Bartell', 37, 'B');

    SELECT * FROM student;

   
    -- SELECT * FROM student WHERE grade = 'B';

    -- SELECT grade AS letter, COUNT(*) FROM student WHERE grade = 'A' GROUP BY grade;

    -- SELECT first_name, last_name FROM student ORDER BY last_name;
    --   SELECT first_name, last_name FROM student ORDER BY last_name DESC;
    --   SELECT first_name, last_name FROM student ORDER BY last_name DESC LiMiT 3;

    --   SELECT first_name, last_name FROM student WHERE last_name LIKE 'S%';
    --   SELECT first_name, last_name, COUNT(*) FROM student WHERE grade = 'A' GROUP BY last_name, first_name;

    SELECT * FROM student WHERE age IN (18,19);
    SELECT * FROM student WHERE grade = 'A' AND age > 18 OR grade = 'B';




