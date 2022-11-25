# 1. Создать класс Person с атрибутами fullname, age, is_married
class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    # 2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке
    def introduce_myself(self):
        print(f'Person: {self.fullname} is {self.age}.He/She is {self.is_married}.')

# 3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом
# marks, который был бы словарем, где ключ это название урока, а значение - оценка.
class Student(Person):
    def __init__(self,fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    # 4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам
    def average_rating(self):
        average_all = sum(self.marks)/len(self.marks)
# 5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience.

class Teacher(Person):
    salary = 10000 # 6. Добавить в класс Teacher атрибут уровня класса salary
    def __init__(self,fullname, age, is_married,experience):
        super().__init__(fullname, age, is_married)
        self.experiences = experience
# 7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей
# формуле: к стандартной зарплате прибавляется бонус 5% за каждый год опыта свыше 3х лет.
    def calculation(self):
        if self.experiences > 3:
            new_salary = self.salary + self.salary*(0.05*(self.experiences-3))
            return new_salary
        else:
            return self.salary

# 8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату
Teacher_1 = Teacher(fullname='Asanov Asan', age = 29, is_married = 'yes',experience = 6)

print(f'Fullname of Teacher: {Teacher_1.fullname}\n'
      f' Age: {Teacher_1.age}\n'
      f' Married:{Teacher_1.is_married}\n' 
      f'experience: {Teacher_1.experiences}\n'
      f' salary: {Teacher_1.calculation()}\n')

# 9. Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики
# добавляются в список и список возвращается функцией как результат.
def create_students():
    student_1 = Student(fullname = 'zizi zuzu', age = 20, is_married = 'yes', marks =
    {'Math':5,'English':5,'Russian':4,'physics':3})
    student_2 = Student(fullname='xixi cucu', age=19, is_married='No',marks =
    {'Math': 5, 'English': 3, 'Russian': 4, 'physics': 4})
    student_3 = Student(fullname='lolo pepe', age=23, is_married='no', marks =
    {'Math': 2, 'English': 5, 'Russian': 5, 'physics': 3})
    listOfStudents = [student_1,student_2,student_3]
    return listOfStudents

# 10. Вызвать функцию create_students
students = create_students()
# и через цикл распечатать всю информацию о каждом ученике с его оценками по каждому предмету.
# Также рассчитать его среднюю оценку по всем предметам

for i in students:  # <__main__.Student object at 0x0000023BABA46430>
    list1 = []
    for j in i.marks.values(): # j=2,5,5,3(каждая)   i.marks.values()= dict_values([2, 5, 5, 3])
        list1.append(j) # j=2,5,5,3(каждая)
    print(f'Fullname of Student: {i.fullname}\n'
              f'Age: {i.age}\n'
              f'Married: {i.is_married}\n'
              f'Average marks: {sum(list1)/len(list1)}\n')

''' clarification for myself:
for i in students:
    print(i)    # ссылка на объект
    # <__main__.Student object at 0x0000023BABA46430>
    print(i.marks)  # сам объект
    # {'Math': 2, 'English': 5, 'Russian': 5, 'physics': 3}
    print(i.marks.values())  #значение объекта(в нашем случае словаря)
    # dict_values([2, 5, 5, 3])
'''

















