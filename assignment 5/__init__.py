import struct

def main():

    while True:
        a="Data Management System Menu:"
        print((len(a)+1)*'*')
        print(a,end='')
        print('*')
        print((len(a)+1)*'*')
        print("1. Quit")
        print("2. Add Student")
        print("3. View Student")
        print("4. Edit Student")
        print("5. Delete Student")
        print("6. List Students by Semester")
        print("7. List Students by Name")
        print("8. Print Students List")
        print("9. Add Grade")
        print("10. Import Grades from File")
        print("11. View Grades of a Student")
        print("12. Edit Grades of a Student")
        print("13. Delete Grades of a Student")
        print("14. List Student Wise Grade of Courses")
        print("15. List Course Wise Grade of Students")
        print("16. Award Sheet")
        print("17. Summary Sheet")
        print("18. Transcripts for a Range of Students")
        x = int(input("Enter your choice: "))
        print('-'*70)
        if x == 1:
            print('Thankyou for using our system! ')
            break
        elif x == 2: adding()  #done
        elif x == 3: student_by_rollnumber()  #done
        elif x == 4: edit_by_rollnumber()  #done
        elif x == 5: delete_by_rollnumber()  #done
        elif x == 6: lst_by_semester()  #done
        elif x == 7: students_by_name() #done
        elif x == 8: display()  #done
        elif x == 9: add_grade()  #done
        elif x == 10: import_grade() #done
        elif x == 11: view_grade()  #done
        elif x == 12: edit_grade()  #done
        elif x == 13: delete_grade()  #done
        elif x == 14: list_studentwise_grade()  #done
        elif x == 15: list_coursewise_grade() #done
        elif x == 16: award_sheet() #done
        elif x == 17: summary_sheet() #done
        elif x == 18: transcripts() #done
        else: print('Invalid Option. Yo must choose from 1-18 either')
        print('-'*70)



def do_exist(roll):
    format_str = '11s30s2sif11s'
    with open('RECORD', 'rb') as f:
        while True:
            data = f.read(struct.calcsize(format_str))
            if not data:
                break
            roll_no, _, _, _, _, _ = struct.unpack(format_str, data)
            if roll_no.decode() == roll:
                return True
    return False

def student_by_rollnumber():
    roll = input('Enter Roll Number for which you need information: ').capitalize().ljust(11)
    if not do_exist(roll):
        print('Record Not Found')
        return
    format_str = '11s30s2sif11s'
    with open('RECORD', 'rb') as f:
        while True:
            data = f.read(struct.calcsize(format_str))
            if not data:
                break
            roll_no, name, dep, sem, percentage, phone = struct.unpack(format_str, data)
            if roll_no.decode() == roll:
                print('DATA OF ROLL NO.' + roll.strip() + ' IS AS FOLLOWS:')
                print(f'Name: {name.decode()}')
                print(f'Department: {dep.decode()}')
                print(f'Semester: {sem}')
                print(f'Percentage: {percentage}%')
                print(f'Phone Number: {phone.decode()}')
                print('-'*70)
                return

def delete_by_rollnumber():
    roll = input('Enter Roll Number for which you need to delete information: ').capitalize().ljust(11)
    if not do_exist(roll):
        print('Record Not Found')
        return
    format_str = '11s30s2sif11s'
    x = b''

    with open('RECORD', 'rb') as f:
        while True:
            data = f.read(struct.calcsize(format_str))
            if not data:
                break

            roll_no, name, dep, sem, percentage, phone = struct.unpack(format_str, data)
            if roll_no.decode() != roll:
                x += data

    with open('RECORD', 'wb') as f:
        f.write(x)

    print(f'The record with Roll Number {roll.strip()} has been deleted.')

