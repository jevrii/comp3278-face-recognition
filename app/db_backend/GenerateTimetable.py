'''
If the student does not have class at the moment, the GUI could present a personal class 
timetable for the student.

Input: [student_id]
Output: {course_name, course_code, venue,type,start_datetime,end_datetime}
'''
import mysql.connector
class GenerateTimetable:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="face_recognition")
    
    def get_timetable(self, student_id, timestamp):
        mycursor = self.conn.cursor(dictionary=True)
        d = []
        mycursor.execute("SELECT C.course_name, C.course_code,\
                            L.venue,L.type,L.start_datetime,L.end_datetime\
                            FROM Enroll AS E, Course AS C, Lesson AS L\
                            WHERE E.student_id = %s AND C.course_code = E.course_code AND E.course_code = L.course_code\
                            AND L.start_datetime >= %s\
                            ORDER BY L.start_datetime LIMIT 5", (student_id,timestamp))
        for row in mycursor:
            d.append(row)
        return d