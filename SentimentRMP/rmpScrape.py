import ratemyprofessor
import datetime
import csv

professor_name = "Jucheol Moon"
professor = ratemyprofessor.get_professor_by_school_and_name(
    ratemyprofessor.get_school_by_name("California State University Long Beach"), professor_name)
if professor is not None:
    # Instructor.csv
    id = 0
    department = professor.department
    name = professor.name
    num_ratings = professor.num_ratings

    headers = ['ID', 'Department', 'Instructor Name', '# Ratings']
    rows = [id, department, name, num_ratings]
    with open('Instructor.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerow(rows)
    file.close()

    # Rating.csv
    instructor_id = 0
    ratings = professor.get_ratings()
    quality, date, difficulty, course, credit, attendance, take_again, grade, review, helpful_pos, helpful_neg = [], [], [], [], [], [], [], [], [], [], []
    for i in range(len(ratings)):
        quality.append(ratings[i].rating)
        formatted_date = ratings[i].date.strftime('%Y-%m-%d %H:%M:%S')
        date.append(formatted_date)
        difficulty.append(ratings[i].difficulty)
        course.append(ratings[i].class_name)
        credit.append(ratings[i].credit)
        attendance.append(ratings[i].attendance_mandatory)
        take_again.append(ratings[i].take_again)
        grade.append(ratings[i].grade)
        review.append(ratings[i].comment)
        helpful_pos.append(ratings[i].thumbs_up)
        helpful_neg.append(ratings[i].thumbs_down)


    headers = ['ID', 'Quality', 'Date', 'Difficulty', 'Course', 'For Credit', 'Attendance Mandatory', 'Would Take Again', 'Grade', 'Review', 'Helpful(Pos)', 'Helpful(Neg)']
    # rows = list(zip([instructor_id] * len(quality), quality, date, difficulty, course, credit, attendance, take_again, grade, review, helpful_pos, helpful_neg))

    rows = [instructor_id, quality, date, difficulty, course, credit, attendance, take_again, grade, review, helpful_pos, helpful_neg]
    with open('Rating.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerow(rows)
    file.close()



    
   

