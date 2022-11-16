import sqlite3 as lite


class Training:
    def __init__(self, name, db_path="default.db"):
        self._db_path = db_path
        self._conn = lite.connect(db_path)

    def __del__(self):
        try:
            self._conn.close()
        except lite.Error:
            ... #  Connexion is already closed, nothing to do

    def add_student(self, student):
        pass