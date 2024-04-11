from array import*

arr1 = array('i',[1,2,3,4,5,6])

def accessElement(array,index):
    if index >= len(array):       #------------------------------------->>>>>>>> T.C - O(1)
        print("There is not any element in this index")   #------------------------------------->>>>>>>> T.C - O(1)
    else:
        print(array[index])  #------------------------------------->>>>>>>> T.C - O(1)

accessElement(arr1,1)


############ T.C ------> O(1)