def edit_by_rollnumber():
    roll = input('Enter Roll Number for which you need to edit information: ').capitalize().ljust(11)
    if not do_exist(roll):
        print('Record Not Found')
        return
    format_str = '11s30s2sif11s'
    with open('RECORD', 'rb') as f:
        lst = []
        while True:
            data = f.read(struct.calcsize(format_str))
            if not data:
                break
            lst.append(data)
    for i in lst:
        roll_no, name, dep, sem, percentage, phone = struct.unpack(format_str, i)
        if roll_no.decode() == roll:
            print('DATA OF ROLL NO.' + roll.strip() + ' IS AS FOLLOWS:')
            print(f'Name: {name.decode()}')
            print(f'Department: {dep.decode()}')
            print(f'Semester: {sem}')
            print(f'Percentage: {percentage}%')
            print(f'Phone Number: {phone.decode()}')
            print('-'*70)
            print('Enter New Data')
            name = input('Enter Name: ').capitalize().ljust(30)
            dep = input('Enter New Department Code(SE/CS/DS/IT): ').capitalize().ljust(2)
            sem = int(input('Enter New Semester(in number): '))
            percentage = float(input('Enter last Semester Percentage: '))
            phone = input('Enter Phone Number: ')
            while len(phone) != 11:
                print('Invalid Phone Number')
                phone = input('Enter PhoneNumber: ')
            data = struct.pack(format_str, roll.encode(), name.encode(), dep.encode(), sem, percentage, phone.encode())
            lst[lst.index(i)] = data
            break
    with open('RECORD', 'wb') as f:
        f.write(b''.join(lst))
    print('Record Edited Successfully.')

def lst_by_semester():
    sem = int(input('Enter Semester for which you need information: '))
    format_str = '11s30s2sif11s'
    with open('RECORD', 'rb') as f:
        c = 0
        while True:
            data = f.read(struct.calcsize(format_str))
            if not data:
                break
            roll_no, name, dep, semester, percentage, phone = struct.unpack(format_str, data)
            if semester == sem:
                c += 1
                if c == 1: print(f'Record of all Students enrolled in {sem} semester is as follows:')
                print('Roll No.' + roll_no.decode().strip())
                print(f'Name: {name.decode()}')
                print(f'Department: {dep.decode()}')
                print(f'Percentage: {percentage}%')
                print(f'Phone Number: {phone.decode()}')
                print('-'*70)
        if c == 0: print('No Student is enrolled in ' + str(sem) +' semester!');
    return

def adding():
    format_str = '11s30s2sif11s'
    roll = input('Enter Roll Number: ').capitalize().ljust(11)
    if do_exist(roll):
        print('Roll Number Already Exists')
        return
    name = input('Enter Name: ').capitalize().ljust(30)
    dep = input('Enter Department Code(SE/CS/DS/IT):').capitalize().ljust(2)
    sem = int(input('Enter Semester(in number): '))
    percentage = float(input('Enter last Semester Percentage: '))
    phone = input('Enter Phone Number: ')
    while len(phone) != 11:
        print('Invalid Phone Number')
        phone = input('Enter PhoneNumber: ')
    data = struct.pack(format_str, roll.encode(), name.encode(), dep.encode(), sem, percentage, phone.encode())
    with open('RECORD', 'ab') as f:
        f.write(data)
    print('Record Added Successfully')

def students_by_name():
    format_str = '11s30s2sif11s'
    students = []
    with open('RECORD', 'rb') as f:
        while True:
            data = f.read(struct.calcsize(format_str))
            if not data:
                break
            roll_no, name, dep, sem, percentage, phone = struct.unpack(format_str, data)
            students.append(name.decode())
    if students == []:
        print('No Student Found')
        return
    print('All Students are as follows: ')
    for i, j in enumerate(students):
        print(f'{i+1}: {j} ')
    return

def display():
    format_str = '11s30s2sif11s'
    with open('RECORD', 'rb') as f:
        while True:
            data = f.read(struct.calcsize(format_str))
            if not data:
                break
            roll, name, dep, sem, percentage, phone = struct.unpack(format_str, data)
            print(f'Roll Number: {roll.decode()}')
            print(f'Name: {name.decode()}')
            print(f'Department: {dep.decode()}')
            print(f'Semester: {sem}')
            print(f'Percentage: {percentage}%')
            print(f'Phone Number: {phone.decode()}')
            print('-'*70)

def grade_already_present(roll, course):
    format_str = '11s20sf'
    with open('GRADE','rb') as f:
        while True:
            data = f.read(struct.calcsize(format_str))
            if not data:
                break
            roll_no, course_name, percentage = struct.unpack(format_str, data)
            if roll_no.decode() == roll and course_name.decode() == course:
                return True

