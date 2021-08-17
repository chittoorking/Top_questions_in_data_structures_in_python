print("'This is python programme for factorial of a number")
n=int(input("Enter the number to find factorial of it"))
def factorial(n):
   if n==0 or n==1:
       return 1
   else:
       return n*factorial(n-1)
print("Factorial of number {0} is {1}".format(n,factorial(n)))
 
    