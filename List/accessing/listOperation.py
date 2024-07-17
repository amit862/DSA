
myList = [1,2,3,4,5,6,7]
print(myList)
myList.insert(4,15) #----------------->O(n)

myList.append(55) #--------------------->O(1)

newList = [11,12,13,14]
newList.extend(newList) #--------------------->O(n)
print(myList)
