import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-NN5S5J8\SQLEXPRESS;'
                      'Database=Test;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
# N1
#CREATE
cursor.execute('''
               CREATE TABLE teacher
               (
                teacherId INTEGER PRIMARY KEY,
                saxeli nvarchar(50),
                gvari nvarchar(50),
                sqesi nvarchar(50),
                sagani nvarchar(50)
               )
               ''')
cursor.execute('''
               CREATE TABLE pupil
               (
                pupilId INTEGER PRIMARY KEY,
                saxeli nvarchar(50),
                gvari nvarchar(50),
                sqesi nvarchar(50),
                klasi INTEGER
               )
               ''')
cursor.execute('''
               CREATE TABLE pupil_teacher
               (
                pupil_teacherId INTEGER PRIMARY KEY,
                pupilId int FOREIGN KEY REFERENCES pupil(pupilId),
                teacherId int FOREIGN KEY REFERENCES teacher(teacherId)
               )
               ''')
#INSERT
cursor.execute('''
                INSERT INTO teacher (teacherId, saxeli, gvari, sqesi, sagani)
                VALUES
                (1, 'nino', 'samxaradze', 'md', 'matematika'),
                (2, 'mirian', 'kenia', 'mr', 'fizika'),
                (3, 'tamar', 'arabuli', 'md', 'qimia')
                ''')
cursor.execute('''
                INSERT INTO pupil (pupilId, saxeli, gvari, sqesi, klasi)
                VALUES
                (1, 'ana', 'yifiani', 'md', '10'),
                (2, 'giorgi', 'gamsaxurdia', 'md', '11'),
                (3, 'nata', 'melikishvili', 'md', '12'),
                (4, 'giorgi', 'javaxishvili', 'mr', '12')
                ''')
cursor.execute('''
                INSERT INTO pupil_teacher (pupil_teacherId, pupilId, teacherId)
                VALUES
                (1, 1, 1),
                (2, 1, 2),
                (3, 2, 3),
                (4, 2, 1),
                (5, 3, 1),
                (6, 3, 3),
                (7, 4, 2)
                ''')
#SELECT
cursor.execute("SELECT teacher.saxeli, teacher.gvari from teacher inner join pupil_teacher on "
               "teacher.teacherId = pupil_teacher.teacherId inner join pupil on pupil_teacher.pupilId "
               "= pupil.pupilId where pupil.saxeli = 'giorgi';")

for row in cursor:
    print(row)

conn.commit()
