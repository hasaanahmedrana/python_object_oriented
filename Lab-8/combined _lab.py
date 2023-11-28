'''THIS FILE CONTAIN ALL THREE TASK OF LAB-8. IF YOU WANT TO RUN ALL THREE TASK, RUN ONE BY COMMENTING OTHERS FOR PROPER WORKING.'''
# --------------------------TASK-1-----------------------------

g = open('grades.txt', 'r')
e = open('errors.txt', 'w')

l = g.readline()
e.writelines(l)

l = g.readline()
e.writelines(l)

line_no = 3
error_count = 0
while True:
    l = g.readline()
    l = l.strip()
    if l == '':
        break
    if len(l) != 57:
        error_count += 1
        e.writelines(str(line_no)+'\n')
        e.writelines(l+'\n')
    else:
        spaces_idx = [41, 48, 51, 54]
        roll_no = l[:10]
        name = l[10:41]
        course = l[42:48]
        mid = l[49:51]
        sessional = l[52:54]
        finals = l[55:57]

        if len(roll_no.strip()) != 10 or (not roll_no.isalnum()) or (not (roll_no[0:4].isalpha() and roll_no[6].isalpha()) and (roll_no[4:6].isdigit() and roll_no[7:].isdigit())):
            error_count += 1
            e.writelines(str(line_no) + '\n')
            e.writelines(l + '\n')
            print('1')
        elif not (sessional[0] >= '0' and sessional[0] <= '9' and sessional[1] >= '0' and sessional[1] <= '9'):
            error_count += 1
            e.writelines(str(line_no) + '\n')
            e.writelines(l + '\n')
            print(sessional)
        elif not (mid[0] >= '0' and mid[0] <= '9' and mid[1] >= '0' and mid[1] <= '9'):
            error_count += 1
            e.writelines(str(line_no) + '\n')
            e.writelines(l + '\n')
            print('3')
        elif not (finals[0] >= '0' and finals[0] <= '9' and finals[1] >= '0' and finals[1] <= '9'):
            error_count += 1
            e.writelines(str(line_no) + '\n')
            e.writelines( l +'\n')
            print('4')
        elif course.count(' ') == 6:
            error_count += 1
            e.writelines(str(line_no) + '\n')
            e.writelines(l + '\n')
        else:
            for i in spaces_idx:
                if l[i] != ' ':
                    error_count += 1
                    e.writelines(str(line_no) + '\n')
                    e.writelines(l+'\n')
                    print('5')
                    break
    line_no += 1

print("grades file is error FREE") if error_count == 0 else print(error_count, "errors are present in grades file")
g.close()
e.close()


# -----------------------------TASK-2-----------------------------
# REPLACING UPGRADED GRADES IN ERROR TO NEW FILE WITHOUT SEEK

g = open('grades.txt', 'r')
e = open('errors.txt', 'r')
g2 = open('updated_grades.txt', 'w')

e.readline()
e.readline()
x = g.readlines()
while True:
    n = e.readline()
    if n == '': break;
    error_line = int(n)
    x[error_line-1] = e.readline()
for i in x:
    g2.writelines(i)
g.close()
e.close()
g2.close()


#-----------------------------TASK-3-----------------------------

g = open('updated_grades.txt', 'r')
x = g.readlines()
all = {}
for j in range(2, len(x)):
    i = x[j]
    i = i.strip()
    roll_no = i[:10]
    name = i[10:41].strip()
    course = i[42:48].strip()
    mid = i[49:51]
    sessional = i[52:54]
    finals = i[55:57]
    course_total = int(mid) + int(sessional) + int(finals)
    if roll_no not in all:
        all[roll_no] = {'roll_no':roll_no, 'name': name, course: course_total, 'total': course_total}
    elif roll_no in all:
        all[roll_no][course] = course_total
        all[roll_no]['total'] += course_total
        all[roll_no]['percentage'] = round((all[roll_no]['total'] / 300) * 100, 1)
        marks = all[roll_no]['percentage']
        if marks >= 85: grade = "  A  ";
        elif marks >= 80: grade = "  A- ";
        elif marks >= 75: grade = "  B+ ";
        elif marks >= 70:grade = "  B  ";
        elif marks >= 65: grade = "  B- ";
        elif marks >= 61: grade = '  C+ ';
        elif marks >= 58: grade = '  C  ';
        elif marks >= 55: grade = '  C- ';
        elif marks >= 50: grade = '  D  ';
        else: grade = "F";
        all[roll_no]['grade'] = grade
