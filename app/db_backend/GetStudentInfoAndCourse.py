'''
When a student login with his/her face, his/her information such as name, login time,
and welcome message will be presented in the graphics user interface (GUI).

input: [student_id]
output: {name, email, lessons[(course_code, datetime)]}
'''

import mysql.connector

class GetStudentInfoAndCourse:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="face_recognition")
        self.cursor = self.conn.cursor()
    def get_info(self, student_id, timestamp):
        ret = {}
        select = f"SELECT name, email_address FROM Student WHERE student_id=\"{student_id}\""
        self.cursor.execute(select)
        result = self.cursor.fetchall()

        ret['name'] = result[0][0]
        ret['email'] = result[0][1]

        select = f"SELECT course_code, start_datetime from Lesson where course_code in\
                        (SELECT course_code from Enroll where student_id={student_id})\
                        and start_datetime BETWEEN '{timestamp}' AND date_add('{timestamp}', interval 1 hour)"
        self.cursor.execute(select)
        result = self.cursor.fetchall()

        ret['lessons'] = result
        
        return ret
