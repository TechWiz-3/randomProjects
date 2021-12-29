def test():
    dic = {}
    name = ["ABC", "XYZ", "ewih", "wrihw", "ishfi", "sif", "sdj", "wdw", "nine", "teno"]
    sub1 = [87, 98, 23, 3, 12, 1, 3, 4, 5, 23]
    sub2 = [67, 89, 23, 4, 3, 5, 2, 3, 4, 12]
    sub3 = [23, 45, 1, 2, 3, 3, 5, 3, 5, 23]
    sub4 = [34, 67, 3, 34, 23, 23, 45, 8, 54, 23]
    sub5 = [23, 56, 12, 34, 23, 12, 34, 45, 34, 23]
    for n in range(len(name)):
        dic[name[n]] = sub1[n]
        dic[name[n]] += sub2[n]
        dic[name[n]] += sub3[n]
        dic[name[n]] += sub4[n]
        dic[name[n]] += sub5[n]
    return dic
counter = 0
for i in sorted(test(),reverse=True):
    print(i)
    counter +=1
    if counter == 4:
        break