g.close()
se = open('se.txt', 'w')
it = open('it.txt', 'w')
se_id = 1
it_id = 1
se_marks = [0] * 4    # ict , pf, dld, total
it_marks = [0] * 4
for i in all.keys():
    if 'BIT' in all[i]['roll_no']:
        s = ''
        s += str(it_id).rjust(6) + ' ' + str(all[i]['roll_no']) + ' ' + str(all[i]['name']).ljust(30) + ' '
        s += str(all[i]['ITC']).rjust(3) + ' ' + str(all[i]['PF']).rjust(3) + ' ' + str(all[i]['DLD']).rjust(3) + ' '
        s += str(all[i]['total']).rjust(5) + ' ' + str(all[i]['percentage']) + ' ' + str(all[i]['grade']) + '\n'
        it.writelines(s)
        it_id += 1
        it_marks[0] += all[i]['ITC']
        it_marks[1] += all[i]['PF']
        it_marks[2] += all[i]['DLD']
        it_marks[3] += all[i]['total']

    if 'BSE' in all[i]['roll_no']:
        s = ''
        s += str(se_id).rjust(6) + ' ' + str(all[i]['roll_no']) + ' ' + str(all[i]['name']).ljust(30) + ' '
        s += str(all[i]['ITC']).rjust(3) + ' ' + str(all[i]['PF']).rjust(3) + ' ' + str(all[i]['DLD']).rjust(3) + ' '
        s += str(all[i]['total']).rjust(5) + ' ' + str(all[i]['percentage']) + ' ' + str(all[i]['grade']) + '\n'
        se.writelines(s)
        se_id += 1
        se_marks[0] += all[i]['ITC']
        se_marks[1] += all[i]['PF']
        se_marks[2] += all[i]['DLD']
        se_marks[3] += all[i]['total']

se.writelines('============================\n'.rjust(78))
it.writelines('============================\n'.rjust(78))
se.writelines(f' BSE DEGREE AVERAGE: {str(se_marks[0]).rjust(3)} {str(se_marks[1]).rjust(3)} {str(se_marks[2]).rjust(3)} {str(se_marks[3]).rjust(5)}'.rjust(66))
it.writelines(f' BIT DEGREE AVERAGE: {str(it_marks[0]).rjust(3)} {str(it_marks[1]).rjust(3)} {str(it_marks[2]).rjust(3)} {str(it_marks[3]).rjust(5)}'.rjust(66))

r = open('result_card', 'w')
it = open('it.txt')
se = open('se.txt')
r.writelines('University of the Punjab'.rjust(50) + '\n' + 'College of Information Technology'.rjust(55) + '\n'+ 'Result Session : Spring 2010'.rjust(53) +'')
r.writelines('\n\nDEGREE: BIT\n')
r.writelines('\nSr.No. Roll No.   Student Name                   ITC  PF DLD Total %age Grade')
r.writelines('\n====== ========== ============================== === === === ===== ==== =====\n')
r.write(it.read())
r.writelines('\n\nDEGREE: BSE\n')
r.writelines('\nSr.No. Roll No.   Student Name                   ITC  PF DLD Total %age Grade')
r.writelines('\n====== ========== ============================== === === === ===== ==== =====\n')
r.write(se.read())
r.close()
se.close()
it.close()