Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> first_name='Joy'
>>> last_name='Wahome'
>>> school='AkiraChix'
>>> 'Hello, my name is'+' '+first_name+' '+last_name+'.'+'I go to'+' '+school+'.'
'Hello, my name is Joy Wahome.I go to AkiraChix.'
>>> a=10
>>> b=20
>>> a
10
>>> b
20
>>> c='dog'
>>> d='cat'
>>> e=a/3
>>> e
3.3333333333333335
>>> type(a)
<class 'int'>
>>> type(c)
<class 'str'>
>>> type(e)
<class 'float'>
>>> f=str(a)
>>> f
'10'
>>> type(f)
<class 'str'>
>>> g=123
>>> h=int(g)
>>> type(h)
<class 'int'>
>>> i=int(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    i=int(c)
ValueError: invalid literal for int() with base 10: 'dog'
>>> print('Hello AkiraChix')
Hello AkiraChix
>>> print('Hello AkiraChix.\n Class of 2019.')
Hello AkiraChix.
 Class of 2019.
>>> print('Hello AkiraChix.\t Class of 2019.')
Hello AkiraChix.	 Class of 2019.
>>> print('Hello AkiraChix.\b Class of 2019.')
Hello AkiraChix. Class of 2019.
>>> first='Joy'
>>> last='Wahome'
>>> greeting='Hello, {} {}'.format(first,last)
>>> print(greeting)
Hello, Joy Wahome
>>> code='ABC123'
>>> amount=1000
>>> recipient='071325898'
>>> message='{} confirmed! Hi {} {}, you have sent ksh {} to {}.'.format(code,first,last,amount,recipient)
>>> message
'ABC123 confirmed! Hi Joy Wahome, you have sent ksh 1000 to 071325898.'
>>> message='{} confirmed! Hi {} {},\n you have sent ksh {}\n to {}.'.format(code,first,last,amount,recipient)
>>> message
'ABC123 confirmed! Hi Joy Wahome,\n you have sent ksh 1000\n to 071325898.'
>>> message=('{} confirmed! Hi {} {},\n)\ you have sent ksh {}\n to {}.').format(code,first,last,amount,recipient)
>>> message
'ABC123 confirmed! Hi Joy Wahome,\n)\\ you have sent ksh 1000\n to 071325898.'
>>> ]]
SyntaxError: invalid syntax
>>> 
>>> 


>>> 
>>> 

>>> 
>>> 

>>> 

>>> 
>>> 

>>> 
]
>>> message='{} confirmed! Hi {} {}, \n you have sent ksh {} \n to {}.'.format(code,first,last,amount,recipient)
>>> message
'ABC123 confirmed! Hi Joy Wahome, \n you have sent ksh 1000 \n to 071325898.'
>>> print(message)
ABC123 confirmed! Hi Joy Wahome, 
 you have sent ksh 1000 
 to 071325898.
>>> 
