# A program for permaculture designers to enter elements for random assembly generation
# Created by Zac the Wise on 16/12/2021

#firstElement = ["fence", "windmill", "shadehouse", "animal shelter", "trellis", "mounds", "compost heaps", "plants", "ducks", "windbreak"]
#thirdElement = ["hosue", "storage box", "yard or compound", "ponds", "tanks", "canals", "swales", "chickens", "fish", "barn"]

import time

firstElement = []
theMagic = ["attached to", "beside", "around", "over", "in", "on", "under", "containing"]
thirdElement = []

print("Enter first elements, when done press enter")
addfirstElement = str(input("Enter the first element: "))
firstElement.append(addfirstElement)
while addfirstElement != "":
    addfirstElement = str(input("Enter a first element: "))
    if addfirstElement != "":
        firstElement.append(addfirstElement)

print("Enter second elements, when done press enter")
addsecondElement = str(input("Enter the second element: "))
thirdElement.append(addsecondElement)
while addsecondElement != "":
    addsecondElement = str(input("Enter the second element: "))
    if addsecondElement != "":
        thirdElement.append(addsecondElement)

for first in firstElement:
    for magic in theMagic:
        for third in thirdElement:
            print(f'{first} {magic} {third}')
            time.sleep(.2)

counter = 0
print("Now for the first element combinations")
for glue in theMagic:
    counter = 0
    for item in firstElement:
        for secondIteration in firstElement:
            try:
                if item == firstElement[counter]:
                    pass
                else:
                    print(f'{item} {glue} {firstElement[counter]}')
                    time.sleep(.1)
                counter+=1
            except:
                pass

print("Now for the second element combinations")
for magic in theMagic:
    counter = 0
    for item in thirdElement:
        for secondIteration in thirdElement:
            try:
                if item == thirdElement[counter]:
                     pass
                else:
                    print(f'{item} {magic} {thirdElement[counter]}')
                    time.sleep(.1)
                counter+=1
            except:
                pass
                
            

#PS: yes i know this is terrible code ok