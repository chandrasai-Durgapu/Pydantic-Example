from pydantic import BaseModel
from typing import List

# Create Course Model
# Each Course has modules
# Each module has lessons

class Lesson(BaseModel):
    lesson_id: int
    topic: str

class Module(BaseModel):
    module_id: int
    name: str
    lessons: List[Lesson]

class Course(BaseModel):
    course_id: int
    title: str
    modules: List[Module]    





