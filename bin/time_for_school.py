#!/usr/bin/env python3

from lib.student import Student
from lib.teacher import Teacher

steve = Student("Steve", "Jobs")

avi = Teacher("Avi", "Flombaum")

some_knowledge = avi.teach()

steve.learn(some_knowledge)

print(f"Steve just learned this important knowledge: '{steve.knowledge[0]}' from Avi")