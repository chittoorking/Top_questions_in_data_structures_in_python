st1=input("Enter a string to check if it contains all unique characters")
st2=dict()
for i in st1:
    st2[i]=st2.get(i,0)+1
l1=len(st2)
l2=len(st1)
if l1==l2:
    print('True')
else:
    print('False')
