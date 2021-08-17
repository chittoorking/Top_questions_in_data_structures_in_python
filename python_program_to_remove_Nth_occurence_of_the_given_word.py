#Given a list of words in python 
#The task is to remove the Nth occurence of the given word in that list
list_=["perfect","plan","perfect","hi","perfect"]
n=3
word="perfect"
count=0
for i in range(0,len(list_)):
    if list_[i]==word:
      count=count+1
      if count==n:
        list_.remove(list_[i])
        break
print(list_)

