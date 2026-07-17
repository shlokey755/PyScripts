Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=5
id(x)
140723929408424
bool_1=(6>10)
print(bool_1)
False
>>> bool_2=(10<=20)
>>> print(bool_2)
True
>>> value1=20
>>> value2=none
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    value2=none
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> value2= None
>>> value1
20
>>> value2
>>> print(value2)
None
>>> 
>>> type(10)
<class 'int'>
>>> type(8.2)
<class 'float'>
>>> type(22/7)
<class 'float'>
>>> <class 'str'>
SyntaxError: invalid syntax
>>> type('22/7')
<class 'str'>
>>> type(true)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> type(5>3)
<class 'bool'>
>>> x=10
>>> type(x)
<class 'int'>
