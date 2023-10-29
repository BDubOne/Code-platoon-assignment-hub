-- SELECT max(id) FROM subjects;

-- EXECUTE 'ALTER SEQUENCE id RESTART WITH' max(id) + 1;

-- INSERT INTO subjects(subject) VALUES
-- ('Front-end Development'),
-- ('Back-end Development'),
-- -- ('Client relations');

-- DELETE FROM subjects
-- WHERE id IN (
--     SELECT id 
--     FROM subjects
--     ORDER BY id DESC
--     LIMIT 3
-- )

-- SELECT max(id) FROM students;

-- EXECUTE 'ALTER SEQUENCE id RESTART WITH' max(id) + 1;

-- INSERT INTO students(first_name,last_name, age, subject_id) VALUES
-- ('Bryan', 'Bartell', 37, 3),
-- ('Jason', 'Vorhees', 99, 5);

-- SELECT max(id) FROM teachers;


-- ALTER SEQUENCE id_seq RESTART WITH (max_id + 1);

INSERT INTO teachers(first_name,last_name,age,subject_id) VALUES
('Francisco',' Anon', 29, 6),
('Adam', 'Origin', 42, 7),
('Nick',' Man', 33, 8);
