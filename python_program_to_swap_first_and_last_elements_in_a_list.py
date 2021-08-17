print("This is python program to swap first and last elements of  a list")
def swapList(newList):
    #Storing the first and last element 
    #as a pair in a tuple variable get
    get=newList[-1],newList[0]
    #unpacking those elements
    newList[0],newList[-1]=get
    return newList

newList=[12,35,9,56,24]
print(swapList(newList))
