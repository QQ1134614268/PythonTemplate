import json
from collections import namedtuple
from json import JSONEncoder


class Student:
    def __init__(self, rollNumber, name, marks):
        self.rollNumber, self.name, self.marks = rollNumber, name, marks


class Marks:
    def __init__(self, english, geometry):
        self.english, self.geometry = english, geometry


class StudentEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def customStudentDecoder(studentDict):
    return namedtuple('X', studentDict.keys())(*studentDict.values())


marks = Marks(82, 74)
student = Student(1, "Emma", marks)

# dumps() produces JSON in native str format. if you want to writ it in file use dump()
studentJson = json.dumps(student, indent=4, cls=StudentEncoder)
print("Student JSON")
print(studentJson)

# Parse JSON into an object with attributes corresponding to dict keys.
studObj = json.loads(studentJson, object_hook=customStudentDecoder)

print("After Converting JSON Data into Custom Python Object")
print(studObj.name, studObj.name, studObj.marks.english, studObj.marks.geometry)
