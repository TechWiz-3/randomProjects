# exception handling
a= 10
b =20
c=0
try:
    d = a/c
    print(d)
except ZeroDivisionError as err:
    print('ZeroDivisionError: ',err)
except TypeError as err:
    print('TypeError: ',err)
except Exception as err:
    print('an exception occurred')
    print('Exception: ',type(err),err)
else:
    print('bye from else')
finally:
    print('bye from finally')



print('good bye')