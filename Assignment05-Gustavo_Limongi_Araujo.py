# -*- coding: utf-8 -*-


# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Gustavo Limongi Araujo, 02/13/2024, Assignment05)
#   RRoot,1/1/2030,Created Script
#   <Gustavo L. Araujo>,<2/13/2024>, <Assignment 05>
# ------------------------------------------------------------------------------------------ #

import csv

# Define the Constants
MENU = """
-------------Course Registration Program-------------
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
------------------------------------------------------
"""
FILE_NAME = "Enrollments.csv"

# Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
student_data: list = []
students: list = []
csv_data: str = ""
file = None
menu_choice: str = ""


def read_csv_data():
    try:
        with open(FILE_NAME, 'r') as file:
            csv_reader = csv.DictReader (file)
            for row in csv_reader:
                students.append(row)
    except FileNotFoundError:
         print(f"File {FILE_NAME} not found")
    except Exception as e:
         print(f"Error reading file :{e}")

def register_student():
    global student_first_name, student_last_name, course_name
    student_first_name = input("Student First Name: ")
    student_last_name = input("Student Last Name: ")
    course_name = input("Course name: ")
    student_data.append({"First Name": student_first_name, "Last Name": student_last_name, "Course": course_name})

def show_current_data():
    for student in student_data:
        print(f"First Name: {student['First Name']}, Last Name: {student['Last Name']}, Course: {student['Course']}")

def save_data_to_file():
    try:
        with open(FILE_NAME, 'w', newline='') as file:
            headers = ["First Name", "Last Name", "Course"]
            csv_writer = csv.DictWriter(file, fieldnames=headers)
            csv_writer.writeheader()
            for student in student_data:
                csv_writer.writerow(student)
        print(f"Data saved to {FILE_NAME}")
    except Exception as e:
        print(f"Error saving data to a file: {e}")

# Main Program
read_csv_data()

while True:
    print(MENU)
    menu_choice = input("Enter your choice from (1-4): ")

    if menu_choice == "1":
        register_student()
    elif menu_choice == "2":
        show_current_data()
    elif menu_choice == "3":
        save_data_to_file()
    elif menu_choice == "4":
        print("Exiting the program....")
        break
    else:
        print("Invalid Choice. Please try again")
