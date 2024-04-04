# -*- coding: cp949 -*-
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grades):
    for grade in grades:
        print grade

print_grades(grades)

def grades_sum(grades):
    total_grades =0
    for grade in grades:
        total_grades +=grade
    return total_grades

print grades_sum(grades)

def grades_averages(grades):
    total_sum = grades_sum(grades)
    avg = total_sum/len(grades)
    return avg

avg_grade = grades_averages(grades)

print avg_grade

    
