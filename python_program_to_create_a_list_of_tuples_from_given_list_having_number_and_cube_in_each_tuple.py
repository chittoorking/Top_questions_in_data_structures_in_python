list1=[1,2,3]
#Using list comprehension to iterate each
#Values in list and create a  tuple as specified
res=[(val,pow(val,3)) for val in list1]
print(res)
