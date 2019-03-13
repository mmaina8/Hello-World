Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[0,1,2,3,4,5,6,7,8,9]
>>> fruits.append (10)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    fruits.append (10)
NameError: name 'fruits' is not defined
>>> fruits.append ('10')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    fruits.append ('10')
NameError: name 'fruits' is not defined
>>> x.append(10)
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> x.extend(11,12)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x.extend(11,12)
TypeError: extend() takes exactly one argument (2 given)
>>> x.extend([11,12])
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
>>> x.pop ()
12
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
>>> x.remove (11)
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> x.reverse
<built-in method reverse of list object at 0x01A9E260>
>>> x.reverse ()
>>> x
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> x.count (8)
1
>>> sum (x)
55
>>> max (x)
10
>>> min (x)
0
>>> x [:2]
[10, 9]
>>> x [3:7]
[7, 6, 5, 4]
>>> 
>>> 
>>> y=[]
>>> y=[x*10 for x in y]
>>> y
[]
>>> y=[x*10 for y in x]
>>> y

>>> x
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> y

>>> y=[]
>>> y
[]
>>> x*10

>>> y=[s*10 for s in x]
>>> y
[100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
>>> for s in x:
	print (x)

	

>>> for s in y:
	print (y)

	

>>> 
>>> y
[100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
>>> for j in y:
	print (j)

	
100
90
80
70
60
50
40
30
20
10
0
>>> x
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> 
>>> 
>>> x
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> x.reverse ()
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> x.remove (10)
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> 
>>> k=x[ :5]
>>> k
[0, 1, 2, 3, 4]
>>> v=x[5: ]
>>> v
[5, 6, 7, 8, 9]
>>> 
>>> 
>>> 
>>> 
>>> n=[[1,2,3],[4,5,6],[7,8,9]]
>>> m=[]
>>> for sublist in n :
	for x in sublist:
		m.append (x)

		
>>> m
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> for e in m:
	print (e)

	
1
2
3
4
5
6
7
8
9
>>> 
