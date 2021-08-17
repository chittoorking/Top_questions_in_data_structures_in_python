fhandle1=open('G:\Desktop\Dta structures and algorithms using python\Top_interview_questions_in_data_structures_in_python\\all_lines.txt')
fhandle2=open('G:\Desktop\Dta structures and algorithms using python\Top_interview_questions_in_data_structures_in_python\\vamsi.txt','w')
count=1
for line in fhandle1:
     if count%2 != 0:
       fhandle2.write(line)
     count+=1
fhandle2.close()  