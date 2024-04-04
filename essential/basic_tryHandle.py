'''
try except
'''

def divide(a,b):

    try:
        return a/b
    except Exception as e:
        return e
    except ZeroDivisionError as ze:
        return ze

    finally:
        return 'finally'

c =divide(2,2)


print(c)