age = int(input("Please enter your age: "))
resident = input("Are you a permanent resident (yes/no): ")
student = input("Are you a student (yes/no): ")

# check eligibility
if age > 17 and age < 26 and resident.lower() == "yes" and student.lower() == "no":
    print("Congrats you are eligible")
else:
    print("Sorry you are not eligible")

