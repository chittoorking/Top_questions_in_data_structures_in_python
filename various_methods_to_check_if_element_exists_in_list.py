# Python code to demonstrate
# checking of element existence
# using loops and in
 
# Initializing list
test_list = [ 1, 6, 3, 5, 3, 4 ]
 
print("Checking if 4 exists in list ( using loop ) : ")
 
# Checking if 4 exists in list
# using loop
for i in test_list:
    if(i == 4) :
        print ("Element Exists")
 
print("Checking if 4 exists in list ( using in ) : ")
 
# Checking if 4 exists in list
# using in
if (4 in test_list):
    print ("Element Exists")
# Python code to demonstrate
# checking of element existence
# using set() + in
# using sort() + bisect_left()
from bisect import bisect_left ,bisect
 
# Initializing list
test_list_set = [ 1, 6, 3, 5, 3, 4 ]
test_list_bisect = [ 1, 6, 3, 5, 3, 4 ]
 
print("Checking if 4 exists in list ( using set() + in) : ")
 
# Checking if 4 exists in list
# using set() + in
test_list_set = set(test_list_set)
if 4 in test_list_set :
    print ("Element Exists")
 
print("Checking if 4 exists in list ( using sort() + bisect_left() ) : ")
 
# Checking if 4 exists in list
# using sort() + bisect_left()
test_list_bisect.sort()
if bisect_left(test_list_bisect, 4)!=bisect(test_list_bisect, 4):
    print ("Element Exists")
else:
    print("Element doesnt exist")
"""
Python code to demonstrate
checking of element existence
using List count() method
"""
 
# Initializing list
test_list = [10, 15, 20, 7, 46, 2808]
 
print("Checking if 15 exists in list")
 
# number of times element exists in list
exist_count = test_list.count(15)
 
# checking if it is more then 0
if exist_count > 0:
    print("Yes, 15 exists in list")
else:
    print("No, 15 does not exists in list")