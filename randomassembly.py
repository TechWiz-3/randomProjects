# A program for permaculture designers to enter elements for random assembly generation
# Created by Zac the Wise on 16/12/2021

#firstElement = ["fence", "windmill", "shadehouse", "animal shelter", "trellis", "mounds", "compost heaps", "plants", "ducks", "windbreak"]
#thirdElement = ["hosue", "storage box", "yard or compound", "ponds", "tanks", "canals", "swales", "chickens", "fish", "barn"]
firstElement = []
theMagic = ["attached to", "beside", "around", "over", "in", "on", "under", "containing"]
thirdElement = []

print("Enter first elements, when done press enter")
addfirstElement = str(input("Enter the first element: "))
while addfirstElement != "":
    addfirstElement = str(input("Enter a first element: "))
    if addfirstElement != "":
        firstElement.append(addfirstElement)

print("Enter second elements, when done press enter")
addsecondElement = str(input("Enter the second element: "))
while addsecondElement != "":
    addsecondElement = str(input("Enter the second element: "))
    if addsecondElement != "":
        thirdElement.append(addsecondElement)

for first in firstElement:
    for magic in theMagic:
        for third in thirdElement:
            print(f'{first} {magic} {third}')

#PS: yes i know this is terrible code ok