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

***You Cannot Assign Values To Reserved Word***

Reserved word == > class , if , True ,False ,break , or ,from ...

***To check the reserved word in Python*** == > help("keywords") 

help("keywords")
# False               break               for                 not
# None                class               from                or
# True                continue            global              pass
# __peg_parser__      def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield 
 














