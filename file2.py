# print (type (10))
# print (type (10.5))
# print(type(5+3j))

# complexNumber=5+8j

# print(complexNumber.real)
# print (complexNumber.imag)
# num1=10
# num2=10.00
# num3=10+9j

# a=100/20
# print (a)

# print (int(a))

# result=(8+9)/8
# print(int(result))

# print (8%2)
# print (9%2)
# print (2**5)
# print (119//2)
# print(120//2)


myList =["one","Two","one","1","10.96","True"]
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