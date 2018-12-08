# This is the final project of the course ELEC-A7050 - Basics in programming 2018

import time
import sys
import operator
from prettytable import PrettyTable
from models import *

# Function to print out the banner text
def welcome_banner():
  print(""" 
    ##########################################################
    # ====================================================== # 
    # ================ WELCOME TO MYCOURSES ================ #
    # ====================================================== #
    ##########################################################
    """)

# Function to print out the banner
def banner(title):
  print('\n*** ######### ' + title + ' ######### ***\n')

# Function to make running text
def loader(string):
  print()
  for char in string:
    print(char, end='')
    sys.stdout.flush()
    time.sleep(0.02)
  print()

# Wrong input handler
def wrongInputHandler():
  print('\nWrong Input!\n')
  time.sleep(0.5)

# Back to menu handler
def backToMenuHandler():
  while True: 
    choice = input('Please enter your choice:\n[1] Back to Menu\n')
    if choice == '1':
      main()
      break
    else:
      wrongInputHandler()

# Exit the program handler
def exitProgram():
  print('\nThanks for using this program. See you soon.')
  loader('Exiting...')
  time.sleep(1)
  exit()

# Function to compare the time
def isSmallerOrEqual(start, end):
  time1 = start.split(':')
  time1 = [int(i) for i in time1]
  time2 = end.split(':')
  time2 = [int(i) for i in time2]
  if time1[0] < time2[0]:
    return True
  elif time1[0] == time2[0] and time1[1] < time2[1]:
    return True
  elif time1[0] == time2[0] and time1[1] >= time2[1]:
    return False
  elif time1[0] > time2[0]:
    return False

# Function to add new student
def addStudent():
  # Display the banner
  banner('Add New Student')
  # Get input variables for student
  firstName = input('Enter first name:\n')
  lastName = input('Enter last name:\n')
  gender = input('Enter gender (male/female):\n')
  # Check if the user want to save the inputs
  while True:
    confirm = input('\nDo you want to save? (y/n):\n').strip().lower()
    if confirm == 'y':
      # Create new student
      newStudent = Student(firstName, lastName, gender)
      # Save student to the database
      studentData.append(newStudent)
      loader('Saving..... Complete!')
      time.sleep(0.5)
      main()
      break
    elif confirm == 'n' : 
      loader('Back to the menu...')
      time.sleep(0.5)
      main()
      break
    else: 
      wrongInputHandler()

# Function to display list of all students
def studentTable():
  # Display the banner
  banner('List of All Students')
  if len(studentData) == 0:
    print('There is no student data. Please add some student first.\n')
  else:
    table = PrettyTable(['Student ID', 'Student Name', 'Student Email', 'Student Gender'])
    for student in studentData:
      table.add_row([student.id, student.name, student.email, student.gender])
    print(table)
  backToMenuHandler()

