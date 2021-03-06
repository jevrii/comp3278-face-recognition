'''
When a student login with his/her face, his/her information such as name, login time,
and welcome message will be presented in the graphics user interface (GUI).

input: [student_id]
output: {name, email, lessons[(course_code, datetime)]}
'''

import mysql.connector

class GetStudentInfoAndCourse:
    def __init__(self, user, passwd, database):
        self.conn = mysql.connector.connect(host="localhost", user=user, passwd=passwd, database=database)
        self.cursor = self.conn.cursor(dictionary=True)
    def get_info(self, student_id, timestamp):
        ret = {}
        select = "SELECT name, email_address FROM Student WHERE student_id=%s"
        self.cursor.execute(select, (student_id,))
        result = self.cursor.fetchall()

        ret['name'] = result[0]['name']
        ret['email'] = result[0]['email_address']

        select = "SELECT course_code, start_datetime, end_datetime, zoom_link, venue, teacher_msg from Lesson where course_code in\
                        (SELECT course_code from Enroll where student_id=%s)\
                        and ( (start_datetime BETWEEN %s AND date_add(%s, interval 1 hour)) or \
                        (%s BETWEEN start_datetime AND end_datetime) )"
        self.cursor.execute(select, (student_id, timestamp, timestamp, timestamp))
        result = self.cursor.fetchall()

        ret['lessons'] = result
        
        return ret
