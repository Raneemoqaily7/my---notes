
 # Strings 1

``` 
myStringOne ='This is Single Quote'

myStringTwo ="This is Double Quote"

print (myStringOne)  #Output ==>This is Single Quote

print(myStringTwo)   #Output== > This is Double Quote

myStringThree ='This is Single Quote "Test"'

myStringFour ="This is Single Quote 'Test'"

print (myStringThree)    #Output== > This is Single Quote "Test"

print(myStringFour)      #Output ==>This is Single Quote 'Test'

myStringFive ="""First
Second
Third"""

print(myStringFive)       Output ==>  First

                                      Second

                                      Third

                                               
```



## String Indexing And Slicing 

- Indexing (access single item)

```
myString ="I Love Python"
print (myString[0]) ==> I    #First Character From The Start 
print(myString[5])  ==> e    #Fifth Character From The Start
print(myString[-1]) ==> n    #First Character From The End
print(myString[-4]) ==> t    #Fourth Character From The End
```
- ***Slicing (Access Multiple Sequence Items)***

   ***[start:End]   #End Not Encluded***
```
myString ="I Love Python"
print (myString[8:11])     #Output ==>yth
print (myString[2:6])      #Output ==>Love
print (myString[7:13])     #Output ==>Python
```
   ***[Start:End:Step]***
```
print (myString[2:11:2])      #Output ==> Lv yh
print (myString[-2:-11:-2])   #Output ==> otPeo
```

```
print (myString[:11])     #Output ==> I Love Pyth     #If Start Is Not Here Start From Index 0
print (myString[0:])      #Output ==> I Love Python   #If End Is Not Here Will Go To The End 
print (myString[2:])      #Output ==> Love Python
print (myString[-2:])     #Output ==> on
print (myString[:-2])     #Output ==> I Love Pyth
print (myString[:])       #Output ==> Love Python     #Full Data 
```


```
print (myString[0::5])    #Output ==> Ieh
print (myString[0::4])    #Output ==> Ivyn
print (myString[0::10])   #Output ==> Ih
print (myString[0::1])    #Output ==> I Love Python    #Full  Data
```

## Strings Method 
 1. ***Length Of String***
```
myString ="I Love Python"
print (len(myString))                #Output ==> 13
myString1 ="     I Love Python"
print (len(myString1))               #Output ==> 18
```
2. ***strip()   rstrip()  lstrip()***

```
myString1 ="        I Love Python      "
print (myString1.strip())                      Output ==>I Love Python
print (myString1.rstrip())                     Output ==>        I Love Python
print (myString1.lstrip())                     Output ==>I Love Python

myString2="#####I Love Python ###########"
print (myString2.strip('#'))                   Output ==>I Love Python
print (myString2.rstrip('#'))                  Output ==>#####I Love Python
print (myString2.lstrip('#'))                  Output ==>I Love Python ###########

myString3="@####@@2@## I Love Python ###@@@#@"
print (myString3.strip("#@"))                  Output ==>I Love Python
print (myString3.rstrip("#@"))                 Output ==>@####@@@## I Love Python
print (myString3.lstrip("#@"))                 Output ==>I Love Python ###@@@#@
```

3. ***title()  &  capitalize***

```
myString= "i love 2d graphics  and 3g technology and python "
print(myString.title())        #Output ==> I Love 2D Graphics  And 3G Technology And Python

print(myString.capitalize())   #Output ==> I love 2d graphics  and 3g technology and python
```


4. ***zfill()***

```
a,b,c,d="1","10","100","1000"
print(a.zfill(4))     #Output ==>0001
print(b.zfill(4))     #Output ==>0010
print(c.zfill(4))     #Output ==>0100
print(d.zfill(4))     #Output ==>1000
```

5. ***upper()   &   lower()***
```
name1= "john"    
name2="JOHN"
print(name1.upper())           Output==>JOHN
print(name2.lower())           Output==>john
```

6. ***split()***

```
myString1 ="Hello Python World"
myString2 ="Hello-Python-World"
print(myString1.split())                   Output ==> ['Hello', 'Python', 'World']
print(myString1.split(" "))                Output ==> ['Hello', 'Python', 'World']
print(myString2.split("-"))                Output ==> ['Hello', 'Python', 'World']
myString3 ="I Love Python and Mysql"       Output ==> ['I', 'Love', 'Python and Mysql']
print(myString3.split(" ",2))
print(myString3.rsplit(" ",2))             Output ==>['I Love Python', 'and', 'Mysql']
```

7. ***center()***

```
name ="john"
print(name.center(8,"@"))        Output ==> @@john@@
```

8. ***count()***
   
```
myString ="I Love Python And Php And Mysql And Java script"
print (myString.count("And"))                              Output ==> 3
print(myString.count("And",0,25))                          Output ==>2 

```


[Main](./README.md)
[Back](./firstApp.md)
[Next](./strings2.md)





