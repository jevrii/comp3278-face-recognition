import mysql.connector
'''
course information, classroom address, teacher’s message, links of Zoom
tutorial/lecture notes, other course materials and so on and so forth will be presented in the GUI.

input: [course_code, start_datetime]
output: {material_name, material_link}
'''

class GetLessonMaterial:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="face_recognition")

    def get_info(self, course_code):
        mycursor = self.conn.cursor(dictionary=True)
        d = []
        mycursor.execute("SELECT CM.material_name,CM.material_link FROM CourseMaterial AS CM\
                                           WHERE CM.course_code = %s", (course_code,))
        for row in mycursor:
            d.append(row)
        return d
