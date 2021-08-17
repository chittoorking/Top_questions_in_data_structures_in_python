s1="Hi I am Vamsi ! I am going to start my own company soon"
words=s1.split()
for word in words:
    if len(word)%2==0:
        print(word)
