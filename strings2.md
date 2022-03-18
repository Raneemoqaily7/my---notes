# Strings Method

9. ***swapcase()***
```
string="i Love PythOn"
print(string.swapcase())        Output ==> I lOVE pYTHoN
```

10. ***startswith() & endswith()***
 - These Two Methods Return True And False
```
string ="I Love Python"
print(string.startswith("I"))            Output ==> True
print(string.startswith("P"))            Output ==>False   
print(string.startswith("P",7,12))       Output ==>True
print (string.endswith("n"))             Output ==>True
print (string.endswith("e",0,6))         Output ==>True
```

11. ***index()***

```
string ="I Love Python"  
print (string.index("P"))           Output ==>7
print (string.index("P",0,10))      Output ==>7
print (string.index("P",0,5))       Output ==> ValueError: substring not found
```
12. ***find(Substring,Start,End)***

```
string ="I Love Python"
print (string.find("P",0,10))         Output ==>7
print (string.find("p",0,5))          Output ==>-1    #-1 :Substring Not Founded
```
13.  ***rjust(width ,Fill char)  & ljust()***

```
name ="john"
print(name.rjust(10,"#"))       Output ==>######john
print(name.ljust(10,"#"))       Output ==>john######
```

14.     ***splitlines()***

 - splitlines() : Rreturn The String as  list

```
string1= """first
second
third
"""
print(string1.splitlines())     Output ==> ['first', 'second', 'third']

string2="first\nsecond\nthird"

print(string2.splitlines())     Output ==> ['first', 'second', 'third']
```

15. ***expandtabs()***

```
string ="Hello\tPython\tdev"

print(string.expandtabs(10))       Output ==> Hello     Python    dev
```

16. *** replace()***
```
string ="Hello Python World"

print(string.replace("Hello","Hi"))    Output ==> Hi Python World
```

17. ***join(iterable)***
- join Applied on Lists And Tuples
- Return List To String 

list = ["Hello","Python","World"]

print("-" .join(list))             Output ==> Hello-Python-World

## String Formating
### Old Way String Formating
name = "John"
age =30

```
 print ("my name is : "+ name)  #Output  ==> my name is : John

 print ("my old is : "+ age )   #Output==> TypeError: can only concatenate str (not "int") to str
```

 %s ==>string
 %d ==> digit
 %f ==>float

```
name = "John"
language = "python"
age =30
Rank =10
   
print ("My name is : %s , my age is : %d ,Iam a %s Dev with Rank %f " %(name,age ,language,Rank))
```
***Output == >My name is : John , my age is : 30 ,Iam a python Dev with Rank 10.000000***

- To Control Float Number 

`print ("Rank %.3f"  %Rank)`    #Output ==> Rank 10.000

msg = "Hello Python People I Love You All"


- To Control Strings (Truncate String)
```
print ( "The massage is : %s" %msg)    Output == > The massage is : Hello Python People I Love You All

print ( "The massage is : %.19s" %msg)  Output == > The massage is : Hello Python People
```

### New Way String Formating

{:d} : digit 
{:s} : string 
{:f} : float
```
name = "John"
language = "python"
age =30
Rank =10

print ("my name is :{} and my age is {} Iam a {} Dev with Rank {}".format(name,age,language,Rank))
 

print ("my name is :{:s} and my age is {:d} Iam a {:s} Dev with Rank {:f}".format(name,age,language,Rank))
```

***Output ==>***
my name is :John and my age is 30 Iam a python Dev with Rank 10

my name is :John and my age is 30 Iam a python Dev with Rank 10.000000
---
msg = "Hello Python People I Love You All"

print ("Massage is : {:.19s}".format( msg))
---

money = 254673894034

print("Money is : {}".format(money))          Output ==> Money is : 254673894034
print("Money is : {:_d}".format(money))       Output ==> Money is : 254_673_894_034
---

a, b, c ="one", "two" ,"three"
print("Hello {} {} {}".format(a ,b ,c))       Output ==> Hello one two three
print("Hello {2} {0} {1}".format(a ,b ,c))    Output ==> Hello three one two

---

name ="john"
age=30
print (f"My Name {name} Iam {age} Years Old")   Output==> My Name john Iam 30 Years Old
---



[Main](./README.md)
[Back](./strings1.md)