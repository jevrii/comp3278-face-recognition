import csv
import datetime
import random
import string

random.seed(3278)

with open('raw_cs_course.csv', newline='') as input_csvfile:
    with open('output_lesson.csv', 'w', newline='') as ouptut_csvfile:
        reader = csv.DictReader(input_csvfile, delimiter=',', quotechar='"')

        writer = csv.DictWriter(ouptut_csvfile, ['course_code', 'start_datetime', 'end_datetime', 'zoom_link', 'venue', 'type', 'teacher'])

        writer.writeheader()

        for row in reader:
            start_datetime_str = row['START DATE'] + ' ' + row['START TIME']
            cur_end_datetime_str = row['START DATE'] + ' ' + row['END TIME']
            end_datetime_str = row['END DATE'] + ' ' + row['END TIME']

            start_datetime = datetime.datetime.strptime(start_datetime_str, '%Y-%m-%d %H:%M')
            end_datetime = datetime.datetime.strptime(end_datetime_str, '%Y-%m-%d %H:%M')

            cur_start_datetime = start_datetime
            cur_end_datetime = datetime.datetime.strptime(cur_end_datetime_str, '%Y-%m-%d %H:%M')

            while cur_start_datetime < end_datetime:
                writer.writerow({'course_code': row['COURSE CODE'] + '_' + row['CLASS SECTION'],
                                'start_datetime': cur_start_datetime, 'end_datetime': cur_end_datetime,
                                'zoom_link': "https://hku.zoom.us/j/" + 
                                        "9" + ''.join(random.choices(string.digits, k=10)) +
                                        "?pwd=" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=32)), # generate zoom link??
                                'venue': row['VENUE'], 'type': 'Lecture', 'teacher': row['INSTRUCTOR']})
                cur_start_datetime += datetime.timedelta(days=7)
                cur_end_datetime += datetime.timedelta(days=7)
            # YYYY-MM-DD HH:MI:SS

courses = set()

with open('raw_cs_course.csv', newline='') as input_csvfile:
    with open('output_course.csv', 'w', newline='') as ouptut_csvfile:
        reader = csv.DictReader(input_csvfile, delimiter=',', quotechar='"')

        writer = csv.DictWriter(ouptut_csvfile, ['course_code', 'course_name'])

        writer.writeheader()

        for row in reader:
            course_code = row['COURSE CODE'] + '_' + row['CLASS SECTION'],
            course_dict = {'course_code': row['COURSE CODE'] + '_' + row['CLASS SECTION'],
                'course_name': row['COURSE TITLE']}
            if not course_code in courses:
                writer.writerow(course_dict)
                courses.add(course_code)
