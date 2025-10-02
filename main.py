import sqlite3
import os 
import time 
from datetime import datetime
import logging


connection = sqlite3.connect('5.db')
cursor = connection.cursor()

# Creating colleges table
cursor.execute('''
CREATE TABLE IF NOT EXISTS colleges(
               CollegeID INTEGER PRIMARY KEY AUTOINCREMENT,
               CollegeName TEXT NOT NULL,
               DeanID INTEGER,
               FOREIGN KEY (DeanID) REFERENCES professors(ProfessorID)
                )''')

# END

# # Creating departments table
cursor.execute('''
CREATE TABLE IF NOT EXISTS departments(
    DeptID INTEGER PRIMARY KEY,
    DeptName TEXT NOT NULL,
    CollegeID INTEGER NOT NULL,
    DeptHeadID INTEGER NOT NULL,
    FOREIGN KEY (CollegeID) REFERENCES colleges(CollegeID),
    FOREIGN KEY (DeptHeadID) REFERENCES professors(ProfessorID)
)
''')
# # END

# # Creating students table
# cursor.execute('''CREATE TABLE IF NOT EXISTS students(
#                 StudentID INTEGER PRIMARY KEY,
#                 FirstName TEXT NOT NULL,
#                 LastName TEXT NOT NULL,
#                 DateOfBirth DATE NOT NULL,
#                 Gender TEXT NOT NULL,
#                 Email TEXT UNIQUE NOT NULL,
#                 PhoneNumber TEXT UNIQUE NOT NULL,
#                 EnrollmentStatus TEXT NOT NULL,
#                 MajorDeptID INTEGER NOT NULL,
#                 FOREIGN KEY (MajorDeptID) REFERENCES departments(DeptID),
#                 MinorDeptID INTEGER NOT NULL,
#                 FOREIGN KEY (MinorDeptID) REFERENCES departments(DeptID)
#                )''')
# # END

# Creating professors table
cursor.execute('''
CREATE TABLE IF NOT EXISTS professors(
               ProfessorID INTEGER PRIMARY KEY AUTOINCREMENT,
               FirstName TEXT NOT NULL,
               LastName TEXT NOT NULL,
               DateOfBirth DATE NOT NULL,
               CHECK ((strftime('%F') - DateOfBirth) >= 18),
               PhoneNumber TEXT UNIQUE NOT NULL,
               OfficeLocation TEXT NOT NULL)''')

# END

# # Creating staff table
# cursor.execute('''CREATE TABLE IF NOT EXISTS staff(
#                 StaffID INTEGER PRIMARY KEY,
#                 FirstName TEXT NOT NULL,
#                 LastName TEXT NOT NULL,
#                 Position TEXT NOT NULL,
#                 Salary FLOAT NOT NULL,
#                 Email TEXT UNIQUE NOT NULL,
#                 PhoneNumber TEXT UNIQUE NOT NULL,
#                 EmploymentStatus TEXT NOT NULL
#                )''')
# # END

# # Creating courses table
# cursor.execute('''CREATE TABLE IF NOT EXISTS courses(
#                 CourseID INTEGER PRIMARY KEY,
#                 CourseName TEXT NOT NULL,
#                 CourseCode TEXT UNIQUE NOT NULL,
#                 DeptID INTEGER NOT NULL,
#                 FOREIGN KEY (DeptID) REFERENCES departments(DeptID)
#                 Credits INTEGER NOT NULL,
#                 Description TEXT NOT NULL
#                )''')

# # END

# # Creating course prerequisites table
# # cursor.execute('''CREATE TABLE IF NOT EXISTS coursePrerequisites(
# #                 ///////////////////////////////////////// HELP ME WITH THIS TABLE :(
# #                )''')

# # END

# # Creating classrooms table
# cursor.execute('''CREATE TABLE IF NOT EXISTS classrooms(
#                 RoomID INTEGER PRIMARY KEY,
#                 BuildingName TEXT NOT NULL,
#                 RoomNumber TEXT NOT NULL,
#                 Capacity INTEGER NOT NULL,
#                 RoomType TEXT NOT NULL
#                )''')

# # END

# # Creating schedules table
# cursor.execute('''CREATE TABLE IF NOT EXISTS courseSchedule(
#                 ScheduleID INTEGER PRIMARY KEY,
#                 CourseID INTEGER NOT NULL,
#                 FOREIGN KEY (CourseID) REFERENCES courses(CourseID),
#                 RoomID INTEGER NOT NULL,
#                 FOREIGN KEY (RoomID) REFERENCES classrooms(RoomID),
#                 ProfessorID INTEGER NOT NULL,
#                 FOREIGN KEY (ProfessorID) REFERENCES professors(ProfessorID),
#                 DayOfWeek TEXT NOT NULL,
#                 StartTime TIME NOT NULL,
#                 EndTime TIME NOT NULL,
#                 Semester TEXT NOT NULL,
#                 Year INTEGER NOT NULL
#                )''')

# # END

# # Creating enrollments table
# cursor.execute('''CREATE TABLE IF NOT EXISTS enrollments(
#                 EnrollmentID INTEGER PRIMARY KEY,
#                 StudentID INTEGER NOT NULL,
#                 FOREIGN KEY (StudentID) REFERENCES students(StudentID),
#                 CourseID INTEGER NOT NULL,
#                 FOREIGN KEY (CourseID) REFERENCES courses(CourseID),
#                 Semester TEXT NOT NULL,
#                 Year INTEGER NOT NULL,
#                 Grade TEXT NOT NULL
#                )''')
# # END

# # Creating tuition and fees table
# cursor.execute('''CREATE TABLE IF NOT EXISTS tuitionAndFees(
#                 FeeID INTEGER PRIMARY KEY,
#                 FeeName TEXT NOT NULL,
#                 Amount INTEGER NOT NULL,
#                 AcademicYear INTEGER NOT NULL,
#                 FeeType TEXT NOT NULL
#                )''')
# # END

# # Creating student accounts table
# cursor.execute('''CREATE TABLE IF NOT EXISTS studentAccounts(
#                 AccountId INTEGER PRIMARY KEY,
#                 StudentID INTEGER NOT NULL,
#                 FOREIGN KEY (StudentID) REFERENCES students(StudentID),
#                 FeeID INTEGER NOT NULL,
#                 FOREIGN KEY (FeeID) REFERENCES tuitionAndFees(FeeID),
#                 AmountDue FLOAT,
#                 DueDate DATE NOT NULL),
#                 Status TEXT NOT NULL)''')
# # END

# Creating fee payments table
connection.commit()
connection.close()