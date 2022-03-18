# Your First App

In terminal run the following commands
```
 mkdir Python         #To create a new Directory 
 cd Python            #Reach your Directory
 touch first.py       #Create new file in your python Directory 
 code .               #open with Vs 
```
run the following in your Vs
```
Print ("I Love Python")
print("Hello Python World")

Print ("I Love Python") ; print("Hello Python World")
```  

* To excute program by using
1. Vs Terminal : click at the run botton on the right top of the terminal
2. Command Line : run this command `python first.py`

##  Indentation 
Python is sensetive in  Indentation (Block of Code)
   ```
  if True :
     Print ("I Love Python")
     print("Hello Python World")
   ```


## Comments
***Comment doesn`t excuted*** 

#This is Comment

#This is another Comment

#This is another Comment

***Prevent Code From Run*** 

#print("programming")  /// this code will not excueted

***Comments important for other programmers to give a notes and describe the code*** 

 """ 
 This 
 is 
 Not 
 Comment
 """



## Dealing With Data 

* Our Apps Contain Code and Data
* Code is The Lines You Write To Manage Deal With This Data
* To structure The Data We Need TO Categorize[Num ,S tring,Boolean]
* Nums --> Age , Phone number ,salaries
* String --> such as Names
* Boolean : True and False 
* Data Stored in On Computer Memory
* Variables doesnt contain your data , We Use it To Refer To This Data

## Some Data Types
* type() : To get the type of the data
* All Data In Python Is Object
- `print(type(100))` --- >  int : integer 
- `print(type(10.9))` --- >   float : Floating point number
- `print(type("Hello python "))` --- >   str : string 
- `print(type([1,2,3,4,5]))` --- >   list
- `print(type((1,2,3,4,50))` --- >   tuple
- `print(type({"one:1 ," two" :2 , "Three :3}))` --- >   dic : dictonary
- `print(type(2==2))` --- >   bool :Boolean

## Variables

syntax === > [Variable name][Assigment Operator] [Value]
Example == > myVariable = "My Value"
             print (myVariable) 

Output == > My Value

* Name Convention and Rules
1. Can start With (a-z A-Z) Or UnderScore
2. You cann`t Start With Numbers Or Special Characteros
3. Can Include (0-9) Or UnderScore
4. Cannot Include Special Characters
5. Name is Not Like name (Case Sensetive)  


name ="John"      #single word ==> Normal

myName ="John"    #Tow Words ==> Camel Case

my_name ="John"   #Tow Words ==> snake_case

a, b, c = 1, 2, 3 
print (a) ==> 1
print (b) ==> 2
print (c) ==> 3

***You Cannot Assign Values To Reserved Word***

Reserved word == > class , if , True ,False ,break , or ,from ...

***To check the reserved word in Python*** == > help("keywords") 


 ## Especial Characters

 1. \b Back Space 
 `print("Hello\World")`    #Will remove o
 Output == > HellWorld

 2.  \newline ==> Escape New Line + \
 ```
  print("Hello \
  World \
  Python")
 ``` 
 Output == > Hello World Python 

 3. \\ Escape Back Slash 

 `print ("I Love Back Slash \")` ==> #This is error it will scape double Quotes and caused an error

 `print ("I love Back Salsh\\")`

 Output ==> I Love Back Slash \

 4. \" Escape Double Quotes

 `print ("I love Double Quotes \"")`

 Output == > I love Double Quotes "

 5. \' Escape Single Quotes

`print ('I love Single Quotes \'')`

 Output == > I love Single Quotes ' 

 6. \n Line Feed
 `print("Hello World\nThis is new line")`

 Output ==>   Hello World
              This is new line

 7. \r Carrige Return 

 `print("123456\rabcd")`

 Output ==> abcd56

 8. \t Horizental Tab 

 `print("Hello\tWorld")`

 Output ==> Hello   World

 9. \xhh Character Hex Value

 `print ("\x5A")`

 Output ==> Z

 `print ("\x59\x5A")`

 Output ==> YZ

 ***You Can check [Hex, decimal, and symbol values - IBM](https://www.ibm.com/docs/en/ste/10.0.0?topic=maps-hex-decimal-symbol-values) for Hex, decimal, and symbol values***


## Concatenation 
```
a= "First Second Third"
b = "A , B , C"
print (a +" "+  b)
```

Output ==>  First Second Third A , B , C
```
a= "First\
 Second\
 Third"
b= " A\
    B\
      C " 
print (a +"\n"+  b)
```

Output ==>
First Second Third
 A    B      C

 ***You Cannot Concatenate str with int***

 `print ( "Hello" + 1)` 

 Output ==> TypeError: can only concatenate str (not "int") to str

 # Strings

``` 
myStringOne ='This is Single Quote'

myStringTwo ="This is Double Quote"

print (myStringOne)  Output ==>This is Single Quote

print(myStringTwo)   Output== > This is Double Quote

myStringThree ='This is Single Quote "Test"'

myStringFour ="This is Single Quote 'Test'"

print (myStringThree)    Output== > This is Single Quote "Test"

print(myStringFour)      Output ==>This is Single Quote 'Test'
```

myStringFive ="""First
Second
Third"""
print(myStringFive)

Output ==> 

First

Second

Third

## String Indexing And Slicing 

- Indexing (access single item)

```
myString ="I Love Python"
print (myString[0]) ==> I
print(myString[5])  ==> e
print(myString[-1]) ==> n    #First Character From The End
print(myString[-4]) ==> t    #Fourth Character From The End
```













 














