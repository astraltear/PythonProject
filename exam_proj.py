# -*- coding: cp949 -*-
# even odd
def is_even(x):
    if x%2==0:
        return True
    else:
        return False

# int float compare
import types
def is_int(x):
    if type(x) == types.IntType:
        return True
    elif type(x) == types.FloatType:
         if x -int(x) ==0:
             return True
         else:
            return False


print is_int(-1)
print is_int(7.0)
print is_int(7.5)
    
# number sum
def digit_sum(n):
    string = str(n)
    sum=0
    for i in string:
        print i
        sum+=int(i)
    return sum

print digit_sum(1234)

#factorial
def factorial(x):
    if x ==0:
        return 1
    else:
        return x*factorial(x-1)

print factorial(4)

# reverse string

a=['a','b','c']
for i in reversed(a):
    print i
print ""    

for i,e in reversed(list(enumerate(a))):
    print i,e
print ""

for item in a[::-1]:
    print item
print ""

def reverse(text):    
    string='';
    for i in range(len(text)-1, -1, -1):
        string+=text[i]
    return string

print reverse("Python!")    

# 문자 거르기 
def anti_vowel(text):
    return_items=''
    for item in text:
        if item not in 'aeiouAEIOU':
            return_items+=item
    return return_items

print anti_vowel("Hey You!")


# scramble game
# 입력을 해야 하는 부분이 있어서 주석처리
'''
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
"f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
"l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
"r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
"x": 8, "z": 10}
def scrabble_score(word):
    total_score=0
    if word.isalpha():
        word = word.lower();
        #print word
        for c in word:
            total_score+= score[c]
        
    else:
        print "is non alpha"
   
    return total_score

word = raw_input("input word:")
print scrabble_score(word)
'''

# string search
def censor(text,word):
    return text.replace(word, len(word) * '*')

print censor("this hack is wack hack", "hack")


def purify(my_list):
    out_list=[]
    for idx in my_list:
        if idx%2==0:
            out_list.append(idx)
    return out_list

print purify([1,2,3,4,5,6])

# list duplicate check
t = [1, 2, 3, 1, 2, 5, 6, 7, 8]
s = [1, 2, 3]
out_list = list(set(t))
print out_list

minus_list = list(set(t) - set(s))
print minus_list


