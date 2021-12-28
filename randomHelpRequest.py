# Write a function in python to display the name of top three rankholder’s for a class of 10 students. The function should take the following 6 lists as input parameters:
# example :-

# Name = [“ABC”, “XYZ”,……..]

# Sub1 = [87, 98, …..]

# Sub2 = [67, 89, ….]

# Sub3 = [23, 45,…]

# Sub4 = [34, 67,…]

# Sub5 = [23, 56,…] 

# Each of these lists contain 10 elements.

# name , sub1 , sub2 , sub 4 , sub 4 , sub 5 .. these should be six lists
# and they should be user defined 

# name is basically name and the rest 5 lists are their marks in those subjects
# 10 students
# 5 subjects
# and each list with 10 elements
# those will be each student's marks

# def getStudents(self):

Sub1 = []
Sub2 = []
Sub3 = []
Sub4 = []
Sub5 = []
Name = [] #students

student1 = ""
student2 = ""
student3 = ""
student4 = ""
student5 = ""
student6 = ""
student7 = ""
student8 = ""
student9 = ""
student10 = ""


def getStudents(self, students):
    global counter
    counter = 0
    allScores = []
    for student in students:
        global studentTotalScore
        studentTotalScore = int(Sub1[counter]) + int(Sub2[counter]) + int(Sub3[counter]) + int(Sub4[counter]) + int(Sub5[counter])
        print(studentTotalScore)
        counter +=1
    allScores.append(studentTotalScore)
    return allScores

for i in range(10):
    student = input("Enter the student name: ")
    Name.append(student)
print("Students list:\n", Name)

for i in range(10):
    addSub1 = input("Enter for Sub1: ")
    Sub1.append(addSub1)
print("Subject 1 Scores:\n", Sub1)

for i in range(10):
    addSub2 = input("Enter for Sub2: ")
    Sub2.append(addSub2)
print("Subject 2 Scores:\n", Sub2)

for i in range(10):
    addSub3 = input("Enter for Sub3: ")
    Sub3.append(addSub3)
print("Subject 3 Scores:\n", Sub3)


for i in range(10):
    addSub4 = input("Enter for Sub4: ")
    Sub4.append(addSub4)
print("Subject 4 Scores:\n", Sub4)


for i in range(10):
    addSub5 = input("Enter for Sub5: ")
    Sub5.append(addSub5)
print("Subject 5 Scores:\n", Sub5)


print(getStudents, Name)