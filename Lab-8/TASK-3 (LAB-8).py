#TASK-3
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