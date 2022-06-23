def get_averg_grade(dict):                  #получение среднего значения из всех значений в словаре
        nbr_grades = 0                      #кол-во значений
        avr_grd = 0                         #среднее значение
        for lst in list(dict.values()):        
            if isinstance(lst, list):       #если текущее значение в словаре - список    
                for item in lst:            #просуммировать все и посчитать кол-во
                    nbr_grades += 1
                    avr_grd += item
            else:                           #иначе текущее значение в словаре - число
                nbr_grades += 1             #так же добавить к сумме и кол-ву значений
                avr_grd += lst
        if nbr_grades > 0:                  #если есть найденные значения в словаре, то
            avr_grd = avr_grd / nbr_grades  #посчитать среднее значение и вернуть его
        return avr_grd


def lst_to_str(lst):                        #метод для формирования сроки со списком курсов
    if lst is None:
        return ''        
    str = ''    
    for item in lst:
        str += item + ', '       
    return str[:-2]

def avg_grade_hws_on_course(students, course):  #метод подсчёта среднего значения оценок за домашки
    avg_grade = 0
    students_on_course = 0
    for student in students:
        if course in student.courses_in_progress and course in student.grades.keys():
            avg_grade += sum(student.grades[course])/len(student.grades[course])
            students_on_course += 1
    if students_on_course > 0:
        avg_grade = avg_grade/students_on_course
    print("'{0}' course has average grade '{1}' of students's homeworks".format(course, avg_grade))

def avg_grade_lecturs_on_course(lecturers, course): #метод подсчёта среднего значения оценок за лекции
    avg_grade = 0
    lecturer_of_course = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached and course in lecturer.grades.keys():
            avg_grade += sum(lecturer.grades[course])/len(lecturer.grades[course])
            lecturer_of_course += 1
    if lecturer_of_course > 0:
        avg_grade = avg_grade/lecturer_of_course
    print("'{0}' course has average grade '{1}' of lecturers".format(course, avg_grade))


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.completed_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached \
                and grade > 0 and grade < 11:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return "error"
    
    
    def __str__(self):
        return "Name: {0}\nSurname: {1}\nAverage grade for homeworks: {2}\nCourses in progress: {3}\nComplited courses: {4}\n".format(\
            self.name, self.surname, get_averg_grade(self.grades), lst_to_str(self.courses_in_progress), lst_to_str(self.completed_courses))

    def __lt__(self, other):
        self_avg_grade = get_averg_grade(self.grades)
        other_avg_grade = get_averg_grade(other.grades)
        return self_avg_grade < other_avg_grade

    def __le__(self, other):
        self_avg_grade = get_averg_grade(self.grades)
        other_avg_grade = get_averg_grade(other.grades)
        return self_avg_grade <= other_avg_grade

    def __eq__(self, other):
        self_avg_grade = get_averg_grade(self.grades)
        other_avg_grade = get_averg_grade(other.grades)
        return self_avg_grade == other_avg_grade
    
    def __ne__(self, other):
        self_avg_grade = get_averg_grade(self.grades)
        other_avg_grade = get_averg_grade(other.grades)
        return self_avg_grade != other_avg_grade

    def __gt__(self, other):
        self_avg_grade = get_averg_grade(self.grades)
        other_avg_grade = get_averg_grade(other.grades)
        return self_avg_grade > other_avg_grade

    def __ge__(self, other):
        self_avg_grade = get_averg_grade(self.grades)
        other_avg_grade = get_averg_grade(other.grades)
        return self_avg_grade >= other_avg_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}        

    def __str__(self):          
        return "Name: {0}\nSurname: {1}\nAverage grade: {2}\n".format(self.name, self.surname, get_averg_grade(self.grades))

    def __lt__(self, other):
        self_avg_grade = get_averg_grade(self.grades)
        other_avg_grade = get_averg_grade(other.grades)
        return self_avg_grade < other_avg_grade

    def __le__(self, other):
        self_avg_grade = get_averg_grade(self.grades)
        other_avg_grade = get_averg_grade(other.grades)
        return self_avg_grade <= other_avg_grade

    def __eq__(self, other):
        self_avg_grade = get_averg_grade(self.grades)
        other_avg_grade = get_averg_grade(other.grades)
        return self_avg_grade == other_avg_grade
    
    def __ne__(self, other):
        self_avg_grade = get_averg_grade(self.grades)
        other_avg_grade = get_averg_grade(other.grades)
        return self_avg_grade != other_avg_grade

    def __gt__(self, other):
        self_avg_grade = get_averg_grade(self.grades)
        other_avg_grade = get_averg_grade(other.grades)
        return self_avg_grade > other_avg_grade

    def __ge__(self, other):
        self_avg_grade = get_averg_grade(self.grades)
        other_avg_grade = get_averg_grade(other.grades)
        return self_avg_grade >= other_avg_grade


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
        return "Name: {0}\nSurname: {1}\n".format(self.name, self.surname)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.completed_courses += ['Git']

better_student = Student('Stive', 'Mask', 'man')
better_student.courses_in_progress += ['Python']
better_student.courses_in_progress += ['C#']
better_student.completed_courses += ['Data Bases']

cool_reviewer = Reviewer('Cool', 'Reviewer')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(better_student, 'Python', 1)
cool_reviewer.rate_hw(better_student, 'Python', 2)
cool_reviewer.rate_hw(better_student, 'Python', 3)

cooler_reviewer = Reviewer('Cooler', 'Reviewer2')
cooler_reviewer.courses_attached += ['C#']
cooler_reviewer.rate_hw(better_student, 'C#', 9)
cooler_reviewer.rate_hw(better_student, 'C#', 8)
cooler_reviewer.rate_hw(better_student, 'C#', 7)

cool_lector = Lecturer('Cool', 'Lector')
cool_lector.courses_attached = ['Python']

best_student.rate_lector(cool_lector, 'Python', 10)

better_student.rate_lector(cool_lector, 'Python', 8)

cooler_lector = Lecturer('Cooler', 'Lecctor2')

cool_lector.courses_attached += ['C#']

better_student.rate_lector(cooler_lector, 'C#', 10)
better_student.rate_lector(cooler_lector, 'C#', 9)
better_student.rate_lector(cooler_lector, 'C#', 5)

print(cool_lector)
print(cooler_lector)
print(cool_reviewer)
print(cooler_reviewer)
print(best_student)
print(better_student)

print('testing students comparision: ')
if best_student < better_student:
    print ('yes')
else:
    print('no')

if best_student <= better_student:
    print ('yes')
else:
    print('no')

if best_student == better_student:
    print ('yes')
else:
    print('no')

if best_student != better_student:
    print ('yes')
else:
    print('no')

if best_student > better_student:
    print ('yes')
else:
    print('no')

if best_student >= better_student:
    print ('yes')
else:
    print('no')

print('testing lectures comparision: ')
if cool_lector < cooler_lector:
    print('yes')
else:
    print ('no')

if cool_lector <= cooler_lector:
    print('yes')
else:
    print ('no')

if cool_lector == cooler_lector:
    print('yes')
else:
    print ('no')

if cool_lector != cooler_lector:
    print('yes')
else:
    print ('no')

if cool_lector > cooler_lector:
    print('yes')
else:
    print ('no')
if cool_lector >= cooler_lector:
    print('yes')
else:
    print ('no')


students_list = []
students_list.append(best_student)
students_list.append(better_student)
avg_grade_hws_on_course(students_list, 'Python')

lecturers_list = []
lecturers_list.append(cool_lector)
lecturers_list.append(cooler_lector)
avg_grade_lecturs_on_course(lecturers_list, 'Python')