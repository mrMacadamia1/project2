import csv


def print_student():
    with open("students.csv") as file:
        csv_reader = csv.reader(file)
        for r in csv_reader:
        	print(r)
print_student()


