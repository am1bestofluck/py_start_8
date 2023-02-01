

import pprint
import sqlite3
import sys

from literals import MAIN, input_int, input_name_like


class Student():

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.grades = "''"

    def add_mark(self, mark: int, subject: str = None):
        
        core = sqlite3.connect(MAIN)
        crs = core.cursor()

        if not subject:
            subject = input('subject to evaluate') # предмет
        all_subjects = dict(enumerate(list(crs.execute("SELECT name FROM subjects"))))



        student_id = crs.execute(' '.join(('SELECT', 'pID', 'FROM students',
                                       'WHERE', f'name LIKE "{self.name}" AND', f'surname LIKE "{self.surname}";')))
        list_it = list(student_id)
        if list_it == []:
            print("no match")
            return
        if len(list_it) > 1:
            print("ВОЗМОЖНЫ РАЗНОЧТЕНИЯ!")
        student_id = list_it[0][0]


        crs.execute('SELECT name FROM  '
                    + '')
        core.execute("")
        core.commit()
        print(self.name)

    def report(self):
        return self.grades

    def upload(self) -> None:
        core = sqlite3.connect(MAIN)
        crs = core.cursor()
        crs.execute(' '.join(('INSERT INTO',
                              'students( name, surname)', 'VALUES'
                              f'("{self.name}", "{self.surname}" );')))
        core.commit()
        new_id = max(list(crs.execute("SELECT pId FROM students")))
        all_subjects = list(crs.execute("SELECT name FROM subjects"))
        for add_student in all_subjects:
            crs.execute(' '.join(('INSERT INTO', add_student[0],
                                  '(stId, grades) VALUES (', f'{new_id[0]},{self.grades}', ');'
                                  )))
        core.commit()
        return None


class Subject():

    def __init__(self, name):
        self.name = name

    def addToBook(self):
        core = sqlite3.connect(MAIN)
        crs = core.cursor()
        crs.execute('CREATE TABLE IF NOT EXISTS '
                    + f'{self.name}' + ' ( '
                    + 'stId INT, '
                    + 'grades TEXT, '
                    + 'FOREIGN KEY (stId) REFERENCES students( pId ) '
                    + ');')
        crs.execute(
            ' '.join((f'INSERT INTO subjects(name) VALUES ("{self.name}");',)))
        student_list = list(crs.execute('SELECT pId FROM students'))
        for student_id in student_list:
            crs.execute(' '.join(('INSERT INTO',
                                  f'{self.name}( stId, grades)', 'VALUES'
                                  f'("{student_id[0]}", "");')))
        core.commit()


def student_add():
    person = Student(name=input_name_like("name"),
                     surname=input_name_like("surname"))
    person.upload()


def object_add():
    tmp = Subject(input_name_like("new subject"))
    tmp.addToBook()


def students_reveal() -> list:
    core = sqlite3.connect(MAIN)
    crs = core.cursor()
    tmp = list(crs.execute('SELECT name, surname FROM students;'))
    return [f'{name[0]} {name[1]}' for name in tmp]


def student_report() -> dict:
    out = {}
    tmp = Student(
        name=input_name_like('name').capitalize(),
        surname=input_name_like('surname').capitalize())
    core = sqlite3.connect(MAIN)
    crs = core.cursor()
    student_id = crs.execute(' '.join(('SELECT', 'pID', 'FROM students',
                                       'WHERE', f'name LIKE "{tmp.name}" AND', f'surname LIKE "{tmp.surname}";')))
    list_it = list(student_id)
    if list_it == []:
        print("no match")
        return
    if len(list_it) > 1:
        print("ВОЗМОЖНЫ РАЗНОЧТЕНИЯ!")
    student_id = list_it[0][0]
    subjects_list = [i[0] for i in
                     list(crs.execute('SELECT name FROM subjects;'))]
    for key_ in subjects_list:
        out[key_] = [i for i in
                     list(crs.execute(f"SELECT grades FROM '{key_}';"))[0]]
    return out

def quit_():
    sys.exit()


def main():
    # student_add()
    # object_add()
    # pprint.pp(students_reveal())
    # student_report()
    
    quit_()
    return


main()
