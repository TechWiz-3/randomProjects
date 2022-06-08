print("please enter your 5 marks below")


def get_mark(inp):
    try:
        mark = int(inp)
    except ValueError:
        print("Please enter only integers between 0 and 100. The mark has  automatically been set to 0")
        mark = 0
        return mark
    else:
        if mark < 101 and mark > -1:
            return mark
        else:
            print("Please enter only integers between 0 and 100. The mark has automatcally been set to 0")
            mark = 0
            return mark


mark1 = get_mark(input("enter mark 1: "))
mark2 = get_mark(input("enter mark 2: "))
mark3 = get_mark(input("enter mark 3: "))
mark4 = get_mark(input("enter mark 4: "))
mark5 = get_mark(input("enter mark 5: "))

# create array/list with five marks
marksList = [mark1, mark2, mark3, mark4, mark5]

# print the array/list
print(marksList)

# calculate the sum and average
sumOfMarks = sum(marksList)
averageOfMarks = sum(marksList)/5

# display results
print("The sum of your marks is: "+str(sumOfMarks))
print("The average of your marks is: "+str(averageOfMarks))
