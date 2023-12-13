#!/usr/bin/env python3

def create_grade_report(student_grades):
    with open('reports/grade_report.txt', 'w') as gr:
        gr.write(student_grades)

if __name__ == '__main__':
    student_grades = input("Student name, grade: ")
    create_grade_report(student_grades)






    [{
  "barista_id": 9,
  "first_name": "Garland",
  "last_name": "Gianelli",
  "meal_served": "soft drink",
  "age": 42
}, {
  "barista_id": 10,
  "first_name": "Gordan",
  "last_name": "Schneidar",
  "meal_served": "taco",
  "age": 45
}, {
  "barista_id": 11,
  "first_name": "Evonne",
  "last_name": "Carlill",
  "meal_served": "pizza",
  "age": 3
}]