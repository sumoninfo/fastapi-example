from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/")
def index():
    return {"name": "First Data"}


students = {
    1: {
        "name": "Sumon",
        "age": 12,
        "class": "Year"
    }
}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student you want to view", gt=0, lt=3)):
    return students[student_id]
