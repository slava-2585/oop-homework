#https://github.com/netology-code/py-homeworks-basic/blob/new_oop/6.classes/README.md

from statistics import mean
from functools import reduce

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self) -> str:
        pass

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)  
        
    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in Lecturer.courses_attached and course in self.courses_in_progress and grade < 11:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка' 
 
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
            

class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def __mean_grade(self):
        return mean(reduce(lambda x, y: x+y, self.grades.values()))
            
        
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка {self.__mean_grade()}'
        

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
 
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
 
# print(best_student.grades)

temp = {'jry':[10, 9, 6, 5], 'dre': [10, 3, 5, 8], 'asr': [1, 5, 6, 7]}
temp2 = reduce(lambda x, y: x+y, temp.values())
print(temp2)