# -*- coding: utf-8 -*-

words = open('./words.txt').read().splitlines()
#print(words)
length_count = {}

l = map(len,words)
# print(type(l))

''' map이라는 것은 함수와 시퀀스 자료형(리스트, 터플, 문자열)을 입력으로 받아서 시퀀스 자료형의 각각의 요소가 
함수의 입력으로 들어간 다음 나오는 출력값을 묶어서 리스트로 돌려주는 함수이다. '''
for l in map(len,words):
    length_count[l] = length_count.get(l,0)+1
    '''
    if l in length_count:
        length_count[l] +=1
    else:
        length_count[l]=1
    '''
    
#print(length_count)

by_len={}
for w in words:
    by_len.setdefault(len(w),[]).append(w)
    
#print(by_len)