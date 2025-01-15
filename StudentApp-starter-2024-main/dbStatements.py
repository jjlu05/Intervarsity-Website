from app import app, db
from app.models import Course, Major, Student
from config  import Config

import sqlalchemy as sqla
import sqlalchemy.orm as sqlo
import os
#os.remove("student.db")

app.app_context().push()

db.create_all()



# #--------------------------------------------------
# # We will use the following statements in later videos

# # Add couple Majors
# major1 = Major(name = 'CS', department = 'Computer Science')
# db.session.add(major1)
# major2 = Major(name = 'DS', department = 'Computer Science')
# db.session.add(major2)
# major3 = Major(name = 'ME', department = 'Mechanical Engineering')
# db.session.add(major3)
# major4 = Major(name = 'RBE', department = 'Robotics Engineering')
# db.session.add(major4)
# major5 = Major(name = 'MATH', department = 'Mathematics')
# db.session.add(major5)
# db.session.commit()

# # print Courses
# query = sqla.select(Major)
# results = db.session.scalars(query)
# for major in results:
#     print(major)

# query =  sqla.select(Major).where(Major.name == 'CS')
# result = db.session.execute(query)
# major1 = result.scalars().first()
# # major1 = result.scalars().all()[0]

# query =  sqla.select(Major).where(Major.name == 'RBE')
# major2 = db.session.scalars(query).first()

# # Add couple courses
# c1 = Course(coursenum='3733',majorid = major1.id, title='Software Engineering') # course is associated with major1
# db.session.add(c1)
# c2 = Course(coursenum='3431',majorid = major1.id, title='Database Systems')     # course is associated with major1
# db.session.add(c2)
# c3 = Course(coursenum='1001',majorid = major2.id, title='Introduction to Robotics')     # course is associated with major2
# db.session.add(c3)
# db.session.commit()

# # Add couple students
# s1 = Student(username='sakire', firstname = 'Sakire', lastname = 'Arslan Ay', email='sakire@wpi.edu', address = 'WPI') 
# s1.set_password('123')
# db.session.add(s1)

# s2 = Student(username='john', firstname = 'John', lastname = 'Yates', email='john@wpi.edu')  #address is optional
# s2.set_password('123')
# db.session.add(s2)

# s3 = Student(username='kitten', firstname = 'Snow', lastname = 'Thecat', email='meow@wpi.edu', address = 'Cat Town')  #address is optional
# s3.set_password('123')
# db.session.add(s3)
# db.session.commit()

# # print Courses
# query = sqla.select(Course)
# results = db.session.scalars(query)
# for course in results:
#     print(course)
    
# print("-----------------------------")
# # print courses for major1
# for course in major1.get_courses():
#     print(course)

# print("-----------------------------")
# # print students
# query = sqla.select(Student)
# results = db.session.scalars(query)
# for student in results:
#     print(student)

# # query Student
# s1 = db.session.scalars(sqla.select(Student).where(Student.username == 'sakire')).first()
# s2 = db.session.scalars(sqla.select(Student).where(Student.username == 'john')).first()
# s3 = db.session.scalars(sqla.select(Student).where(Student.username == 'kitten')).first()


# # associate the Students with Majors  (Many-to-Many relationship through 'students_majors_table' association table)
# s1.majors_of_student.add(major1)   # student1 double majors in CS and RBE
# s1.majors_of_student.add(major2)   
# s2.majors_of_student.add(major2)   # student2 only majors in RBE
# s3.majors_of_student.add(major1)   # student3 only majors in CS
# db.session.commit()

# # print majors of the student, i.e., CS and RBE
# results = db.session.scalars(s1.majors_of_student.select())
# for m in results:
#     print(m)

# # print students in the RBE major
# results = db.session.scalars(major2.students_in_major.select())
# for s in results:
#     print(s)
