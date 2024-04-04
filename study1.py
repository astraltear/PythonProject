# comment
'''
multi line comment
'''

# reference variable

a= 5
b = 10
c = b
print(id(a), id(b),id(c))
print( a is b, b is c)  # False,  True

import keyword
print(keyword.kwlist)

print(type( 3+4j ))
print( type( (1,) ) )  # tuple
print( type( [1,2] ) ) # list
print( type( {1,2} ) )  #set
print( type( {'name':2} ) )  #dic

print('output',end='$');print('output2')  # output$output2

# packing
v1, *v2 = 1,2,3,4,5
print(v1, v2)

# a++ ++a 증감 연산자 없음
print( bool(0), bool(None),bool('') ) # all False
print(format(1.5432,'100.3f'))
print('name {0}, age {1}'.format("korean",30))
print('name {}, age {}'.format("korean",50))
print('name {2}, age {0}'.format("ko",20,30))

print('aa\tbb')
print(r'aa\tbb')

str1 = 'sequence'
print(str1.find('e'), str1.find('e',3),str1.rfind('e'))

# 아래의 코드는 string 이 immutable한 것을 보여준다.
# 해당 변수의 값이 변경된 것이 아니라 새로운 참조객체를 만든 후 새로운 객체의 주소로 링킹해 준다.
ss1 = 'mbc'
print(ss1,id(ss1))

ss1='abc'
print(ss1,id(ss1))

str2 = ['123','456','234']
str2.sort(key=int)
print(str2)

# shallow copy
names=['tom','james','charles']
names2 = names
print(id(names), id(names2))

# deep copy
import copy
names3 = copy.deepcopy(names)
print(id(names), id(names2),id(names3))

names2[2]='X'
print(names, names2,names3)

# tuple read only
t='a','d','e',
print(t,len(t),t.index('d'))

t1 = (10,20)
x,y = t1
t2 = y,x
print(t2)

# set - not duplication
s1 = {1,2,3}
s2={3,4}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1-s2, s1|s2, s1&s2)
# print(s1[0])   'set' object does not support indexing

s1.add(5)
s1.update({5,6})
s1.update([8,9])
s1.update((10,11))
print(s1)

#s1.remove(20)  # 값이 없으면 에러
s1.discard('eden')  # 값이 없으면 통과

s3 = s1  # shallow copy
s3.clear() #  s3, s1 clear
print(s1,s3)

# dict 순서가 없다.
mydict = dict(k1=1, k2='abc',k3=3.4)
print(mydict)

del mydict['k1']
print(mydict)

# Regular Expression
import  re

str1 = '123 abc가나다ABC_555_6_78mbc'
print(re.findall(r'123', str1,))  # ['123']
print(re.findall(r'[0-9]', str1,)) # ['1', '2', '3', '5', '5', '5', '6', '7', '8']
print(re.findall(r'[0-9]+', str1,)) # ['123', '555', '6', '78']
print(re.findall(r'[0-9]{2}', str1,)) # ['12', '55', '78']
print(re.findall(r'[0-9]{2,3}', str1,)) # ['123', '555', '78']
print(re.findall(r'.bc', str1,))  # ['abc', 'mbc']
print(re.findall(r'^1+', str1,))        #1로 시작  ['1']
print(re.findall(r'^1.', str1,))        #1로 시작   ['12']
print(re.findall(r'[^1].+', str1,))  # 1을 제외하고 모든 문자  ['23 abc가나다ABC_555_6_78mbc']
print(re.findall(r'mbc$', str1,))  # ['mbc']

