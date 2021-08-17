# Python code to demonstrate
# length of list
# using naive method
  
# Initializing list 
test_list = [ 1, 4, 5, 7, 8 ]
  
# Printing test_list
print ("The list is : " + str(test_list))
  
# Finding length of list 
# using loop
# Initializing counter
counter = 0
for i in test_list:
      
    # incrementing counter
    counter = counter + 1
  
# Printing length of list 
print ("Length of list using naive method is : " + str(counter))
# Python program to demonstrate working
# of len()
a = []
a.append("Hello")
a.append("Geeks")
a.append("For")
a.append("Geeks")
print("The length of list is: ", len(a))
# Python program to demonstrate working
# of len()
n = len([10, 20, 30])
print("The length of list is: ", n)
# Python code to demonstrate
# length of list
# using len() and length_hint
from operator import length_hint
  
# Initializing list 
test_list = [ 1, 4, 5, 7, 8 ]
  
# Printing test_list
print ("The list is : " + str(test_list))
  
# Finding length of list 
# using len()
list_len = len(test_list)
  
# Finding length of list 
# using length_hint()
list_len_hint = length_hint(test_list)
  
# Printing length of list 
print ("Length of list using len() is : " + str(list_len))
print ("Length of list using length_hint() is : " + str(list_len_hint))
# Python code to demonstrate
# length of list
# Performance Analysis
from operator import length_hint
import time
  
# Initializing list 
test_list = [ 1, 4, 5, 7, 8 ]
  
# Printing test_list
print ("The list is : " + str(test_list))
  
# Finding length of list 
# using loop
# Initializing counter
start_time_naive = time.time()
counter = 0
for i in test_list:
      
    # incrementing counter
    counter = counter + 1
end_time_naive = str(time.time() - start_time_naive)
  
# Finding length of list 
# using len()
start_time_len = time.time()
list_len = len(test_list)
end_time_len = str(time.time() - start_time_len)
  
# Finding length of list 
# using length_hint()
start_time_hint = time.time()
list_len_hint = length_hint(test_list)
end_time_hint = str(time.time() - start_time_hint)
  
# Printing Times of each 
print ("Time taken using naive method is : " + end_time_naive)
print ("Time taken using len() is : " + end_time_len)
print ("Time taken using length_hint() is : " + end_time_hint)
 #It can be clearly seen that time taken is naive >> length_hint() > len(), hence len() is the best choice to use.