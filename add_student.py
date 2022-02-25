import csv


def add_student(first_name, last_name, age):
    with open("students.csv", "a") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([first_name, last_name, age])


add_student('Andrey', 'Ponomarev', '25')