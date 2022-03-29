student_list = []
response = 'yes'

while response.lower() == 'yes':
    name = input("Enter your name")
    student_list.append(name)

    response = input("Enter 'yes'to add more names or 'no' otherwise")

print('List of student nams:')
for student in student_list:
    print(student)