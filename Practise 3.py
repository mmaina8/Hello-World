Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s='foobar'
>>> len (s)
6
>>> s[0:3]
'foo'
>>> s[0:6]
'foobar'
>>> first_name='Joy'
>>> last_name='Wahome'
>>> full_name='{} {}'.format(first_name,last_name)
>>> a=full_name[0:3]
>>> a==first_name
True
>>> b=full_name[4:10]
>>> b==last_nam
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b==last_nam
NameError: name 'last_nam' is not defined
>>> b==last_name
True
>>> s.swapcase()
'FOOBAR'
>>> a='Joy'
>>> a.swapcase ()
'jOY'
>>> b='the sun rises in the east'
>>> b.title()
'The Sun Rises In The East'
>>> c='joy123'
>>> c.isdigit()
False
>>> d=123
>>> d.isdigit()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
>>> d='123'
>>> d.isdigit()
True
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> numbers=[1,2,3,4,5,6]
>>> letters=['a','b','c','d']
>>> 2 in numbers
True
>>> 8 in numbers
False
>>> 'c' in letters
True
>>> 'e' in letters
False
>>> numbers*3
[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
>>> numbers+letters
[1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd']
>>> fruits=['apple','melon','grapes','mango','banana']
>>> fruits.append('orange')
>>> fruits
['apple', 'melon', 'grapes', 'mango', 'banana', 'orange']
>>> fruits.extend(['berries','peach'])
>>> fruits
['apple', 'melon', 'grapes', 'mango', 'banana', 'orange', 'berries', 'peach']
>>> fruits.pop()
'peach'
>>> fruits
['apple', 'melon', 'grapes', 'mango', 'banana', 'orange', 'berries']
>>> fruits.remove('berries')
>>> fruits
['apple', 'melon', 'grapes', 'mango', 'banana', 'orange']
>>> fruits.reverse()
>>> fruits
['orange', 'banana', 'mango', 'grapes', 'melon', 'apple']
>>> fruits.sort()
>>> fruits
['apple', 'banana', 'grapes', 'mango', 'melon', 'orange']
>>> fruits.append('grapes')
>>> fruits.append('banana')
>>> fruits.append('mango')
>>> fruits
['apple', 'banana', 'grapes', 'mango', 'melon', 'orange', 'grapes', 'banana', 'mango']
>>> fruits.count('grapes')
2
>>> numbers
[1, 2, 3, 4, 5, 6]
>>> sum(numbers)
21
>>> max(numbers)
6
>>> min(numbers)
1
>>> max(fruits)
'orange'
>>> min(fruits)
'apple'
>>> sum(fruits)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    sum(fruits)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> fruits[0]
'apple'
>>> fruits[4]
'melon'
>>> numbers[3]
4
>>> numbers[5]
6
>>> numbers[-2]
5
>>> numbers[-4:-1]
[3, 4, 5]
>>> fruits[3:]
['mango', 'melon', 'orange', 'grapes', 'banana', 'mango']
>>> numbers[:-2]
[1, 2, 3, 4]
>>> fruits[-5:-2]
['melon', 'orange', 'grapes']
>>> 
>>> LIST TRAVERSAL
SyntaxError: invalid syntax
>>> for fruit in fruits
SyntaxError: invalid syntax
>>> for fruit in fruits:
	print(fruit)

	
apple
banana
grapes
mango
melon
orange
grapes
banana
mango
>>> for car in fruits:
	print(car)

	
apple
banana
grapes
mango
melon
orange
grapes
banana
mango
>>> for number in numbers:
	print(number)

	
1
2
3
4
5
6
>>> for number in numbers:
	print(number*10)

	
10
20
30
40
50
60
>>> for number in numbers:
	print(number^2)

	
3
0
1
6
7
4
>>> for number in numbers:
	print(number**2)

	
1
4
9
16
25
36
>>> numbers
[1, 2, 3, 4, 5, 6]
>>> x=range(5,15)
>>> x
range(5, 15)
>>> for n in x:
	print(n)

	
5
6
7
8
9
10
11
12
13
14
>>> s=range(9,19)
>>> s
range(9, 19)
>>> for v in s:
	print(s*5)

	
Traceback (most recent call last):
  File "<pyshell#99>", line 2, in <module>
    print(s*5)
TypeError: unsupported operand type(s) for *: 'range' and 'int'
>>> for v in s:
	print(v*5)

	
45
50
55
60
65
70
75
80
85
90
>>> 
>>> 'List comprehension- generatin a new list from an existing list in a newline'
'List comprehension- generatin a new list from an existing list in a newline'
>>> 'List comprehension- generatin a new list from an existing list in a single line'
'List comprehension- generatin a new list from an existing list in a single line'
>>> 
>>> squares=[number*number for number in numbers]
>>> doubles=[number*2 for number in numbers]
>>> squares
[1, 4, 9, 16, 25, 36]
>>> doubles
[2, 4, 6, 8, 10, 12]
>>> e[]
SyntaxError: invalid syntax
>>> for number in numbers:
	x=number*2
	e.append(x)

	
Traceback (most recent call last):
  File "<pyshell#114>", line 3, in <module>
    e.append(x)
NameError: name 'e' is not defined
>>> e=[]
>>> for number in numbers:
	x=number*2
	e.append(x)

	
>>> e
[2, 4, 6, 8, 10, 12]
>>> e==doubles
True
>>> m=[100,200,300,400,500]
>>> for p in m:
	p=m/7

	
Traceback (most recent call last):
  File "<pyshell#123>", line 2, in <module>
    p=m/7
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> for p in m:
	print (p=m/7)

	
Traceback (most recent call last):
  File "<pyshell#125>", line 2, in <module>
    print (p=m/7)
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> p=[number*2 for number in numbers]
>>> p
[2, 4, 6, 8, 10, 12]
>>> for p in m:
	print (p/7)

	
14.285714285714286
28.571428571428573
42.857142857142854
57.142857142857146
71.42857142857143
>>> p
500
>>> double=[p//7 for p in m]
>>> 
>>> double
[14, 28, 42, 57, 71]
>>> double=[p%7 for p in m]
>>> double
[2, 4, 6, 1, 3]
>>> m
[100, 200, 300, 400, 500]
>>> cler
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    cler
NameError: name 'cler' is not defined
>>> 
=============================== RESTART: Shell ===============================
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
>>> 
>>> 
>>> 
>>> m = [100,200,300,400,500]
>>> 
>>> 

>>> m
[100, 200, 300, 400, 500]

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 10%3
1
>>> 
>>> 
>>> 
>>> 20%7
6
>>> 
>>> p = [z%7 for z in m]
>>> 
>>> 
>>> 
>>> p
[2, 4, 6, 1, 3]
>>> 
>>> 
>>> 
>>> [x for x in m]
[100, 200, 300, 400, 500]
>>> 
>>> 
>>> 
>>> 
>>> [x//5 for x in m]
[20, 40, 60, 80, 100]
>>> 
>>> [x*50 for x in m]
[5000, 10000, 15000, 20000, 25000]
>>> 
>>> 
>>> 
>>> k =[]
>>> 
>>> 
>>> 
>>> for n in m:
	a = n%7
	k.append(a)

	
>>> 
>>> 
>>> 
>>> k
[2, 4, 6, 1, 3]
>>> 
>>> 
>>> 
>>> w = range(78,88)
>>> 
>>> 
>>> 
>>> w
range(78, 88)
>>> 
>>> 
>>> [x*2 for x in w]
[156, 158, 160, 162, 164, 166, 168, 170, 172, 174]
>>> for x in w:
	print(x*2)

	
156
158
160
162
164
166
168
170
172
174
>>> 
>>> 
>>> 
>>> 
>>> 
>>> x=[0,1,2,3,4,5,6,7,8,9]
>>> for j in x:
	print(j)

	
0
1
2
3
4
5
6
7
8
9
>>> for 
