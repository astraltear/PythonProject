import types
def distance_from_zero(s):
    if type(s)==int or type(s)==float:
        return abs(s)
    else:
        return "Not an integer or float!"


print( distance_from_zero(123) )
