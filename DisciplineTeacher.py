class Teacher:
    def __init__(self, name, education, experience):
        self._name = name           # Защищённый атрибут имени
        self._education = education   # Защищённый атрибут образования
        self._experience = experience  # Защищённый атрибут опыта работы

    # Геттеры
    @property
    def name(self):
        return self._name

    @property
    def education(self):
        return self._education

    @property
    def experience(self):
        return self._experience

    # Сеттер для опыта работы
    @experience.setter
    def experience(self, value):
        self._experience = value

    # Метод для получения информации об учителе
    def get_teacher_data(self):
        return f"{self._name}, образование {self._education}, опыт работы {self._experience} лет."

    # Метод для добавления оценки
    def add_mark(self, student_name, mark):
        return f"{self._name} поставил оценку {mark} студенту {student_name}."

    # Метод для удаления оценки
    def remove_mark(self, student_name, mark):
        return f"{self._name} удалил оценку {mark} студенту {student_name}."

    # Метод для консультации
    def give_a_consultation(self, class_name):
        return f"{self._name} провел консультацию в классе {class_name}."


class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self._discipline = discipline  # Защищённый атрибут предмета
        self._job_title = job_title      # Защищённый атрибут должности

    # Геттер для discipline
    @property
    def discipline(self):
        return self._discipline

    # Геттер для job_title
    @property
    def job_title(self):
        return self._job_title

    # Сеттер для job_title
    @job_title.setter
    def job_title(self, value):
        self._job_title = value

    # Адаптация метода get_teacher_data
    def get_teacher_data(self):
        base_data = super().get_teacher_data()
        return f"{base_data}\nПредмет {self._discipline}, должность {self._job_title}."

    # Адаптация метода add_mark
    def add_mark(self, student_name, mark):
        return f"{self._name} поставил оценку {mark} студенту {student_name}. Предмет: {self._discipline}"

    # Адаптация метода remove_mark
    def remove_mark(self, student_name, mark):
        return f"{self._name} удалил оценку {mark} студенту {student_name}. Предмет: {self._discipline}"

    # Адаптация метода give_a_consultation
    def give_a_consultation(self, class_name):
        return f"{self._name} провел консультацию в классе {class_name}. По предмету {self._discipline} как {self._job_title}"


# Пример использования

teacher = DisciplineTeacher("Иван Петров", "БГПУ", 4, "Химия", "Директор")

print(teacher.get_teacher_data())
print(teacher.add_mark("Николай Иванов", 4))
print(teacher.remove_mark("Дмитрий Сидоров", 3))
print(teacher.give_a_consultation("10 Б"))