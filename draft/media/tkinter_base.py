import tkinter as tk

class CustomFrame(tk.Frame):
    """
    Ceci est la base pour créer sa propre frame. Complétez le constructeur et
    ajoutez les méthodes si nécessaire.
    """
    def __init__(self, master=None, cnf={}, **kw):
        tk.Frame.__init__(self, master, cnf, **kw)
