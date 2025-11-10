import psycopg2
from psycopg2 import sql

# Function to connect to the PostgreSQL database
def connectToDB():
    try:
        connection = psycopg2.connect(host = 'localhost', database = 'Assignment 3 Q1', user = 'postgres', password = 'password') 
        return connection
    except Exception as e:
        print("Error connecting to the database:", e)
        return None

def getAllStudents():
    connection = connectToDB() # Connects to the database
    if connection:
        cursor = connection.cursor() # Create a cursor object to interact with the database
        cursor.execute("SELECT * FROM students;") # Executes a Select query to fetch all students
        rows = cursor.fetchall() # Fetches all rows from the executed query
        print("\nAll Students:")
        for row in rows:
            print(row) # Prints each student's details
        cursor.close() # Closes the cursor
        connection.close() # Closes the database connection

def addStudent(first_name, last_name, email, enrollment_date):
    connection = connectToDB() # Connects to the database
    if connection:
        cursor = connection.cursor() # Create a cursor object to interact with the database
        cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);", (first_name, last_name, email, enrollment_date)) # Executes an Insert query to add a new student
        connection.commit() # Commits the transaction to the database
        cursor.close() # Closes the cursor
        connection.close() # Closes the database connection

def updateStudentEmail(student_id, new_email):
    connection = connectToDB() # Connects to the database
    if connection:
        cursor = connection.cursor() # Create a cursor object to interact with the database
        cursor.execute("UPDATE students SET email = %s WHERE student_id = %s;", (new_email, student_id)) # Executes an Update query to change the email of a student based on student_id

        if cursor.rowcount == 0:
            print("No student found with that ID.") # If the student_id does not exist do nothing
        else:
            connection.commit() # Commits the transaction to the database
        cursor.close() # Closes the cursor
        connection.close() # Closes the database connection

def deleteStudent(student_id):
    connection = connectToDB() # Connects to the database
    if connection:
        cursor = connection.cursor() # Create a cursor object to interact with the database
        cursor.execute("DELETE FROM students WHERE student_id = %s;", (student_id,)) # Executes a Delete query to remove a student based on student_id

        if cursor.rowcount == 0: # If the student_id does not exist do nothing
            print("No student found with that ID.")
        else:
            connection.commit() # Commits the transaction to the database
        cursor.close()
        connection.close()


getAllStudents()
#addStudent('John', 'Ue', 'john.Ue@example.com', '2023-01-01')
#getAllStudents()
#deleteStudent(2)
#updateStudentEmail(4, 'new@example.com')
#getAllStudents()