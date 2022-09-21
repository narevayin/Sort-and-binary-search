from re import X


mylist = [7,-5,10, 15, 21, -85, 67, 7,10,]

newlist = []

while mylist:
    minimum = mylist[0]
    for i in mylist:
        if i < minimum:
            minimum = i
    newlist.append(minimum)
    mylist.remove(minimum)

print (newlist)


def search(list1, low, high, x):
 
    if high >= low:
 
        mid = (high + low) // 2

        if list1[mid] == x:
            return mid
 
        elif list1[mid] > x:
            return search(list1, low, mid - 1, x)
 
        else:
            return search(list1, mid + 1, high, x)
 
    else:
        return -1
 
list1 = newlist
x = int(input('enter number: '))
 
result = search(list1, 0, len(list1)-1, x)
 
if result != -1:
    print("index", str(result))
else:
    print("not in array")