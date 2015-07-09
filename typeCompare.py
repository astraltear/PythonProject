import types
def distance_from_zero(s):
    if type(s)==types.IntType or type(s)==types.FloatType:
        return abs(s)
    else:
        return "Not an integer or float!"


print distance_from_zero(123)
