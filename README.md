# The final project of ELEC-A7050 - Basics in Programming 

[![SMS Created](https://img.shields.io/badge/Created-December%202018-brightgreen.svg)](#)
[![SMS version](https://img.shields.io/badge/Python-3-blue.svg)](#)

**Name:** Hien Cao

**Student Number:** 716718

**School:** Aalto University, School of Electrical Engineering

## Project information:

**Project Name:** Study plan management system

**Project Description:** Implement a system to maintain study plans for students. The system should be able to maintain multiple students, each with a personal study plan. The study plan consists of courses that a student has planned to take. For each course the system should maintain the schedule: which periods and at which times the course events take place. For each student the system should be able to present a personal schedule for each period, depending on which courses the student has selected.

**Project Language and Libraries:** The app is written by python3 with PrettyTable library and other built-in python library such as time, system, operator.

## Running the Program:
* `python3 -m pip install -r requirements.txt`
* `python3 app.py`

## Program struture:
* app.py - contains the main functions and error handlers to run the program
* models.py - contains the data structure and database of Student and Course
* requirements.txt - contains the external python libraries required to run the program
* README.md

## Main Feature:
* Add new student
* Add new course
* Register for courses, which also handle overlap notification
* Show list of all students
* Show list of all courses
* Show courses' timetable
* Show student's timetable
* Show list of students registered for a course








