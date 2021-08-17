print("This is the python programme to print sum and average without using lists")
sum=0
count=0
while True:
    x=float(input("Enter the number "))
    sum=sum+x
    count+=1
    y=input("Do you want to enter another number!y/n")
    if y=='y':
        continue
    else:
        break
print("The sum is {0} and average is {1}".format(sum,(sum/count)))

