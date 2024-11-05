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
        return f"{self._name}, образование: {self._education}, опыт работы: {self._experience} лет."

    # Метод для добавления оценки
    def add_mark(self, student_name, mark):
        return f"{self._name} поставил оценку {mark} студенту {student_name}."

    # Метод для удаления оценки
    def remove_mark(self, student_name, mark):
        return f"{self._name} удалил оценку {mark} студенту {student_name}."

    # Метод для консультации
    def give_a_consultation(self, class_name):
        return f"{self._name} провел консультацию в классе {class_name}."

    # Собственный метод: метод для описания процесса обучения
    def teach(self, student_name):
        return f"{self._name} проводит уроки для студента {student_name}."


class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self._discipline = discipline  # Защищённый атрибут предмета
        self._job_title = job_title      # Защищённый атрибут должности

    # Геттеры для discipline и job_title
    @property
    def discipline(self):
        return self._discipline

    @property
    def job_title(self):
        return self._job_title

    # Метод для получения полной информации о преподавателе
    def get_full_info(self):
        base_info = self.get_teacher_data()
        return f"{base_info}, предмет: {self._discipline}, должность: {self._job_title}."

    # Переопределение метода add_mark, чтобы добавить дополнительную функциональность
    def add_mark(self, student_name, mark):
        super_add_mark = super().add_mark(student_name, mark)
        return f"{super_add_mark} Преподавание предмета: {self._discipline}."

    # Собственный метод: метод для организации внеклассных мероприятий
    def organize_event(self, event_name):
        return f"{self._name} организует мероприятие {event_name}."


# Пример использования классов

teacher = Teacher("Иван Иванович", "высшее", 10)
print(teacher.get_teacher_data())
print(teacher.add_mark("Анастасия", 5))
print(teacher.give_a_consultation("11А"))
print(teacher.teach("Максим"))

discipline_teacher = DisciplineTeacher("Сергей Петрович", "высшее", 15, "математика", "учитель")
print(discipline_teacher.get_full_info())
print(discipline_teacher.add_mark("Ольга", 4))
print(discipline_teacher.organize_event("Научная конференция"))