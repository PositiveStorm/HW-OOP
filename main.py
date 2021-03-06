class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.lecture_grades = {}
        self.avg_grade = float()


    def rate_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress or course in lecturer_courses_in_progress:
            if course in lecturer.rate:
                lecturer.rate[course] += [rate]
            else:
                lecturer.rate[course] = [rate]
        else:
            return 'Ошибка'


    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.avg_grade < other.avg_grade

    def __str__(self):

        for course in self.grades:
            self.avg_grade = round(sum(self.grades[course]) / len(self.grades[course]), 1)
            break
        text = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за дз: {self.avg_grade} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return text

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses_in_progress = []
        self.rate = {}
        self.avg_rate = float()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.avg_rate < other.avg_rate

    def __str__(self):
        for course in self.rate:
            self.avg_rate = sum(self.rate[course]) / len(self.rate[course])
            break
        text = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avg_rate}'
        return text



class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        text = f'Имя: {self.name} \nФамилия: {self.surname}'
        return text


def avg_st(student_list, course):
    sum_grades = 0
    counter = 0
    for student in students_list:
        if course in student.grades:
            sum_grades += sum(student.grades[course]) / len(student.grades[course])
            counter += 1
    return round(sum_grades / counter, 2)

def avg_lect(lecturers_list, course):
    sum_rates = 0
    counter = 0
    for lecturer in lecturers_list:
        if course in lecturer.rate:
            sum_rates += sum(lecturer.rate[course]) / len(lecturer.rate[course])
            counter += 1
    return round(sum_rates / counter, 2)

best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']



cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)


cool_lecturer = Lecturer('Mike', 'Vazovski')
cool_lecturer.courses_in_progress += ['Python']

best_student.rate_lecturer(cool_lecturer, 'Python', 4)
best_student.rate_lecturer(cool_lecturer, 'Python', 3)
best_student.rate_lecturer(cool_lecturer, 'Python', 1)

print(cool_lecturer.rate)

best_student1 = Student('Sabirova', 'Polina', 'female')
best_student1.courses_in_progress += ['Python']
best_student1.finished_courses += ['Введение в программирование']

cool_reviewer1 = Reviewer('Sally', 'Lokhart')
cool_reviewer1.courses_attached += ['Python']

cool_reviewer1.rate_hw(best_student1, 'Python', 7)
cool_reviewer1.rate_hw(best_student1, 'Python', 4)
cool_reviewer1.rate_hw(best_student1, 'Python', 9)

best_student1.rate_lecturer(cool_lecturer, 'Python', 10)
best_student1.rate_lecturer(cool_lecturer, 'Python', 7)
best_student1.rate_lecturer(cool_lecturer, 'Python', 5)
cool_lecturer1 = Lecturer('Mona', 'Mia')
cool_lecturer1.courses_in_progress += ['Python']
best_student1.rate_lecturer(cool_lecturer1, 'Python', 5)
best_student1.rate_lecturer(cool_lecturer1, 'Python', 10)
best_student1.rate_lecturer(cool_lecturer1, 'Python', 9)
print(best_student1.grades)
print()

print(cool_lecturer.rate)
print()
print(cool_lecturer1.rate)
print()
print(cool_reviewer)
print()
print(cool_reviewer1)
print()
print(cool_lecturer)
print()
print(cool_lecturer1)
print()
print(best_student)
print()
print(best_student1)
print()
print(best_student < best_student1)
print()
print(cool_lecturer < cool_lecturer1)
print()

students_list = [best_student, best_student1]
print(avg_st(students_list, 'Python'))

lecturers_list = [cool_lecturer, cool_lecturer1]
print(avg_lect(lecturers_list, 'Python'))