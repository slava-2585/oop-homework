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

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.__mean_grade()} \nКурсы в процессе изучения: {" ".join(self.courses_in_progress)} \nЗавершенные курсы: {" ".join(self.finished_courses)}'
        return res
    
    def __mean_grade(self):
        if self.grades == {}:
            return 0
        else:
            return round(mean(reduce(lambda x, y: x+y, self.grades.values())), 1)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)  
        
    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and grade < 11:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.__mean_grade() < other.__mean_grade()
 
     
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
        return round(mean(reduce(lambda x, y: x+y, self.grades.values())), 1)
            
        
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.__mean_grade()}'
        return res
        
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.__mean_grade() < other.__mean_grade()

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
    
def mean_stud(studs, courses):
    total = []
    for s in studs:
        print (s.grades[courses])
        total += s.grades[courses]
    return round(mean(total), 1)

def mean_lect(lects, courses):
    total = []
    for l in lects:
        print(l.grades[courses])
        total += l.grades[courses]
    return round(mean(total), 1)


stud1 = Student('Иванов', 'Иван', 'Мужской')
stud1.finished_courses = ['C++', 'Java']
stud1.courses_in_progress = ['Python', 'Web']
stud2 = Student('Екатерина', 'Петрова', 'Женский')
stud2.finished_courses = ['PHP']
stud2.courses_in_progress = ['Java', 'Web']
lect1 = Lecturer('Адилет', 'Асанкожоев')
lect1.courses_attached = ['Python', 'Web']
lect2 = Lecturer('Олег', 'Булыгин')
lect2.courses_attached = ['Java', 'Web']
rev1 = Reviewer('Екатерина', 'Великая')
rev1.courses_attached = ['Python', 'C++', 'Web']
rev2 = Reviewer('Анастасия', 'Некрасова')
rev2.courses_attached = ['Java', 'C++']

rev1.rate_hw(stud1, 'Python', 5)
rev1.rate_hw(stud1, 'Python', 4)
rev1.rate_hw(stud1, 'Python', 9)
rev1.rate_hw(stud1, 'Web', 5)
rev1.rate_hw(stud1, 'Web', 8)
rev1.rate_hw(stud1, 'Web', 10)

rev2.rate_hw(stud2, 'Java', 9)
rev2.rate_hw(stud2, 'Java', 8)
rev2.rate_hw(stud2, 'Java', 9)
rev2.rate_hw(stud2, 'Web', 7)
rev1.rate_hw(stud2, 'Web', 9)
rev2.rate_hw(stud2, 'Web', 6)

stud1.rate_lect(lect1, 'Python', 8)
stud1.rate_lect(lect1, 'Python', 10)
stud1.rate_lect(lect1, 'Python', 9)
stud1.rate_lect(lect1, 'Web', 8)
stud1.rate_lect(lect1, 'Web', 10)
stud1.rate_lect(lect1, 'Web', 9)
stud2.rate_lect(lect2, 'Java', 8)
stud2.rate_lect(lect2, 'Java', 10)
stud2.rate_lect(lect2, 'Java', 9)
stud2.rate_lect(lect2, 'Web', 8)
stud2.rate_lect(lect2, 'Web', 7)
stud2.rate_lect(lect2, 'Web', 6)



print(stud1)
print(stud2)
print(stud1 < stud2)
print()
print(lect1)
print(lect2)
print(lect1 > lect2)
print(mean_stud([stud1, stud2], 'Web'))
print(mean_lect([lect1, lect2], 'Web'))