# Function to add new course:
def addCourse():
  # Display the banner
  banner('Add new course')
  # Get input variables for course
  name = input('Enter the course name:\n')
  periods = input('Enter the course periods (1-5, seperated by comma):\n').split(',')
  # Check correct input for periods
  while len(set(periods).intersection(['1', '2', '3', '4', '5'])) == 0 or len(set(periods).intersection(['1', '2', '3', '4', '5'])) != len(set(periods)):
    wrongInputHandler()
    periods = input('Enter the course periods (1-5, seperated by comma):\n').split(',')
  numberOfDay = input('Enter number of day for a week:\n')
  # Check correct input for numberOfDay
  check = True
  while check:
    try: 
      if int(numberOfDay) < 1 or int(numberOfDay) > 5:
        wrongInputHandler()
        numberOfDay = input('Enter number of day for a week:\n')
      else:
        check = False
    except ValueError:
      wrongInputHandler()
      numberOfDay = input('Enter number of day for a week:\n')
  weekDaysData = []
  for i in range(int(numberOfDay)):
    weekDay = input('Enter the day no {} (Mon-Fri):\n'.format(i + 1)).strip().lower().capitalize()
    # Check correct input for weekDay
    while len(set((weekDay, )).intersection(['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])) == 0:
      wrongInputHandler()
      weekDay = input('Enter the day no {} (Mon-Fri):\n'.format(i + 1)).strip().lower().capitalize()
    start = input('Enter the start time (hh:mm):\n')
    # Check correct start time input
    while len(start) != 5 or start[2] != ':' or int(start.split(':')[0]) < 0 or int(start.split(':')[0]) > 23 or int(start.split(':')[1]) < 0 or int(start.split(':')[1]) > 59:
      wrongInputHandler()
      start = input('Enter the start time (hh:mm):\n')
    end = input('Enter the end time (hh:mm):\n')
    # Check correct end time input
    while len(start) != 5 or start[2] != ':' or int(start.split(':')[0]) < 0 or int(start.split(':')[0]) > 23 or int(start.split(':')[1]) < 0 or int(start.split(':')[1]) > 59:
      wrongInputHandler()
      end = input('Enter the end time (hh:mm):\n')
    # Check if start time is less than end time
    while not isSmallerOrEqual(start, end):
      wrongInputHandler()
      start = input('Enter the start time (hh:mm):\n')
      end = input('Enter the end time (hh:mm):\n')
    weekDaysData.append([weekDay, start, end])
  while True:
    confirm = input('\nDo you want to save? (y/n):\n').lower()
    if confirm == 'y':
      # Create the new course
      newCourse = Course(name, periods, weekDaysData)
      # Add new course to the course database
      courseData.append(newCourse)
      loader('Saving..... Complete!')
      time.sleep(0.5)
      main()
      break
    elif confirm == 'n' : 
      loader('Back to the menu...')
      time.sleep(0.5)
      main()
      break
    else: 
      wrongInputHandler()
  
# Function to display list of courses
def courseTable():
  # Display the banner
  banner('List of Courses')
  if len(courseData) == 0:
    print('There is no course data. Please add some course first.\n')
  else:
    table = PrettyTable(['Course ID', 'Course Name', 'Periods'])
    for course in courseData:
      table.add_row([course.id, course.name, ', '.join(course.periods)])
    print(table)
  backToMenuHandler()

# Function to display the course's timetable 
def courseTimeTable(courseID):
  for course in courseData:
    if course.id == courseID:
      table = PrettyTable(['Course ID', 'Course Name', 'Periods', 'Date', 'Start', 'End'])
      for period in course.periods:
        for date in course.weekDays:
          table.add_row([course.id, course.name, period, date[0], date[1], date[2]])
      banner('Course: ' + course.name + ' - Timetable')
      print(table)

# Function to get the course timetable information
def getCourseTimeTable():
  banner('Course Timetable')
  if len(courseData) == 0:
    print('There is no course data. Please add some course first.\n')
  else:
    table = PrettyTable(['Course ID', 'Course Name', 'Periods'])
    for course in courseData:
      table.add_row([course.id, course.name, ', '.join(course.periods)])
    print(table)
    choice = int(input('Enter the course id to be displayed:\n'))
    while not checkCourseID(choice):
      wrongInputHandler()
      choice = int(input('Enter the course id to be displayed:\n')) 
    courseTimeTable(choice)
    while True: 
      select = input('Please enter your choice:\n'
                      '[1] Display Other Course\n'
                      '[2] Back to Menu\n')
      if select == '1':
        getCourseTimeTable()
        break
      elif select == '2':
        main()
        break
      else:
        print('Wrong Input!\n')
        time.sleep(0.5) 
  backToMenuHandler()

# Function to check whether the course id is in the list of courses
def checkCourseID(courseID):
  check = False
  for course in courseData:
    if course.id == courseID:
      check = True
  return check

# Function to check whether the course id is in the list of courses
def checkStudentID(studentID):
  check = False
  for student in studentData:
    if student.id == studentID:
      check = True
  return check

# Function to register course for student
def registerCourse():
  banner('Course Registration')
  # Check empty student data
  if len(studentData) == 0:
    print('There is no student data. Please add some student first.\n')
  else:
    table = PrettyTable(['Student ID', 'Student Name', 'Student Email', 'Student Gender'])
    for student in studentData:
      table.add_row([student.id, student.name, student.email, student.gender])
    print(table)
    # Check valid input for student id
    while True:
      try:
        selectedStudentID = int(input('Enter selected student id:\n'))
        while not checkStudentID(selectedStudentID):
          wrongInputHandler()
          selectedStudentID = int(input('Enter selected student id:\n'))
      except ValueError:
        wrongInputHandler()
        continue
      else:
        break
    # Check empty course data
    if len(courseData) == 0:
      print('There is no course data. Please add some course first.\n')
    else:
      table = PrettyTable(['Course ID', 'Course Name', 'Periods'])
      for course in courseData:
        table.add_row([course.id, course.name, ', '.join(course.periods)])
      print(table)
      # Check valid input for the course id
      while True:
        try:
          selectedCourseID = int(input('Enter selected course id:\n'))
          while not checkCourseID(selectedCourseID ):
            wrongInputHandler()
            selectedCourseID = int(input('Enter selected course id:\n'))
        except ValueError:
          wrongInputHandler()
          continue
        else: 
          break
      # Check if the student has already enrolled for the course
      while alreadyEnrolled(selectedStudentID, selectedCourseID):
        print('\nThe student has already enrolled for the course.\n')
        while True: 
            select = input('Please enter your choice:\n'
                            '[1] Register for Other Course\n'
                            '[2] Back to Menu\n')
            if select == '1':
              selectedCourseID = int(input('Enter selected course id:\n'))
              break
            elif select == '2':
              main()
              break
            else:
              wrongInputHandler()
      # Check if the courses overlap
      if isOverLap(selectedStudentID, selectedCourseID):
        print('\nThe chosen course overlaps existed course of the student.')
      while True: 
        confirm = input('\nDo you want to save selected student with selected course? (y/n):\n').lower()
        if confirm == 'y':
          # Add the course to the student and vice versa
          updateRegister(selectedStudentID, selectedCourseID)
          loader('Saving..... Complete!')
          time.sleep(0.5)
          main()
          break
        elif confirm == 'n' : 
          loader('Back to the menu...')
          time.sleep(0.5)
          main()
          break
        else: 
          wrongInputHandler()
    while True: 
      choice = input('Please enter your choice:\n'
                      '[1] Back to Menu\n')
      if choice == '1':
        main()
        break
      else:
        wrongInputHandler()
  backToMenuHandler()

# Function to add course to student and student to course
def updateRegister(studentID, courseID):
  for student in studentData:
    if student.id == studentID:
      for course in courseData:
        if course.id == courseID:
          student.registerCourses.append(course)
          course.registerStudents.append(student)

# Function to check if the student has already enrolled for the course
def alreadyEnrolled(studentID, courseID):
  for student in studentData:
    if student.id == studentID:
      for course in student.registerCourses:
        if course.id == courseID:
          return True
        else:
          return False

# Function to check if courses timetable overlap
def isOverLap(studentID, courseID):
  for student in studentData:
    if student.id == studentID:
      for course in courseData:
        if course.id == courseID: 
          for studentCourse in student.registerCourses:
            if len(set(course.periods).intersection(studentCourse.periods)) > 0:
              courseDate = []
              studentCourseDate = []
              for date in course.weekDays:
                courseDate.append(date[0])
              for date in studentCourse.weekDays:
                studentCourseDate.append(date[0])
              overLapDate = set(courseDate).intersection(studentCourseDate)
              if len(set(overLapDate)) > 0:
                for date in overLapDate:
                  for i in course.weekDays:
                    for j in studentCourse.weekDays:
                      if i[0] == date and j[0] == date:
                        lastestStart = ''
                        earliestEnd = ''
                        if isSmallerOrEqual(i[1], j[1]):
                          lastestStart = j[1]
                        else:
                          lastestStart = i[1]
                        if isSmallerOrEqual(i[2], j[2]):
                          earliestEnd = i[2]
                        else: 
                          earliestEnd = j[2]
                        if isSmallerOrEqual(earliestEnd, lastestStart):
                          return False
                        else: 
                          return True
                        
# Function to show student's timetable
def studentTimeTable():
  banner('Student Learning Timetable')
  # Check empty student data
  if len(studentData) == 0:
    print('There is no student in the database.\n')
  else:
    table = PrettyTable(['Student ID', 'Student Name', 'Student Email', 'Student Gender'])
    for student in studentData:
      table.add_row([student.id, student.name, student.email, student.gender])
    print(table)
    # Check valid input for student id
    while True:
      try:
        selectedStudentID = int(input('Enter selected student id:\n'))
        while not checkStudentID(selectedStudentID ):
          wrongInputHandler()
          selectedStudentID = int(input('Enter selected student id:\n')) 
      except ValueError:
        wrongInputHandler()
        continue
      else:
        break
    for student in studentData:
      if student.id == selectedStudentID:
        if student.registerCourses == []:
          print('\nThe student has not enrolled for any course.\n')
          while True: 
            select = input('Please enter your choice:\n'
                            '[1] Display Other Student Timetable\n'
                            '[2] Back to Menu\n')
            if select == '1':
              studentTimeTable()
              break
            elif select == '2':
              main()
              break
            else:
              wrongInputHandler()
        else:
          choice = input('\nPlease enter your choice:\n'
                            '[1] Timetable for all periods\n'
                            '[2] Timetable for periods\n')
          while choice != '1' and choice != '2':
            wrongInputHandler()
            choice = input('\nPlease enter your choice:\n'
                            '[1] Timetable for all periods\n'
                            '[2] Timetable for periods\n')
          if choice == '1':
            table = PrettyTable(['Course ID', 'Course Name', 'Periods', 'Date', 'Start', 'End'])
            for course in student.registerCourses:
              for period in course.periods:
                for date in course.weekDays:
                  table.add_row([course.id, course.name, int(period), date[0], date[1], date[2]])
            banner('Student: ' + student.name + ' - Timetable for All Periods')
            # Print the table with periods order
            print(table.get_string(sort_key=operator.itemgetter(1, 0), sortby="Periods"))
            while True: 
              select = input('\nPlease enter your choice:\n'
                              '[1] Display Other Student Timetable\n'
                              '[2] Back to Menu\n')
              if select == '1':
                studentTimeTable()
                break
              elif select == '2':
                main()
                break
              else:
                wrongInputHandler()
          else:            
            selectPeriods = input("\nSelect the periods to be displayed (1-5, seperated by comma):\n").split(',')
            # Check valid input for periods
            while len(set(selectPeriods).intersection(['1', '2', '3', '4', '5'])) == 0 or len(set(selectPeriods).intersection(['1', '2', '3', '4', '5'])) != len(set(selectPeriods)):
              wrongInputHandler()
              selectPeriods = input("\nSelect the periods to be displayed (1-5, seperated by comma):\n").split(',')
            samePeriod = []
            table = PrettyTable(['Course ID', 'Course Name', 'Periods', 'Date', 'Start', 'End'])
            for selectPeriod in selectPeriods:
              for course in student.registerCourses:
                for period in course.periods:
                  if selectPeriod == period:
                    samePeriod.append(period)
                    for date in course.weekDays:
                      table.add_row([int(course.id), course.name, period, date[0], date[1], date[2]])
            samePeriod.sort()
            if len(samePeriod) == 0:
              print('\nThe student has no course with timetable in the selected period(s).\n')
            else:
              banner('Student: ' + student.name + ' - Timetable for Period(s): ' + ', '.join(set(samePeriod)))
              # Print the table in course ID order
              print(table.get_string(sort_key=operator.itemgetter(1, 0), sortby="Periods"))
            while True: 
              select = input('\nPlease enter your choice:\n'
                              '[1] Display Other Student Timetable\n'
                              '[2] Back to Menu\n')
              if select == '1':
                studentTimeTable()
                break
              elif select == '2':
                main()
                break
              else:
                wrongInputHandler()
  backToMenuHandler()
  
# Function to show the list of students who already registered for a course
def courseStudentList():
  banner('List of Students Registered for a Course')
  # Check empty student data
  if len(courseData) == 0:
    print('There is no course in the database.\n')
  else:
    table = PrettyTable(['Course ID', 'Course Name', 'Periods'])
    for course in courseData:
      table.add_row([course.id, course.name, ', '.join(course.periods)])
    print(table)
    # Check valid input for course id
    while True:
      try:
        courseID = int(input('Enter the course id to be displayed:\n'))
        while not checkCourseID(courseID):
          wrongInputHandler()
          courseID = int(input('Enter the course id to be displayed:\n'))
      except ValueError:
        wrongInputHandler() 
        continue
      else:
        break
    printCourseStudent(courseID)
    while True: 
      select = input('Please enter your choice:\n'
                      '[1] Display Student List of Other Course\n'
                      '[2] Back to Menu\n')
      if select == '1':
        courseStudentList()
        break
      elif select == '2':
        main()
        break
      else:
        print('Wrong Input!\n')
        time.sleep(0.5)
  backToMenuHandler()

# Function to display list of student of a specific course with the course id
def printCourseStudent(courseID):
  for course in courseData:
    if course.id == courseID:
      if len(course.registerStudents) == 0:
        print('\nThere is no student enrolling for the course\n')
      else:
        table = PrettyTable(['Student ID', 'Student Name', 'Student Email', 'Student Gender'])
        for student in course.registerStudents:
          table.add_row([int(student.id), student.name, student.email, student.gender])
        banner('Course: ' + course.name + ' - List of Registered Students')
        # Print the table in student id order
        print(table.get_string(sort_key = operator.itemgetter(1, 0), sortby = 'Student ID')) 

def main():
  welcome_banner()
  choice = input('Please enter your choice:\n'
                  '[1] Add New Student\n'
                  '[2] Add New Course\n'
                  '[3] Register Course\n'
                  '[4] Show All Students\n'
                  '[5] Show All Courses\n'
                  '[6] Show Course Timetable\n'
                  '[7] Show Student Timetable\n'
                  '[8] Show List of Students Registered for a Course\n'
                  '[9] Exit The Program\n')
  if choice == '1':
    addStudent()
  elif choice == '2':
    addCourse()
  elif choice == '3':
    registerCourse()
  elif choice == '4':
    studentTable()
  elif choice == '5':
    courseTable()
  elif choice == '6':
    getCourseTimeTable()
  elif choice == '7':
    studentTimeTable()
  elif choice == '8':
    courseStudentList()
  elif choice == '9':
    exitProgram()
  else:
    wrongInputHandler()
    main()

if __name__ == '__main__':
  main()


