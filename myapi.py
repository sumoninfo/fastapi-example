from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def index():
    return {"name": "First Data"}


students = {
    1: {
        "name": "Sumon",
        "age": 12,
        "year": "Year 12"
    }
}


class Student(BaseModel):
    name: str
    age: int
    year: str


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student you want to view", gt=0, lt=100)):
    return students[student_id]


@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}

    students[student_id] = student
    return student
