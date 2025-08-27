#hasmaps dictionary
#Dictionary are mutable
from datetime import datetime

person={"name":"zed","gender":"male","age":18,"height":6*2+2,"mydatenumeric":20250825,"mydatestring":"2025-08-25"}
print("Does age exists :" , 'age' in person)
print("Does age exists :" + 'age' in person)
print(person)
dict1={"date":datetime.today()}
print(dict1)
print(person["name"])
print(person.get("name"))
print(person['gender'])
print(person['age'])
print(person.get('state')) #returns NULL (None) if state does not exist
print(person.get('state','PA')) #returns PA if state does not exist
person['name']='John'
print(person)
person['age']+=18
print(person)
person['college']=True
print(person)
person['college']=False
print(person)
person['city']='Miami'
print(person)
print("Does age exists :" , 'age' in person)
del person['college']
print(person)
person['siblings']=['Cory']
print(person)
person['siblings'].append('Betsy')
print(person)
person_attrib={'status':'married','children':3}
person.update(person_attrib)
print(person)
billy={
    'name':'Billy',
    'age':18,
    'height':6*2+2,
    'grades':[100,98,89,99,100],
    'attendance':[True,False,True,True,True]
}
sarah={
    'name':'Sarah',
    'age':20,
    'height':25,
    'grades':[100,100,100,100,100],
    'attendance':[True,True,True,True,True]
}
ben={
    'name':'Ben',
    'age':19,
    'height':222,
    'grades':[100,100,100,100,100],
    'attendance':[True,True,True,False,False]
}

students={1:billy,2:sarah,3:ben}
print("Line 60")
print(students)
print(len(students))
print(students.keys())
print(students.values())
print(students.items())
print(billy)
print(len(billy))
print(billy.keys())
print(billy.values())
print(billy.items())

#Iterate students
for k in students:
    print(students[k])
    print("Key:",k)

print(students.keys())
billy1=students[1]
print(billy1)
print(billy['attendance'])


print("hello")
print(ben.get('height'))
print(ben.get('grades'))

items=ben.items()
print(items)
for k,v in items:
    print(k,v)

grades=[]
items=students.items()
print(items)
print("I am here")
for k,v in items:
    for g in v['grades']:
        grades.append(g)
print(grades)
print(sum(grades)/len(grades))

d = {'A': 1, 'B': 2, 'C': 3}
print(list(d.values()))
print(list(d.keys()))
d = {'A': 1, 'B': 2, 'C': 3}
del d['A']
print(d)

d = {}
d[1] = 1
d['1'] = 2
d[1] = 3
print("d is :" , d)
sum = 0
for i in d:
    sum += d[i]
print(sum)

course = {'1': 'CIT590',
          '2': 'CIT591',
          '3': 'CIT593'}
print(course['1'])

course = {'1': 'CIT590',
          '2': 'CIT591',
          '3': 'CIT593'}
print(course.get('4'))

course = {'1': 'CIT590',
          '2': 'CIT591',
          '3': 'CIT593'}
print(course.get('4', 'CIT594'))

def open_read_file(file):
    f=open(file, 'r')
    print(type(f))
    cnt=0
    line = f.readline()
    while line:
        print(line, end='')
        line=f.readline()
        #print(line, end='')
        cnt +=1
    print("")
    print('There are ', cnt, ' lines in this file.')
    f.close()

def main():
    #open_read_file('HYSA1.txt')
     open_read_file('C:/Users/mohan/Downloads/HYSA.txt')
if __name__ == '__main__':
    main()


def open_read_append_new_file(file1,file2):

    with open(file1) as fin:
        lst = fin.readlines()
        lst.reverse()
        fout = open(file2,'a')
        fout.writelines(lst)
        fout.close()

def main():
    #open_read_file('HYSA1.txt')
    open_read_append_new_file('C:/Users/mohan/Downloads/HYSA.txt',"HYSAout1.txt")
if __name__ == '__main__':
    main()


def open_read_append_same_file(file):

    f = open(file,'r+')

    lst=f.readlines()

    lst.insert(0,'\n')
    lst.insert(0,'Hello I added this line')
    lst.insert(0,'\n')

    f.writelines(lst)

    f.close()

def main():
    open_read_append_same_file('HYSAcheck.txt')

if __name__ == '__main__':
    main()


def open_read_write_new_file(file1,file2):
    with open(file1) as fin:
        text = fin.read()
        fout=open(file2,'w')
        fout.write(text)
        fout.close()

def main():
    open_read_write_new_file('HYSAcheck.txt','HYSAcheck1.txt')

if __name__ == '__main__':
    main()


def import_and_create_dictionary(filename):
    f = open(filename,'r')
    lst_lines = f.readlines()
    expenses={}

    for l in lst_lines:
        lst = l.strip().split(",")

        key = lst[0].strip()
        value = lst[1].strip()


        if len(lst) <= 1:
            continue

        try:
            value = float(value)
            expenses[key] = expenses.get(key, 0) + value
        except:
            continue

        f.close()
        return expenses

def main():
    expenses = import_and_create_dictionary('names_values1.txt')
    print(expenses)

if __name__ == '__main__':
    main()