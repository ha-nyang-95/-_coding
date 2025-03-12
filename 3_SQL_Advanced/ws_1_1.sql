CREATE DATABASE online_course_platform_db

USE online_course_platform_db

DROP TABLE feedback;
DROP TABLE courses;
DROP TABLE students;

CREATE TABLE students(
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100),
    name VARCHAR(100),
    INDEX idx_students_name (username)
);

CREATE TABLE courses(
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    INDEX idx_courses_name (title)
);

CREATE TABLE feedback(
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    comment TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

INSERT INTO students (username,name)
VALUES
('john','John Doe'),
('jane_smith','Jane Smith'),
('mary_jones','Mary Jones'),
('paul_brown','Paul Brown'),
('lisa_white','Lisa White'),
('tom_clark','Tom Clark');

INSERT INTO courses (title)
VALUES
('Introduction to Programming'),
('Data Science Fundamentals'),
('Web Development Basics'),
('Machine Learning'),
('Cybersecurity 101'),
('Cloud Computing');

INSERT INTO feedback (student_id,course_id,comment,created_at)
VALUES
(1,1,'Great introductory course!','2023-08-01 10:00:00'),
(2,2,'Very informative','2023-08-02 11:00:00'),
(3,3,'Helped me understand the basics','2023-08-03 12:00:00'),
(4,4,'Excellent course on ML','2023-08-04 13:00:00'),
(5,5,'Learned a lot about cybersecurity.','2023-08-05 14:00:00'),
(6,6,'Comprehensive introduction to cloud computing','2023-08-06 15:00:00');

-- 1-2 --
SELECT students.name,feedback.comment,courses.title
FROM feedback
INNER JOIN courses ON courses.id = feedback.course_id
INNER JOIN students ON students.id = feedback.student_id
WHERE students.username='John Doe';

SELECT students.name,feedback.comment,courses.title
FROM feedback
LEFT JOIN students ON students.id = feedback.student_id
LEFT JOIN courses ON courses.id = feedback.course_id
WHERE students.username = 'jane_smith';

SELECT students.name, feedback.comment, feedback.created_at
FROM students
INNER JOIN feedback ON feedback.student_id = students.id
WHERE students.username='mary_jones' AND feedback.created_at = (
    SELECT max(created_at)
    FROM feedback
    INNER JOIN students ON students.id = feedback.student_id
    WHERE students.username = 'mary_jones'
    );

-- 1-3 --
SELECT s.name, f.comment, f.created_at
FROM feedback f
INNER JOIN students s ON s.id=f.student_id
WHERE s.username='john'
ORDER BY f.created_at
LIMIT 1;

CREATE OR REPLACE VIEW v_student_feedback AS
SELECT
    s.username,
    s.name,
    c.title AS course_title,
    f.comment,
    f.created_at
FROM feedback f
INNER JOIN students s ON s.id = f.student_id
INNER JOIN courses c ON c.id = f.course_id;

SELECT *
FROM v_student_feedback;

SELECT *
FROM v_student_feedback
WHERE username='john';


SELECT * FROM students;
SELECT * FROM courses;
SELECT * FROM feedback;