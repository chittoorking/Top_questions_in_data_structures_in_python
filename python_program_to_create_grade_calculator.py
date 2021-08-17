#Python code for the Grade
#Calculate program in action

#Creating a dictionary which
#consists of the student name,
#assignment result test results
#And their respective lab results
def grade(student_grade):
    name=student_grade['name']
    assignment_marks=student_grade['assignment']
    assignment_score=sum(assignment_marks)/len(assignment_marks)
    test_marks=student_grade['test']
    test_score=sum(test_marks)/len(test_marks)
    lab_marks=student_grade['lab']
    lab_score=sum(lab_marks)/len(lab_marks)
    score=0.1*assignment_score+0.7*test_score+0.2*lab_score
    if score>=90 :return 'A'
    elif score>=80 :return 'B'
    elif score>=70 :return 'C'
    elif score>=60 :return 'D'
jack={"name":"Jack Frost","assignment":[80,50,40,20],"test":[75,75],"lab":[78,20,77,20]}
x=grade(jack)
print(x)
