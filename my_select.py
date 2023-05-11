from sqlalchemy import select
from sqlalchemy import and_
from connect_db import session
from sqlalchemy import func, desc
from models import Stusents, Groups, Teachers, Courses, Grades

def select_1():
    query_1=session.query(Grades.student_name, func.round(func.avg(Grades.grade, 2).label('avg_grade'))\
        .select_from(Grades).join(Students).group_by(Students.id).order_by(desc('avg_grade')).limit(5).all()
    print(query_1)

def select_2(course):
    query_2=session.query(Grades.student_name, Grades.course_name, func.max(func.avg(Grades.grade).label('highest_avg_grade')) \
        select_from(Grades).filter(Grades.course_name = course).all()
    print(query_2)

def select_3(course):
    query_3 = session.query(Grades.course_name, Groups.group_number, func.avg(Grades.grade).label('avg_grade'))\
        .select_from(Groups)join(Grades).filter(Grades.course_name == course).group_by(Groups.group_number).all()
    print(query_3)

def select_4():
    query_4=session.query(func.avg(Grades.grade).label('avg_grade')).select_from(Grades).all()
    print(query_4)

def select_5(name):
    query_5=session.query(Courses.teacher_name, Courses.course).select_from(Courses).filter(Courses.teacher_name==name).all()
    print(query_5)

def select_6(number):
    query_6=session.query(Groups.group_number, Groups.student_name).select_from(Groups).filter(Groups.group_number==number).all()
    print(query_6)

def select_7(course, number):
    query_7=session.query(Grades.course_name, Grades.grade, Groups.group_number)\
        .select_from(Groups)join(Grades).filter(and_(Grades.course_name == course, Groups.group_number== number).all()
    print(query_7)

def select_8():
    query_8=session.query(Courses.teacher_name, Courses.course, func.avg(Grades.grade).label('avg_grade'))\
        .select_from(Courses).join(Grades).all()
    print(query_8)

def select_9(name):
    query_9 = session.query(Students.name, Grades.course).select_from(Students)\
        .join(Grades).filter(Students.name==name).all()
    print(query_9)

def select_10(tname, sname):
    query_10=session.query(Courses.teacher_name, Courses.course, Grades.student_name)\
        .select_from(Courses)join(Grades).filter(and_(Grades.student_name == sname, Courses.teacher_name== tname).all()
    print(query_10)

if __name__ == "__main__":


