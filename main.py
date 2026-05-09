from fastapi import FastAPI
from database import initialize_db, get_connection
from models import Student

app = FastAPI()

@app.on_event("startup")
def startup():
    initialize_db()

@app.get("/")
def root():
    return {"message": "Student API is running"}

@app.post("/students")
#function add student 
def add_student(student : Student): 
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students(name, grade) VALUES(?,?)", 
                   (student.name, student.grade))
    conn.commit()
    conn.close()
    return{"message" : "Student added succesfully"}


@app.get("/students") 
def get_students(): 
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return{"students" : [dict(row) for row in rows]}


@app.get("/students/{student_id}")
def get_student(student_id: int): 
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = cursor.fetchone()
    conn.close
    if row is None: 
        return{"error" : "Student not found"}
    return{"Studnet" : dict(row)}

@app.delete("/students/{student_id}")
def delete_student(student_id: int): 
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = cursor.fetchone()
    if row is None: 
         return{"error" : "Student not found"}
    else: 
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    return{"message" : "Student deleted succesfully"}


@app.put("/students/{student_id}")
def put_student(student_id: int, student: Student): 
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = cursor.fetchone()
    if row is None: 
         return{"error" : "Student not found"}
    else: 
        cursor.execute("UPDATE students SET name = ?, grade = ? WHERE id = ?", (student.name, student.grade, student_id))
    conn.commit()
    conn.close()
    return{"message" : "student updated succesfully"}

    
    