# TASK-2
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

