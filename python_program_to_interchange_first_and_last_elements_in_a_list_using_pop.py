print("This is python program to swap first and last element using swap")
def swapList(newList):
    first=newList.pop(0)
    last=newList.pop(-1)
    newList.insert(0,last)
    newList.append(first)
    return newList
newList=[12,35,9,56,24]
print(swapList(newList))
