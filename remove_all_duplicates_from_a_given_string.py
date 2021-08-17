print("This is python program to remove duplicates from a given string")
st=input("Enter the string")
st_set=set(st)
final_string=''.join(st_set)
print(final_string)
#What will be the output if order of characters matter
dict1=dict()
for i  in st:
     dict1[i]=dict1.get(i,0)+1
res=''.join(dict1)
print(res)