import re
ss='''정필재 기자 = 1인 가구가 급증하고 있다. 2035년에는 세 가구 중 한 집은 독거가구가 될 것이라는 전망도 나온다.
8일 통계청과 LG경제연구원, 산업연구원 등에 1980년 1인 가구가 차지하는 비율이 4.5%에 불과했으며 1990년에도 9%에 머물렀다.
하지만 올해 1인 가구는 27.1%로 늘었으며 증가속도는 더욱 빨라져 2025년 31.3%(685만2000가구), 2035년에는 34.3%(762만8000가구)에 이를 것으로 예상된다.
1인 가구가 증가하는 속도도 빠르다. 미국은 경우 1인 가구 비중이 42년 새 9.6%포인트 증가해 26.7% 수준에 이르렀지만 한국의 경우 35년만에 22.3%포인트 증가했다.
사회적 관점에서 1인 가구의 증가는 각종 문제의 원인이 될 수 있지만 경제적 관점에서 이는 소비확대로 이어진다는 분석도 나온다.
국내경제활동 인구의 1인당 가처분소득을 146만원으로 가정했을 때 1인 가구는 114만원(78.0%)을 쓴다. 하지만 2인 가구의 1인 소비는 105만원(71.9%)에 불과하다.
특히 2020년 가구구성 변화에 따른 소비 변화를 추정해 보면 고령화는 소비를 -1.6% 낮추지만 1인 가구 및 가구원수 감소는 전체 소비를 3.1% 높일 것으로 예상된다.
또 2006년 전체 민간소비의 3.3%(16조원)에 불과했던 1인 가구 전체 소비지출 비율은 2010년 11.1%(60조원)로 확대된 이후 2020년 15.9%%(120조원)까지 늘어날 것으로 보인다.
이같은 사례는 해외에서도 찾아볼 수 있다.
미국의 연방소비자지출설문조사를 보면 1인 가구의 연간 지출은 3만4471달러로 나타났다. 고소비가구계층 중 자녀가 없는 부부가구의 구성원(1인당 2만8017달러)보다 많이 쓴다. 고소비가구 중 자녀가 있는 경우 2만3179달러를 소비해 1인 가구의 연간 지출보다 낮았다.
일본 역시 2011년 말 기준 1인 가구 평균 소비는 다인 가구의 월평균 소비보다 1.7%높게 나타났다.
일본종합연구소와 후생노동성이 2005년부터 5년간 인구구조 변화에 따른 소비 변화를 연구한 결과 가구원 감소로 인한 소비증대 효과는 2.7%였고 고령화 효과는 -0.7%에 불과했다.
고가영 LG경제연구원 선임연구원은 "1인 가구 증가가 인구고령화 등으로 위축된 소비를 상쇄해 줄 것으로 기대된다"고 말했다.
'''

re_result  = re.sub(r'[^가-힣\s]','',ss)
re_result = re_result.split(' ')

count={}
for i in re_result:
    if i in count.keys():
        count[i] +=1
    else:
        count[i] = 1

print(count)


score = 40
print(type(score))

if 90 <= score <=100:
    grade='A'
elif 70 <= score <90:
    grade='B'
else:
    grade='F'

print("result:"+str(score)+" grade:"+grade)

import  random
print(random.randint(1,100))
print('----------------------')
colors=['red','blue','black']   # list type
for color in colors:
    print(color, end=' ')
print('\n----------------------')
colors2=('red','blue','black') # tuple type
for color in colors2:
    print(color, end=' ')
print('\n----------------------')

colors3={'red','blue','black'}  # 순서가 없다. set
for color in colors3:
    print(color, end=' ')
print('\n----------------------')

soft={'java':'web','python':'all','c':'embed'}  # dict

for data in soft:
    print(data, end=' ')
print('\n----------------------')

for data in soft.keys():
    print(data, end=' ')
print('\n----------------------')

for data in soft.values():
    print(data, end=' ')
print('\n----------------------')

for data in soft.items():
    print(data, end=' ') # tuple
    print(data[0], '^^',data[1])
print('\n----------------------')

li1 = [3,4,5]
li2 = [5,6,7]

datas = [a+b for a in li1 for b in li2 ]
print(datas)

print( list(range(1,6,2)) )
print( set(range(1,6,2)) )
print( sum([1,2,3,4,5]))

re_list=[]
for i in range(1,101):
    if i%3==0 and i%5==0:
        re_list.append(i)
print(re_list)