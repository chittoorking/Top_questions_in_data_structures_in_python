print("This is python program to interchange first and last elements in a list")
a=[1,2,3,4,5,6]
c=a.pop(0)
d=a.pop(-1)
a.insert(0,d)
a.append(c)
print(a)
