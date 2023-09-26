import ratemyprofessor
import mysql.connector
from mysql.connector import Error
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

# function to put all prof names in a list
def getProfNames():
    connection = mysql.connector.connect(**db_config)

    # names = []
    # profNames = getProfNames(names)
    # print(profNames)
    school_name = "California State University Long Beach"
    school = ratemyprofessor.get_school_by_name(school_name)

    #establish webdriver
    driver = webdriver.Chrome()

    # ad blocker
    chrome_options = ChromeOptions()
    chrome_options.add_extension('extension_5_10_1_0.crx')
    driver = webdriver.Chrome(options = chrome_options)
    #access web page using web driver
    driver.get("https://www.ratemyprofessors.com/search/professors/18846?q=*")

    # names = []
    count = 0

    # number of profs
    numNames = driver.find_element("xpath", '//*[@id="root"]/div/div/div[4]/div[1]/div[1]/div[1]/div/h1')
    numNamesText = numNames.text
    numNamesInt = int(numNamesText[:4])
    # Close cookies button
    buttonClose = driver.find_element("xpath", '/html/body/div[5]/div/div/button')
    buttonClose.click()

    for i in range(1, numNamesInt + 1):
        # 8 professors per page
        if count == 8:
            time.sleep(8)
            # click show more button
            buttonShow = driver.find_element("xpath", '//*[@id="root"]/div/div/div[4]/div[1]/div[1]/div[4]/button')
            buttonShow.click()
            time.sleep(8)
            count = 0
        # scrape prof names
        xpath = f'//*[@id="root"]/div/div/div[4]/div[1]/div[1]/div[3]/a[{i}]/div/div[2]/div[1]'
        xpath_name = driver.find_element("xpath", xpath)
        name_text = xpath_name.text
        if school is not None:
        # Iterate through professors with different names
            professor = ratemyprofessor.get_professor_by_school_and_name(school, name_text)

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
        count += 1
    #     arr.append(name_text)
    #     count += 1
    #     print(arr)
    # return arr


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

getProfNames()

