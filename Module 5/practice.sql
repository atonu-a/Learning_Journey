-- Active: 1791385942957@@127.0.0.1@5432@postgres


CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INT, -- FK → departments.id  (some may be NULL)
    salary NUMERIC(10, 2),
    hire_date DATE,
    is_active BOOLEAN DEFAULT TRUE
);


CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(100),
    email VARCHAR(150),
    joined_date DATE
);

INSERT INTO
    employees (
        id,
        name,
        department_id,
        salary,
        hire_date,
        is_active
    )
VALUES (
        1,
        'Rahim Uddin',
        1,
        75000.00,
        '2020-03-15',
        TRUE
    ),
    (
        2,
        'Karim Hossain',
        1,
        82000.00,
        '2019-07-01',
        TRUE
    ),
    (
        3,
        'Nusrat Jahan',
        2,
        55000.00,
        '2021-01-20',
        TRUE
    ),
    (
        4,
        'Farhan Ahmed',
        2,
        60000.00,
        '2022-06-10',
        FALSE
    ),
    (
        5,
        'Sumaiya Begum',
        3,
        48000.00,
        '2020-11-05',
        TRUE
    ),
    (
        6,
        'Tanvir Islam',
        3,
        51000.00,
        '2023-02-28',
        TRUE
    ),
    (
        7,
        'Ritu Akter',
        4,
        90000.00,
        '2018-09-12',
        TRUE
    ),
    (
        8,
        'Mehedi Hasan',
        4,
        87000.00,
        '2019-04-03',
        TRUE
    ),
    (
        9,
        'Sadia Rahman',
        1,
        70000.00,
        '2022-08-17',
        TRUE
    ),
    (
        10,
        'Jobayer Alam',
        NULL,
        45000.00,
        '2023-12-01',
        TRUE
    );



INSERT INTO
    customers (
        id,
        name,
        city,
        email,
        joined_date
    )
VALUES (
        1,
        'Arif Chowdhury',
        'Dhaka',
        'arif@gmail.com',
        '2022-01-10'
    ),
    (
        2,
        'Mitu Akter',
        'Chittagong',
        'mitu@yahoo.com',
        '2022-03-22'
    ),
    (
        3,
        'Sujon Mia',
        'Sylhet',
        'sujon@gmail.com',
        '2021-07-05'
    ),
    (
        4,
        'Puja Das',
        'Dhaka',
        'puja@hotmail.com',
        '2023-02-14'
    ),
    (
        5,
        'Rubel Khan',
        'Rajshahi',
        'rubel@gmail.com',
        '2021-12-30'
    ),
    (
        6,
        'Nasrin Sultana',
        'Dhaka',
        'nasrin@gmail.com',
        '2023-05-18'
    ),
    (
        7,
        'Imran Hossain',
        'Khulna',
        'imran@gmail.com',
        '2020-09-09'
    ),
    (
        8,
        'Lima Begum',
        'Barisal',
        'lima@gmail.com',
        '2022-11-01'
    ),
    (
        9,
        'Sajid Ahmed',
        'Dhaka',
        'sajid@gmail.com',
        '2024-01-15'
    ),
    (
        10,
        'Tania Islam',
        'Chittagong',
        'tania@gmail.com',
        '2023-08-20'
    );


SELECT * FROM employees;

SELECT * FROM customers;