'''
If the student does not have class at the moment, the GUI could present a personal class 
timetable for the student.

Input: [student_id]
Output: {course_name, course_code, venue,type,start_datetime,end_datetime}
'''
import mysql.connector
import  datetime
# from datetime import datetime

class GenerateTimetable:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="face_recognition")
    
    def get_timetable(self, student_id, timestamp):
        mycursor = self.conn.cursor(dictionary=True)
        sem_time = datetime.datetime(2021,1,10,00,00)
        now_time = datetime.datetime.strptime(timestamp,'%Y-%m-%d %H:%M:%S')
        d = []
        sem_timestamp = str(sem_time)
        # print(sem_time)
        # print(now_time)
        # print(type(sem_time))
        # print(type(now_time))

        # Show sem 1 courses only
        if now_time <= sem_time:
            mycursor.execute("SELECT C.course_name, C.course_code,\
                                L.venue,L.type,L.start_datetime,L.end_datetime\
                                FROM Enroll AS E, Course AS C, Lesson AS L\
                                WHERE E.student_id = %s AND C.course_code = E.course_code AND E.course_code = L.course_code\
                                AND L.start_datetime >= %s\
                                AND L.start_datetime <= %s\
                                ORDER BY L.start_datetime LIMIT 8", (student_id,timestamp,sem_timestamp))
        
        # Show sem 2 courses only
        else:
            mycursor.execute("SELECT C.course_name, C.course_code,\
                                    L.venue,L.type,L.start_datetime,L.end_datetime\
                                    FROM Enroll AS E, Course AS C, Lesson AS L\
                                    WHERE E.student_id = %s AND C.course_code = E.course_code AND E.course_code = L.course_code\
                                    AND L.start_datetime >= %s\
                                    AND L.start_datetime > %s\
                                    ORDER BY L.start_datetime LIMIT 8", (student_id,timestamp,sem_timestamp))

        for row in mycursor:
            d.append(row)
        return d