#__init__.py is the scraper

import ratemyprofessor
import mysql.connector
from mysql.connector import Error

# Function to insert data into the Instructor MySQL table
def insert_instructor(connection, department, name, num_ratings):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO Instructor (Department, Name, NumRatings) VALUES (%s, %s, %s)"
        val = (department, name, num_ratings)
        cursor.execute(sql, val)
        connection.commit()
        return cursor.lastrowid  # Get the last inserted ID
    except Error as e:
        print(f"Error inserting data into Instructor: {e}")
        return None

# Function to insert data into the Rating MySQL table
def insert_rating(connection, instructor_id, quality, date, difficulty, course, credit, attendance, take_again, grade, review, helpful_pos, helpful_neg):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO Rating (InstructorID, Quality, Date, Difficulty, Course, ForCredit, AttendanceMandatory, WouldTakeAgain, Grade, Review, HelpfulPos, HelpfulNeg) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (instructor_id, quality, date, difficulty, course, credit, attendance, take_again, grade, review, helpful_pos, helpful_neg)
        cursor.execute(sql, val)
        connection.commit()
    except Error as e:
        print(f"Error inserting data into Rating: {e}")

# MySQL database configuration
db_config = {
    "host": "192.168.1.98",
    "user": "root",
    "password": "zip@zap",
    "database": "sentimentrmp",
}

try:
    connection = mysql.connector.connect(**db_config)

    school_name = "California State University Long Beach"
    school = ratemyprofessor.get_school_by_name(school_name)

    if school is not None:
        # Iterate through professors with different names
        for professor_name in ["Jucheol Moon", "Lawrence Lan", "Kyle Mori"]:
            professor = ratemyprofessor.get_professor_by_school_and_name(school, professor_name)

            if professor is not None:
                # Insert instructor data into MySQL database
                instructor_id = insert_instructor(connection, professor.department, professor.name, professor.num_ratings)

                if instructor_id is not None:
                    # Insert rating data into MySQL database
                    ratings = professor.get_ratings()
                    for rating in ratings:
                        insert_rating(
                            connection,
                            instructor_id,
                            rating.rating,
                            rating.date.strftime('%Y-%m-%d %H:%M:%S'),
                            rating.difficulty,
                            rating.class_name,
                            rating.credit,
                            rating.attendance_mandatory,
                            rating.take_again,
                            rating.grade,
                            rating.comment,
                            rating.thumbs_up,
                            rating.thumbs_down
                        )

except Error as e:
    print(f"Error connecting to MySQL: {e}")
finally:
    if connection.is_connected():
        connection.close()