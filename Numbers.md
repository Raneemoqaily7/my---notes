# Numbers
```
print (type (10))      #<class 'int'>
print (type (10.5))    #<class 'float'>
print(type(5+8j))      #<class 'complex'>

complexNumber=5+8j
print(complexNumber.real)     #5.0
print (complexNumber.imag)    #8.0

```

- Notes
1. You Can Convert int To float Or complex

```
num1=10
num2=10.00
num3=10+9j

print(float(num1))       #Output =>10.0
print(complex(num1))     #Output ==>(10+0j)

print(int(num2))         #Output ==> 10
print(complex(num2))     #Output (10+0j)

print(int(num3))         #Output ==>TypeError: can't convert complex to int
```

```
a=100/20
print (a)          #Output ==> 5.0

print (int(a))     #Output ==>5

result=(8+9)/8

print (result)          #Output ==> 2.125

print(int(result))      #Output ==> 2


print (8%2)             #Output ==>0

print (9%2)             #Output ==>1

print (2**5)           #Output ==>32

print (119//2)         #Output ==>59

print(120//2)          #Output ==>60
```

# Lists

1. List Items Enclosed in Square Brackets
2. List Are Orderd , To use Indexes To Access Items 
3. Lists Are Mutable ==>Add ,Delete ,Edit 
4. List Items Are Not Uniqe 
5. List Can Have Differnt Data Type 


- To Access item by use it index

```
myList =["one","Two","one","1","10.96","True"]
print (myList[0])            #Output ==>one 
print (myList[-1])           #Output ==> True 
print(myList[-6])            #Output ==>one 
```

***Some Operation on myList***

myList =["one","Two","one","1","10.96","True"]
```
# print (myList[0])
# print(myList[-6])
print (myList[0])            #one 
print (type (myList))        #<class 'list'>
print (type (myList[0]))    #<class 'str'>
print(myList[-1])           #True 
myList[0]="Hello"
print (myList)              #['Hello', 'Two', 'one', '1', '10.96', 'True']
print (myList[0:3])         #['Hello', 'Two', 'one']
myList[0:3]="hello"
print (myList)              #['h', 'e', 'l', 'l', 'o', '1', '10.96', 'True']
myList[0:4] =[]             
print (myList)              #['o', '1', '10.96', 'True']

print(len(myList))          #4
```