#ex 7

student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

def all_grades():
    for i, grade in student["grades"].items():
        print(f"  {i}: {grade}")

print(f"Name: {student["name"]}")
print(f"Number of subjects: {len(student["subjects"])}")
print(f"Enrolled in PNE: {"PNE" in student["subjects"] }")
print(f"Databases grade: {student["grades"]["Databases"]}")
print(f"Average grade: {round(sum(student["grades"].values()) / len(student["grades"]) , 2)}")
print(f"Subject grades:")
all_grades()