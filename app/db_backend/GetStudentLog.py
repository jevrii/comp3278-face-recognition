import mysql.connector
import  datetime

class GetStudentLog:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="face_recognition")

    def get_info(self, course_code):
        mycursor = self.conn.cursor(dictionary=True)
        d = []
        mycursor.execute("SELECT S.name,S.student_id, MAX(LS.last_heartbeat)\
                             FROM Enroll AS E, LoginSessions AS LS, Student AS S\
                                           WHERE E.course_code = %s\
                                               AND E.student_id = LS.student_id\
                                                   AND E.student_id = S.student_id\
                                                       GROUP BY S.student_id\
                                                       ORDER BY S.student_id", (course_code,))
        for row in mycursor:
            d.append(row)
        return d
