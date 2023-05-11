from connect_db import session
from datetime import datetime
from faker import Faker
from random import randint
from models import Students, Groups, Teachers, Courses, Grades

fake = Faker()

def data_for_students():
    for i in range(1, 20):
        student = Students(
            name=fake.name())
        session.add(student)
        group = Groups(
            student_name=student.name,
            group_number=randint(1, 3))
        session.add(group)
        grade = Grades(
            student_name=student.name,
            course_name=fake.job(),
            grade=randint(2, 5),
            date_grade=fake.date_between(start_date='-5y'))
        session.add(grade)
        teacher = Teachers(
            name=fake.name())
        session.add(teacher)
        course = Courses(
            course=grade.course_name,
            teacher_name=teacher.name)
        session.add(course)
    session.commit()


if __name__ == "__main__":
    data_for_students()




