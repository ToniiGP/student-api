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

