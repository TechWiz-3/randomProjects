grade = int(input("Please enter the mark: "))

if grade > 84:
    print("Great work, you have achieved a high distinction")
elif grade > 74:
    print("Good job, you've achieved a distinction")
elif grade > 64:
    print("Nice work, you've achieved credit")
elif grade > 49:
    print("You have passed")
else: # grade below 50
    print("You've failed, better luck next time")