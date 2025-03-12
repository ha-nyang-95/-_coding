-- Active: 1741574235838@@localhost@3306@hospital_db

DROP TABLE IF EXISTS visit;
DROP TABLE IF EXISTS doctor;
DROP TABLE IF EXISTS patient;

CREATE TABLE patient(
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_date DATE,
    phone_number VARCHAR(15)
);

CREATE TABLE doctor(
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    specialty VARCHAR(100)
);

CREATE TABLE visit(
    visit_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    doctor_id INT,
    visit_date DATE,
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id)
);

INSERT INTO patient (patient_id, first_name, last_name, birth_date, phone_number)
VALUES
(1, 'John', 'Doe', '1990-01-01', '123-456-7890'),
(2, 'Jane', 'Smith', '1985-02-10', '098-765-4321'),
(3, 'Alice', 'White', '1970-03-15', '111-222-3333');

INSERT INTO doctor (doctor_id, first_name, last_name, specialty)
VALUES
(1, 'Alice', 'Brown', 'Cardiology'),
(2, 'Bob', 'Johnson', 'Neurology'),
(3, 'Charlie', 'Davis', 'Dermatology');


INSERT INTO visit (visit_id, patient_id, doctor_id, visit_date)
VALUES
(1, 1, 1, '2024-01-01'),
(2, 2, 2, '2024-02-01'),
(3, 1, 2, '2024-03-01'),
(4, 3, 3, '2024-04-01'),
(5, 1, 2, '2024-05-01'),
(6, 2, 3, '2024-06-01'),
(7, 3, 1, '2024-07-01');

SELECT p.last_name,p.first_name,p.phone_number,v.visit_date,d.last_name,d.first_name,d.specialty
FROM visit v
INNER JOIN patient p ON p.patient_id = v.patient_id
INNER JOIN doctor d ON d.doctor_id = v.doctor_id;

SELECT d.last_name, COUNT(*) AS doctor_visit_count
FROM visit v
INNER JOIN patient p ON p.patient_id = v.patient_id
INNER JOIN doctor d ON d.doctor_id = v.doctor_id
GROUP BY d.last_name

CREATE OR REPLACE VIEW v_hospital_visit AS
SELECT 
    p.last_name AS patient_last_name,
    p.first_name AS patient_first_name,
    p.phone_number,
    v.visit_date,
    d.doctor_id,
    d.last_name AS doctor_last_name,
    d.first_name AS doctor_first_name,
    d.specialty
FROM visit v
INNER JOIN patient p ON p.patient_id = v.patient_id
INNER JOIN doctor d ON d.doctor_id = v.doctor_id;

SELECT * FROM v_hospital_visit;

SELECT doctor_id, doctor_last_name, patient_last_name, COUNT(*)
FROM v_hospital_visit
WHERE doctor_id=2
GROUP BY patient_last_name
HAVING COUNT(*)>=2;

-- 1-5 --

SELECT *
FROM doctor
WHERE (doctor.last_name,doctor.specialty) in (
    SELECT d.last_name,d.specialty
    FROM doctor d
    JOIN visit v ON d.doctor_id=v.doctor_id
    WHERE d.specialty in ('Neurology', 'Dermatology')
    GROUP BY d.last_name, d.specialty
    HAVING COUNT(DISTINCT v.patient_id) >= 2
);




CREATE OR REPLACE VIEW v_hospital_visit_2 AS
SELECT
    p.last_name AS patient_last_name,
    p.phone_number,
    v.visit_date,
    d.last_name AS doctor_last_name,
    d.specialty
FROM visit v
INNER JOIN doctor d ON d.doctor_id = v.doctor_id
INNER JOIN patient p ON p.patient_id = v.patient_id;

SELECT * FROM v_hospital_visit_2;

SELECT doctor_last_name,patient_last_name,phone_number,visit_date
FROM v_hospital_visit_2
WHERE doctor_last_name='Brown';