import json
# data = {}
# with open('data.json', 'w') as f:
#     json.dump(data, f)

def loading():
    with open('data.json', 'r') as f:
        data = json.load(f)
        return data

def saving(data):
    with open('data.json', 'w') as f:
        json.dump(data, f)

def display():
    print('CODE'.ljust(8) + 'TITLE'.ljust(30) + ' CREDIT HOURS' + ' SEMESTER' + '  TYPE ')
    with open('data.json', 'r') as f:
        data = json.load(f)
        for each in data.values():
            print(' '.join(each.values()))
    print('='*80)

def adding():
    c = input('Enter Code:')
    data = loading()
    if c in data.keys():
        print('code already exists..')
        return
    if len(c) > 8:
        while len(c)>8:
            print('code must be less than 9 characters..')
            c = input('Enter Code:')
    t = input('Enter Title:')
    if len(t) > 40:
        while len(t) > 40:
            print('Title must be less than 41 characters..')
            t = input('Enter Title:')
    h = int(input('Enter Credit hours:'))
    s = int(input('Enter Semester:'))
    type = input('Enter type (core/elective):')
    data = loading()
    data[c] = {'code': str(c).ljust(8),
               'title': t.ljust(30),
               'credit_hours': str(h).center(10),
               'semester': str(s).center(8),
               'type': type.center(8)}
    saving(data)
    display()

def deleting():
    key = input('Enter Code for which you want to delete:')
    data = loading()
    if key in data.keys():
        del data[key]
        saving(data)
        display()
    else:
        print('No such record found')

def listing():
    display()

def searhing():
    key = input('Enter Code for which you want to search:')
    data = loading()
    if key in data.keys():
        print('CODE'.ljust(8) + 'TITLE'.ljust(30) + ' CREDIT HOURS' + ' SEMESTER' + '  TYPE ')
        print(' '.join(data[key].values()))
    else:
        print('No such record found')

def editing():
    key = input('Enter Code for which you want to edit:')
    data = loading()
    if key in data.keys():
        print(' '.join(data[key].values()))
    print('PRESS\n 1 for title change\n 2 for credit_hours change\n 3 for semester change\n 4 for type change')
    options = (1, 2, 3, 4)
    while True:
        x = int(input('What do you want to edit in it?'))
        if x in options: break;
        print('Choose within given range(1-4) for editing!')
    if x == 1:
        y = input('Enter new title:')
        data[key]['title'] = str(y).ljust(30)
    elif x == 2:
        y = input('Enter new credit_hours:')
        data[key]['credit_hours'] = str(y).center(10)
    elif x == 3:
        y = input('Enter new Semester:')
        data[key]['semester'] = str(y).center(8)
    elif x == 4:
        y = input('Enter new type(core/elective):')
        data[key]['type'] = str(y).center(8)


    saving(data)
    display()

while True:
    print()
    print('-----------<< WELCOME TO STUDENT MANAGEMENT SYSTEM >>------------')
    print()
    x = input('ENTER:\n a for adding\n d for deleting\n s for searching\n l for listing\n e for editing\n q for quiet\nEnter here: ')
    if x == 'a':
        adding()
    elif x == 'd':
        deleting()2
    elif x == 'q':
        print('THANK YOU FOR USING OUR SYSTEM')
        break
    elif x == 'l':
        listing()
    elif x == 's':
        searhing()
    elif x == 'e':
        editing()
    else:
        print('INVALID INPUT')



