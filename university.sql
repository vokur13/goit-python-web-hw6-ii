-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name VARCHAR(56) NOT NULL,
    first_name VARCHAR(56) NOT NULL,
    e_mail VARCHAR(128) NOT NULL,
    faculty_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (faculty_id) REFERENCES faculties (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE

);

-- Table: faculties
DROP TABLE IF EXISTS faculties;
CREATE TABLE faculties (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(56) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: professors
DROP TABLE IF EXISTS professors;
CREATE TABLE professors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name VARCHAR(56) NOT NULL,
    first_name VARCHAR(56) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(56) NOT NULL,
    professor_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
     FOREIGN KEY (professor_id) REFERENCES professors (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Table: marks
DROP TABLE IF EXISTS marks;
CREATE TABLE marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject_id INTEGER,
    mark INTEGER,
    date_of DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);



