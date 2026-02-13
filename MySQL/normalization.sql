USE normalization;

CREATE TABLE IF NOT EXISTS dojos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  location VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS students (
  id INT AUTO_INCREMENT PRIMARY KEY,
  dojo_id INT,
  name VARCHAR(255),
  address1 VARCHAR(255),
  address2 VARCHAR(255),
  FOREIGN KEY (dojo_id) REFERENCES dojos(id)
);

CREATE TABLE IF NOT EXISTS interests (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) UNIQUE
);

CREATE TABLE IF NOT EXISTS students_interests (
  id INT AUTO_INCREMENT PRIMARY KEY,
  student_id INT,
  interest_id INT,
  FOREIGN KEY (student_id) REFERENCES students(id),
  FOREIGN KEY (interest_id) REFERENCES interests(id)
);
