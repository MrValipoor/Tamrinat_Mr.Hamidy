Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:46:45) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=3.14
>>> b=int(a)
>>> print(b)
3
>>> a='3.14'
>>> b=float(a)
>>> print(b)
3.14
>>> c=int(b)
>>> print(c)
3
>>> age=[10,12,33,100,200,500]
>>> print(age[5])
500
>>> print(age[-1])
500
.
>>> age2=age[2:4]
>>> print(age2)
[33, 100]
>>> age3=[1:5:1]
SyntaxError: invalid syntax
>>> age3=age[1:5:1]
>>> print(age3)
[12, 33, 100, 200]
>>> age.append(1)
>>> print(age)
[10, 12, 33, 100, 200, 500, 1]
>>> del age[5]
>>> print(age)
[10, 12, 33, 100, 200, 1]
>>> d=have good time mr.hamidy
SyntaxError: invalid syntax
>>> d='have good time mr.hamidy'
>>> print(d)
have good time mr.hamidy
>>> 