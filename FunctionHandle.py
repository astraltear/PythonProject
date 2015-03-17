# -*- coding: utf-8 -*-


def divide(a,b):
    q = a// b  # 몫
    r = a - q*b # 나머지
    return (q,r)

quota , remain =  divide(10,3)

print quota, remain