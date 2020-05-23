"""
Ce module montre l'utilisation d'un namedtuple pour la manipulation de données
complexes.
"""
from collections import namedtuple

Training = namedtuple('Training',
                      ['name', 'duration', 'students', 'seats', 'price'],
                      defaults=[[], 12, 2500])

#  Création d'une formation
python = Training("Python", 5)

#  Accès aux champs de la donnée
print(python[0], python[1])
print(python.name, python.duration)

print(python)

# Création d'une formation avec un des paramètre par défaut modifié.
print(Training("Django", 4, price=2000))