

import sqlite3

from literals import MAIN, input_int, input_name_like

class Student():

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.grades = ''


    def add_mark(self, mark: int):
        core = sqlite3.connect(MAIN)
        crs = core.cursor()
        crs.execute('FROM subjects SELECT grades WHERE '
            + '')
        core.execute("")
        core.commit()
        print(self.name)

    def report(self):
        return self.grades
    
    def upload():
        # core = sqlite3.connect(MAIN)
        # crs = core.cursor()
        return

class Subject():

    def __init__(self, name):
        self.name = name

    def addToBook(self):
        core = sqlite3.connect(MAIN)
        crs = core.cursor()
        crs.execute('CREATE TABLE IF NOT EXISTS '
            + f'{self.name}' + ' ( '
            + 'student_fk INT, '
            + 'grades TEXT, '
            + 'FOREIGN KEY (student_fk) REFERENCES students( pId ) '
            + ');')
        student_list = list(crs.execute('SELECT pId FROM students'))
        for student_id in student_list:
            print(student_id)
        core.commit()


def student_add():
    return


def object_add():
    return


def student_evaluate():
    return


def student_reveal():
    return

def main():
    print()
    # q = Student(name="John",surname="Doe")
    # q.add_mark(input_int())
    che = Subject('chemistry')
    che.addToBook()

main()

