# #TASK-1
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


