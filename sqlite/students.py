import sqlite3
conn = sqlite3.connect("students_db.db")

c = conn.cursor()
# c.execute("CREATE TABLE students (first_name TEXT, last_name TEXT, age INTEGER);")
# insert_query = "INSERT INTO students VALUES ('James', 'Brown', 21);"

# c.execute("INSERT INTO students VALUES ('James', 'Brown', 21);")

# first_name = 'Jack'
# last_name = 'White'
# age = 22

# jane = ('Jane', 'Air', 18)
# students = [
# 	('Jane', 'Ostin', 19),
# 	('Jack', 'Scott', 22),
# 	('Bob', 'Green', 20)
# ]

# Bad approach! SQL injection danger!
# insert_query = f"INSERT INTO students VALUES ('{first_name}', '{last_name}', {age});"

# Good approach!
# insert_query = "INSERT INTO students VALUES (?, ?, ?);"

# c.execute(insert_query, (first_name, last_name, age))
# c.execute(insert_query, jane)

# for student in students:
# 	c.execute(insert_query, student)

# c.executemany(insert_query, students)


# c.execute("SELECT * FROM students WHERE first_name IS 'James';")

# c.execute("UPDATE students SET last_name = 'Austen' WHERE last_name IS 'Ostin';")

c.execute("DELETE FROM students WHERE last_name IS 'Green';")

# for row in cursor:
# 	print(row)

# print(c.fetchone())
# print(c.fetchall())

c.execute("SELECT * FROM students;")
data = c.fetchall()
[print(row) for row in data]

conn.commit()

conn.close()


# c.execute("INSERT INTO students VALUES ('James', 'Brown', 20);")
# conn.commit()



# conn.close()