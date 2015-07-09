
lloyd={"name":"LIoyd","homework":[90.0, 97.0, 75.0, 92.0],"quizzes":[88.0, 40.0, 94.0],"tests":[75.0, 90.0]}
alice={"name":"Alice","homework":[100.0, 92.0, 98.0, 100.0],"quizzes":[82.0, 83.0, 91.0],"tests":[89.0, 97.0]}
tyler={"name":"Tyler","homework":[0.0, 87.0, 75.0, 22.0],"quizzes":[0.0, 75.0, 78.0],"tests":[100.0, 100.0]}
student=[lloyd,alice,tyler]

'''
for stu in student:
    print stu['name']
    print sum(stu['homework'])
    print stu['quizzes']
    print stu['tests']
'''

def average(valList):
    avg = sum(valList)/len(valList)
    return avg

def get_average(valDict):
    total_avg=0
    home_avg= average(valDict['homework'])
    quiz_avg= average(valDict['quizzes'])
    test_avg= average(valDict['tests'])
    total_avg=home_avg*0.1+quiz_avg*0.3+test_avg*0.6
    return total_avg

def get_letter_grade(score):
    grade='F'
    if score >=90 :
        grade='A'
    elif score >= 80 and score <90:
        grade='B'
    elif score >= 70 and score <80:
        grade='C'
    elif score >= 60 and score <70:
        grade='D'
    else:
        grade='F'

    return grade

def get_class_average(students):
    sum=0
    for i in students:
        sum+=get_average(i)
    return sum/len(students), get_letter_grade(sum/len(students))
    
print get_class_average(student)

#print get_letter_grade(get_average(lloyd))