def add_grade():
    format_str = '11s20sf'
    roll = input('Enter Roll Number for which Grade would you like to add: ').capitalize().ljust(11)
    if not do_exist(roll):
        print('No Such Roll number Found')
        return
    course = input('Enter Course Name: ').capitalize().ljust(20)
    if grade_already_present(roll, course):
        print('Grade for this course already exists')
        return
    grade = float(input('Enter Percentage '))
    with open('GRADE', 'ab') as f:
        f.write(struct.pack(format_str, roll.encode(), course.encode(), grade))
    print('Grade Added Successfully')

def import_grade():
    format_str = '11s20sf'
    try:
        with open('GRADE.txt', 'r') as f1:
            lines = f1.readlines()
        with open('GRADE', 'ab') as f:
            for line in lines:
                roll, course, grade = line.split()
                roll = roll.capitalize().ljust(11)
                course = course.capitalize().ljust(20)
                grade = float(grade)
                f.write(struct.pack(format_str, roll.encode(), course.encode(), grade))
        print('Grades Imported Successfully')
    except FileNotFoundError:
        print("Error: 'GRADE.txt' file not found. Make sure the file exists and contains the data in the correct format.")

def view_grade():
    format_str = '11s20sf'
    roll = input('Enter Roll Number for which you need to view Grade: ').capitalize().ljust(11)
    if not do_exist(roll):
        print('Roll Number Not Found')
        return
    with open('GRADE', 'rb') as f:
        while True:
            data = f.read(struct.calcsize(format_str))
            if not data:
                break
            roll_no, course, grade = struct.unpack(format_str, data)
            if roll_no.decode() == roll:
                print(f'Course: {course.decode()}')
                print(f'Grade: {grade}')
                print('-'*70)
    return

def edit_grade():
    format_str = '11s20sf'
    roll = input('Enter Roll Number for which you need to edit Grade: ').capitalize().ljust(11)
    if not do_exist(roll):
        print('Roll Number Not Found')
        return
    course = input('Enter Course Name: ').capitalize().ljust(20)
    if not grade_already_present(roll, course):
        print('Grade for this course does not exists')
        return
    grade = float(input('Enter Percentage '))
    with open('GRADE', 'rb') as f:
        lst = []
        while True:
            data = f.read(struct.calcsize(format_str))
            if not data:
                break
            lst.append(data)
    for i in lst:
        roll_no, course_name, percentage = struct.unpack(format_str, i)
        if roll_no.decode() == roll and course_name.decode() == course:
            lst[lst.index(i)] = struct.pack(format_str, roll.encode(), course.encode(), grade)
            break
    with open('GRADE', 'wb') as f:
        f.write(b''.join(lst))
    print('Grade Edited Successfully')

def delete_grade():
    format_str = '11s20sf'
    roll = input('Enter Roll Number for which you need to delete Grade: ').capitalize().ljust(11)
    if not do_exist(roll):
        print('Roll Number Not Found')
        return
    course = input('Enter Course Name: ').capitalize().ljust(20)
    if not grade_already_present(roll, course):
        print('Grade for this course does not exists')
        return
    with open('GRADE', 'rb') as f:
        lst = []
        while True:
            data = f.read(struct.calcsize(format_str))
            if not data:
                break
            lst.append(data)
    for i in lst:
        roll_no, course_name, _ = struct.unpack(format_str, i)
        if roll_no.decode() == roll and course_name.decode() == course:
            lst.remove(i)
            break
    with open('GRADE', 'wb') as f:
        f.write(b''.join(lst))
    print('Grade Deleted Successfully')

def list_studentwise_grade():
    roll = input('Enter Roll Number for which you need to view Grade: ').capitalize().ljust(11)
    if not do_exist(roll):
        print('Roll Number Not Found')
        return
    format_str = '11s20sf'
    with open('GRADE', 'rb') as f:
        lst = []
        while True:
            data = f.read(struct.calcsize(format_str))
            if not data:
                break
            roll_no, course, grade = struct.unpack(format_str, data)
            if roll_no.decode() == roll:
                lst.append([course, grade])
    if lst == []:
        print('No Grade Found for this student')
        return
    for i in lst:
        print(f'Course: {i[0].decode()} Grade: {i[1]}')
    return

def course_existS(course):
    with open('GRADE', 'rb') as f:
        while True:
            data = f.read(struct.calcsize('11s20sf'))
            if not data:
                break
            _, course_name, _ = struct.unpack('11s20sf', data)
            if course_name.decode() == course:
                return True
    return False

