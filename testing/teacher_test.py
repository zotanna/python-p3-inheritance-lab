#!/usr/bin/env python

from lib.teacher import Teacher
from lib.user import User

class TestTeacher:
    '''Class "Teacher" in teacher.py'''

    def test_is_subclass(self):
        '''is a subclass of "User".'''
        assert(User in Teacher.__bases__)

    def test_initializes_with_names(self):
        '''initializes with first and last name.'''
        my_teacher = Teacher("My", "Teacher")
        assert((my_teacher.first_name, my_teacher.last_name) == ("My", "Teacher"))

    def test_has_class_attribute_knowledge(self):
        '''has a class attribute called "KNOWLEDGE", a list with len > 0.'''
        assert(isinstance(Teacher.KNOWLEDGE, list) and len(Teacher.KNOWLEDGE) > 0)

    def test_can_teach(self):
        '''teaches from list of KNOWLEDGE.'''
        my_teacher = Teacher("My", "Teacher")
        assert(my_teacher.teach() in Teacher.KNOWLEDGE)