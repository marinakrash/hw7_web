from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()


class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

class Groups(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_number = Column(Integer, nullable=False)
    student_name = Column(String(100), ForeignKey(Students.name, ondelete="CASCADE"))

class Teachers(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

class Courses(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    course = Column(String(100), nullable=False)
    teacher_name = Column(String(100), ForeignKey(Teachers.name, ondelete="CASCADE"))

class Grades(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_name = Column(String(100), ForeignKey(Students.name, ondelete="CASCADE"))
    course_name = Column(String(100), nullable=False)
    grade = Column(Integer, nullable=False)
    date_grade = Column(DateTime, nullable=False)
