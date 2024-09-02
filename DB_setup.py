import mysql.connector
import random
import string

# modify it by your own connection info
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='root'
)

cursor = conn.cursor()


def create_database_and_tables():
    cursor.execute("CREATE DATABASE IF NOT EXISTS stu_enroll")
    cursor.execute("USE stu_enroll")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            FIRST_NAME VARCHAR(50) NOT NULL,
            SURNAME VARCHAR(50) NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Courses (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            DESCRIPTION VARCHAR(255) NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Enrolments (
            ENROLMENT_ID INT AUTO_INCREMENT PRIMARY KEY,
            USERID INT,
            COURSEID INT,
            STATUS ENUM('not started', 'in progress', 'completed') NOT NULL,
            FOREIGN KEY (USERID) REFERENCES Users(ID),
            FOREIGN KEY (COURSEID) REFERENCES Courses(ID)
        )
    """)

    conn.commit()

def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def insert_random_courses(n):
    cursor.execute("USE stu_enroll")
    for _ in range(n):
        descs = random_string(10)
        cursor.execute("INSERT INTO Courses (DESCRIPTION) VALUES (%s)", (descs,))
    conn.commit()

def insert_random_users(n):
    cursor.execute("USE stu_enroll")
    for _ in range(n):
        first_name = random_string(6)
        surname = random_string(8)
        cursor.execute("INSERT INTO Users (FIRST_NAME, SURNAME) VALUES (%s, %s)", (first_name, surname))
    conn.commit()

def insert_random_enrolments(n):
    cursor.execute("USE stu_enroll")

    cursor.execute("SELECT ID FROM Users")
    user_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT ID FROM Courses")
    course_ids = [row[0] for row in cursor.fetchall()]

    for _ in range(n):
        userid = random.choice(user_ids)
        courseid = random.choice(course_ids)
        status = random.choice(['not started', 'in progress', 'completed'])
        cursor.execute("INSERT INTO Enrolments (USERID, COURSEID, STATUS) VALUES (%s, %s, %s)", (userid, courseid, status))
    conn.commit()
# modify those by your own need of num of data-entry
create_database_and_tables()
insert_random_courses(50)  
insert_random_users(100)   
insert_random_enrolments(200)  


cursor.close()
conn.close()

print("Database setup and data insertion complete.")