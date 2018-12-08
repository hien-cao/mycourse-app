# The data models for the app

# Create class student
class Student:
  def __init__(self, firstName, lastName, gender):
    self.id = self.studentIDGenerator()
    self.name = '{} {}'.format(firstName.strip().lower().capitalize(), lastName.strip().lower().capitalize())
    self.email = '{}.{}@aalto.fi'.format(firstName.strip().lower(), lastName.strip().lower())
    self.gender = gender.strip().lower().capitalize()
    self.registerCourses = []
  
  def studentIDGenerator(self):
    if len(studentData) == 0:
      return 1001
    else: 
      return int(studentData[-1].id) + 1

  def __str__(self):
    return 'Student: ' + self.name

# Create class course
class Course:
  def __init__(self, name, periods, weekDays):
    self.id = self.courseIDGenerator()
    self.name = name.strip().title()
    self.periods = periods
    self.weekDays = weekDays
    self.registerStudents = []

  def courseIDGenerator(self):
    if len(courseData) == 0:
      return 101
    else: 
      return int(courseData[-1].id) + 1
  
  def __str__(self):
    return 'Course: ' + self.name

# Student database
studentData = []

# Course database
courseData = []