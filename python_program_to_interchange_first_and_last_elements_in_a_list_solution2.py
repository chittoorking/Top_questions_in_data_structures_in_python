print("This is python program to swap first and last elements of a list")
def swapList(newList):
    newList[0],newList[-1]=newList[-1],newList[0]
    return newList
newList=[12,35,9,56,24]
print(swapList(newList))
#Understand that in function it is taking a tuple and updating with another tuple
#With interchanging values
