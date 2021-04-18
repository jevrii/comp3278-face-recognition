'''
If the student does not have class at the moment, the GUI could present a personal class 
timetable for the student.

Input: [student_id, timestamp]
Output: (nothing)
'''
import mysql.connector
class GenerateLoginLog:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="face_recognition")
    
    def login_record(self, student_id, session_id):
        mycursor = self.conn.cursor(dictionary=True)
        mycursor.execute("INSERT INTO `LoginSessions`(`session_id`, `student_id`, `login_timestamp`, `last_heartbeat`) VALUES\
                            (%s,%s,NOW(3),NOW(3))", (session_id,student_id))
        self.conn.commit()

    def heartbeat(self, session_id):
        mycursor = self.conn.cursor(dictionary=True)
        mycursor.execute("UPDATE `LoginSessions` SET `last_heartbeat`=NOW(3) WHERE `session_id`=%s",\
                            (session_id,))
        self.conn.commit()
