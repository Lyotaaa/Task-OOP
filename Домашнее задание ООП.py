class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        # self.student_rating = []

    def evaluating_lecturers(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'    
    
    def average_grade_for_homework(self):
        if not self.grades:
            return 0.0
        grade_list = []
        for value in self.grades.values():
            grade_list.extend(value)
        return (sum(map(int, grade_list)) / len(grade_list))

    def __str__(self):
        res = f'Имя: {self.name}\n' \
            f'Фамилия: {self.surname}\n' \
            f'Средняя оценка за домашнее задание: {self.average_grade_for_homework()}\n' \
            f'Курсы в процессе обучения: {self.courses_in_progress}\n' \
            f'Завершенные курсы: {self.finished_courses}\n'
        return res 
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_grade_for_homework() < other.average_grade_for_homework()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def lecture_evaluation(self):
        if not self.grades:
            return 0.0
        grade_list = []
        for value in self.grades.values():
            grade_list.extend(value)
        return sum(map(int, grade_list)) / len(grade_list)

    def __str__(self):
        res = f'Имя: {self.name}\n' \
            f'Фамилия: {self.surname}\n' \
            f'Средняя оценка за лекции: {self.lecture_evaluation()}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.lecture_evaluation() < other.lecture_evaluation()

class Reviewers(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        res = f'Имя: {self.name}\n' \
            f'Фамилия: {self.surname}\n'
        return res

# class Student
first_student = Student('Ivan', 'Ivanov', 'man')
first_student.courses_in_progress += ['Python']
first_student.finished_courses += ['GIT']

second_student = Student('Alexei', 'Alexeyev', 'man')
second_student.courses_in_progress += ['Python']
second_student.finished_courses += ['GIT']

# class Lecturer
first_lecturer = Lecturer('Pyotr', 'Petrov')
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Pavel', 'Pavlov')
second_lecturer.courses_attached += ['Python']

# class Reviewers
first_mentor = Reviewers('Maxim', 'Maksimov') 
first_mentor.courses_attached += ['Python']

second_mentor = Reviewers('Andrei', 'Andreev') 
second_mentor.courses_attached += ['Python']

# class Student
first_student.evaluating_lecturers(first_lecturer, 'Python', '10')
first_student.evaluating_lecturers(first_lecturer, 'Python', '9')
first_student.evaluating_lecturers(first_lecturer, 'Python', '8')

first_student.evaluating_lecturers(second_lecturer, 'Python', '7')
first_student.evaluating_lecturers(second_lecturer, 'Python', '6')
first_student.evaluating_lecturers(second_lecturer, 'Python', '5')

second_student.evaluating_lecturers(first_lecturer, 'Python', '7')
second_student.evaluating_lecturers(first_lecturer, 'Python', '6')
second_student.evaluating_lecturers(first_lecturer, 'Python', '5')

second_student.evaluating_lecturers(second_lecturer, 'Python', '4')
second_student.evaluating_lecturers(second_lecturer, 'Python', '3')
second_student.evaluating_lecturers(second_lecturer, 'Python', '2')

# class Reviewers
first_mentor.rate_hw(first_student, 'Python', '6')
first_mentor.rate_hw(first_student, 'Python', '5')
first_mentor.rate_hw(first_student, 'Python', '4')

first_mentor.rate_hw(second_student, 'Python', '3')
first_mentor.rate_hw(second_student, 'Python', '2')
first_mentor.rate_hw(second_student, 'Python', '1')

second_mentor.rate_hw(first_student, 'Python', '9')
second_mentor.rate_hw(first_student, 'Python', '8')
second_mentor.rate_hw(first_student, 'Python', '7')

second_mentor.rate_hw(second_student, 'Python', '6')
second_mentor.rate_hw(second_student, 'Python', '5')
second_mentor.rate_hw(second_student, 'Python', '4')

def comparison_grades(a, b):
    res_1 = a > b
    res_2 = a < b
    if res_1 == True:
        return f'{a.name} {a.surname} набрал больше балов, чем {b.name} {b.surname}'
    elif res_2 == True:
        return f'{b.name} {b.surname} набрал больше балов, чем {a.name} {a.surname}'
        
student_list = [first_student, second_student]
lecturer_list = [first_lecturer, second_lecturer]

def student_rating(student_list, course):
    total = []
    for student in student_list:
        for course in student.grades.values():
            total.extend(course)
    return sum(map(int, total)) / len(total)

def lecturer_rating(lecturer_list, course):
    total = []
    for lecturer in lecturer_list:
        for course in lecturer.grades.values():
            total.extend(course)
    return sum(map(int, total)) / len(total)


print(f'Список студентов:\n{first_student}\n{second_student}')
print(f'Список лекторов:\n{first_lecturer}\n{second_lecturer}')
print(f'Список ревью:\n{first_mentor}\n{second_mentor}')

print(f'Результат сравнения студентов:\n{comparison_grades(first_student, second_student)}\n')
print(f'Результат сравнения лекторов:\n{comparison_grades(first_lecturer, second_lecturer)}\n')

print(f'Средняя оценка для всех студентов по курсу {"Python"}: {student_rating(student_list, "Python")}\n')
print(f'Средняя оценка для всех лекторов по курсу {"Python"}: {lecturer_rating(lecturer_list, "Python")}')