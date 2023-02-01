
"""storing paths and constants here.
Also, building some default base"""

from pathlib import Path
import random
import sqlite3

from string import ascii_letters




MAIN = "gradesJournal.db"

NAMES = "rand_names.txt"
SUBJECTS = ""

def input_int(invite: str = "int", min_: int =1, max_: int = 5):
    out = max_ + 1 
    while not out.isdigit() and not min_< out <max_:
        out = input(invite)
    return int(out)



def input_name_like(invite: str = "name"):
    out = "$placeholder"
    while not set(out).issubset(set(ascii_letters)):
        out = input(f'input {invite}')
    return out.capitalize()



def init_base():
    main = sqlite3.connect(MAIN)
    crs = main.cursor()
    crs.execute("CREATE TABLE students ("
                + 'pId INTEGER PRIMARY KEY, '
                + 'name TEXT, '
                + 'surname TEXT '
                + ');')
    crs.execute('CREATE TABLE subjects ( '
                + 'sId INTEGER  PRIMARY KEY, '
                + 'name TEXT UNIQUE);')
    main.commit()



def randomize_students():
    collection = open(NAMES).read().split('\n')
    names = []
    for i in range(100):
        names.append((
            random.choice(collection).split()[0],
            random.choice(collection).split()[1]))

    main = sqlite3.connect(MAIN)
    crs = main.cursor()
    for student in names:
        crs.execute(' '.join(('INSERT INTO',
        'students( name, surname)', 'VALUES'
        f'("{student[0]}", "{student[1]}" );')))
    main.commit()


def init_subjects():
    collection = ['olympic_icecream_munching','submerged_chess',
    'assembler_interface_design', 'dyplomatic_bombardment',
    'horoscopes']
    pick = random.sample(collection,k = 3)

    main = sqlite3.connect(MAIN)
    crs = main.cursor()

    for i in pick:
        crs.execute(' '.join(('INSERT INTO',
        'subjects( name)', 'VALUES'
        f'("{i}");')))
    
    
    students = list(crs.execute(' '.join(('SELECT','pId','FROM',
    'students',';'))))

    for subj in pick:
        crs.execute(' '.join(('CREATE TABLE', subj,'(',
        'stId INT,','grades TEXT',');')))
        for student in students:
            crs.execute(' '.join(('INSERT INTO',subj,'( stid, grades )',
            'VALUES', f'( {student[0]} , "" );')))
    main.commit()


def main():
    # if Path(MAIN).exists():
    #     print('delete old one first')
    #     return
    # init_base()
    # randomize_students()
    # init_subjects()
    return


if __name__ == "__main__":
    main()