def list_coursewise_grade():
    format_str = '11s20sf'
    course = input('Enter Course Name: ').capitalize().ljust(20)
    if not course_existS(course):
        print('No record for this course exist')
        return
    with open('GRADE', 'rb') as f:
        lst = []
        while True:
            data = f.read(struct.calcsize(format_str))
            if not data:
                break
            roll_no, c, grade = struct.unpack(format_str, data)
            if c.decode()==course:
                lst.append([roll_no, grade])
    print(f'All the students enrolled in {course.strip()} course are as follows: ')
    for i in lst:
        print(f'Roll Number: {i[0].decode().strip()}    Grade: {i[1]}')
    return

def award_sheet():
    all_courses = dict()
    format_str = '11s20sf'
    with open('GRADE','rb') as f:
        while True:
            data = f.read(struct.calcsize(format_str))
            if not data: break;
            roll_no,course,grade = struct.unpack(format_str, data)
            course = course.decode(); roll_no = roll_no.decode()
            if course not in all_courses:
                all_courses[course] = [roll_no]
            else:
                all_courses[course].append(roll_no)
        if all_courses == {}:
            print('NO COURSES ENROLLED FOR ANY STUDENT')
        for each in all_courses.keys():
            print(f'---- SUBJECT: {each.strip().upper()} ----')
            for each_student in all_courses[each]:
                print('Roll no: ',each_student)
    return

def summary_sheet():
    format_str = '11s30s2sif11s'
    all_students = dict()
    with open('RECORD', 'rb') as f:
        while True:
            data = f.read(struct.calcsize(format_str))
            if not data: break;
            roll_no, name, dep, sem, percentage, phone = struct.unpack(format_str, data)
            roll_no = roll_no.decode().strip()
            all_students[roll_no] = [name.decode().strip(), dep.decode(), str(sem), phone.decode(), str(percentage)]

    courses_enrolled = dict()
    format_str = '11s20sf'
    with open('GRADE','rb') as f:
        while True:
            data = f.read(struct.calcsize(format_str))
            if not data: break;
            roll_no, course, grade = struct.unpack(format_str, data)
            roll_no = roll_no.decode().strip(); course = course.decode()
            if course not in courses_enrolled:
                courses_enrolled[course] = [roll_no]
            else:
                courses_enrolled[course].append(roll_no)
    for each in courses_enrolled.keys():
        print(f'COURSE :{each.upper()}')
        for each_student in courses_enrolled[each]:
            print(' '.join(all_students[each_student]))
    return

def transcripts():
    format_str_student = '11s30s2sif11s'
    all_students = dict()

    with open('RECORD', 'rb') as f:
        while True:
            data = f.read(struct.calcsize(format_str_student))
            if not data:
                break
            roll_no, name, dep, sem, percentage, phone = struct.unpack(format_str_student, data)
            roll_no = roll_no.decode().strip()
            all_students[roll_no] = [name.decode().strip(), dep.decode(), str(sem), phone.decode(), str(percentage)]

    format_str_grade = '11s20sf'
    courses_enrolled = dict()

    with open('GRADE', 'rb') as f:
        while True:
            data = f.read(struct.calcsize(format_str_grade))
            if not data:
                break
            roll_no, course, grade = struct.unpack(format_str_grade, data)
            roll_no = roll_no.decode().strip()
            if roll_no not in courses_enrolled:
                courses_enrolled[roll_no] = [(course, grade)]
            else:
                courses_enrolled[roll_no].append((course, grade))

    start_roll = input('Enter the starting Roll Number: ').capitalize().ljust(11)
    end_roll = input('Enter the ending Roll Number: ').capitalize().ljust(11)

    for roll in all_students.keys():
        if start_roll <= roll <= end_roll:
            print(f'Roll Number: {roll}')
            print(f'Name: {all_students[roll][0]}')
            print(f'Department: {all_students[roll][1]}')
            print(f'Semester: {all_students[roll][2]}')
            print(f'Phone Number: {all_students[roll][3]}')
            print(f'Percentage: {all_students[roll][4]}')
            print('Courses Enrolled: ')
            if roll in courses_enrolled:
                for course, grade in courses_enrolled[roll]:
                    print(f'Course: {course.decode()} Grade: {grade}')
            print('-' * 70)

if __name__ == "__main__":
    main()
