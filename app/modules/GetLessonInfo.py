import mysql.connector
'''
course information, classroom address, teacher’s message, links of Zoom
tutorial/lecture notes, other course materials and so on and so forth will be presented in the GUI.
'''

class GetLessonInfo:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="face_recognition")

    def get_info(self, input_list):
        mycursor = self.conn.cursor(dictionary=True)
        mycursor.execute(mycursor.execute("SELECT C.course_name, C.course_code,L.venue,L.zoom_link,CM.material_name,CM.material_link\
                                           FROM Course AS C, Lesson AS L, CourseMaterial AS CM\
                                           WHERE L.course_code = C.course_code \
                                               AND L.course_code = %s AND start_datetime = %s", input_list))
        # for row in mycursor:
        #     print("course_name",row['course_name'])
        return mycursor

    def test(self):
        print("hi")
