"""
Ce module montre l'utilisation d'une dataclass pour la manipulation de données
complexes.
"""
import dataclasses as dc


@dc.dataclass()
class Training:
    name: str
    duration: int
    students: list = dc.field(default_factory=list)
    seats: int = 12
    price: int = 2500

    def add_student(self, student):
        if student in self.students:
            raise ValueError("Student already in training")

        self.students.append(student)