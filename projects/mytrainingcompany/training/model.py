"""
Module pour une représentation de formation sous forme d'objet.
"""

import sqlite3 as lite

conn = lite.connect("testdb.db")

cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS trainings ("
            "subject TEXT NOT NULL, "
            "duration INT NOT NULL, "
            "seats INT NOT NULL")

title = "Python, l'essentiel"
duration = 5
seats = 12

SQL_ADD_TRAINEE = ""
SQL_COUNT_TRAINEES_FOR_TRAINING = ""
SQL_GET_TRAINING = ""
name = ""
company = ""
training = ""

import sqlite3 as lite

conn = lite.connect("testdb.db")

cur.execute(SQL_ADD_TRAINEE, (name, company))
cur.execute(SQL_COUNT_TRAINEES_FOR_TRAINING, (training))



cur.execute("INSERT INTO trainings VALUES (?, ?, ?)",
            (title, duration, seats))

cur.execute("SELECT * FROM trainings WHERE duration=:duration",
            {duration:5})

try:
    with conn:
        cur = conn.cursor()
        cur.execute(SQL_ADD_EPISODE, (ep_number, season_number, title))
except lite.IntegrityError:
    raise ValueError(f"Episode {title} s{season_number}e{ep_number} axists")


class Venue:
    def __init__(self, capacity):
        self._capacity = capacity

        if self._capacity < 1:
            raise ValueError(f"Venue capacity too small {self._capacity}")

    def capacity(self):
        return self._capacity


class Student:
    def __init__(self, name: str, title:str = None, company: str = None):
        """
        Describes a student

        :param name: The student name
        :param company: The student's company name
        """
        self._name = name.capitalize()
        self.title = title
        self._company = company.capitalize() if company else None

    @property
    def name(self):
        return self._name

    @property
    def company(self):
        return self._company

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False

        return (self._name, self._company) == (other.name, other.company)


class Training:
    def __init__(self, subject: str, duration: int, price, max_seats: int = 12):
        """
        Describes a training

        :param subject: Subject of the training
        :param duration: Duration in days
        :param available_seats: maximum seats available for the training
        """

        self._duration = int(duration)
        if self._duration < 1:
            raise ValueError(f"Duration should be at least one (1) day : {self._duration}")

        self._seats = int(max_seats)
        if self._seats < 1:
            raise ValueError(f'The training should have at least one seat : {self._seats}')

        self._base_price = int(price)
        if self._base_price < 1:
            raise ValueError(f'Training price cannot be negative or null : {self._base_price}')

        self._subject = subject

    @property
    def subject(self):
        return self._subject

    @property
    def duration(self):
        return self._duration

    @property
    def seats(self):
        return self._seats


class scheduled_training:
    def __init__(self, training: Training, venue: Venue = None):
        self.training = training
        self.date
        self._students = []
        self._venue = venue

    def add_student(self, student: Student):
        if len(self.students) >= self.training.:
            raise ValueError("Training full, can't add student")

        self._students.append(student)

    def remove_student(self, student: Student):
        if student not in self._students:
            raise ValueError(f"Student {student.name} not in this training")

        self._students.remove(student)

    def remove_student_by_name(self, name: str) -> Student:
        """
        Remove a student by his name. Raises ValueError if no student with this name is present or if more than one is
        present.

        :param name: The name of the student
        :return: The student with the name
        :raises ValueError: if there is no student or more than one student with this name.
        """
        students_names = [student.name for student in self._students]
        name_occurences = students_names.count(name.capitalize())

        if name_occurences > 1:
            raise ValueError(f"More than one student with name {name}")
        elif name_occurences < 0:
            raise ValueError(f"No student with name {name}")
        else:
            return self._students.pop(students_names.index(name.capitalize()))

    def remove_students_for_company(self, company: str):
        """
        Remove all students for a given company.

        :param company: The company name.
        :return: A list of students removed which are from the company or an empty list if there is no student from that
        company.
        """
        students = [student for student in self._students if student.company == company.capitalize()]
        self._students = [student for student in self._students if student not in students]

        return students



