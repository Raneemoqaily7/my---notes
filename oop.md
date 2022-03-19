# OOP

- OOP AllowYou To Organize Your Code and Make it Rediacle and Reusable 
- Everything in Python is Object 

- ***IF MAN IS OBJECT*** 

***Attribute ==> Name ,Age ,Address,PhoneNumber,Info ==>[Data]***

***Methods [Behaviours] ==> Walking ,Eating ,Singing ==>[Functions]***

- ***If Car is Object*** 
- ***Attribute ==> Color ,Model ,Brand***

- ***Methods ==> Walking ,Stopping***

# Class
- Class is Template To Create Objects [blueprint,object constructor]
```
class Member:
    def __init__(self):
        print("Anew Member Has Been Added")



member_one =Member()          #Anew Member Has Been Added
member_two =Member()          #Anew Member Has Been Added

print (member_one.__class__)   #<class '__main__.Member'>
```

```
class Member:
    def __init__(self ,firstName,lastName,gender):    #This is a constructor wrote  the data you want use in (init)
        self.fName=firstName
        self.lName=lastName
        self.gender=gender

    
    def first_Name(self):                 #all methodss should have self 

        if self.gender == "male":
           return f'Hello Mr {self.fName}'      #to use the data that you define in your constructor use self.

        elif self.gender == "female":
            return f'Hello Mis {self.fName}'

    def full_Name(self):

        return f'{self.fName} {self.lName}'

    def get_all_data(self):

    return f'{self.first_Name()} your full name is : {self.full_Name()}'  #to use method inside method-> self.methodname()


member_one =Member("John","Smith","male")        #Here you have to assign real data for ur instances 
print (member_one.full_Name())                 #John Smith
print(member_one.get_all_data())               #Hello Mr John your full name is : John Smith
member_two=Member("Julia","Smith","female")    
print(member_two.get_all_data())                #Hello Mis Julia your full name is : Julia Smith
```

## Class Attributes

- It Defineds Outside the Constructor 

class Member:

    not_allowed_names =["ha","ba" ,"Na]       #Class Attribute
    def __init__(self ,firstName,lastName,gender):
        self.fName=firstName
        self.lName=lastName
        self.gender=gender

```
class Member:

    not_allowed_name=["ha","ba","Na"]

    def __init__(self ,firstName,lastName,gender):
        self.fName=firstName
        self.lName=lastName
        self.gender=gender

    
    def first_Name(self):
        if self.fName in Member.not_allowed_name:  # Use Class Attribite inside a method(you have to call the class name.)
            raise ValueError ("Name Not Allowded")
        else:
         if self.gender == "male":
           return f'Hello Mr {self.fName}'

         elif self.gender == "female":
            return f'Hello Mis {self.fName}'

    def full_Name(self):
        
           return f'{self.first_Name()} {self.lName}'   #pass a method inside a method use (self.methodName())

    def get_all_data(self):

        return f'{self.first_Name()} your full name is : {self.full_Name()}'


member_one =Member("John","Smith","male")
print (member_one.full_Name())              #UP==>Hello Mr John Smith
print(member_one.get_all_data())            #UP==>Hello Mr John your full name is : Hello Mr John Smith
member_two=Member("Julia","Smith","female")
print(member_two.full_Name())                #UP==>Hello Mis Julia Smith

member_three=Member("Na","Smith","female")
print(member_three.get_all_data())            #UP==>raise ValueError ("Name Not Allowded")  ValueError: Name Not Allowded

```

### To Count Number  Of Instance 
- Use Class A ttribute 
```
class Member:

    not_allowed_name=["ha","ba","Na"]
    user_num=0       #initial value for Class Attribute

    def __init__(self ,firstName,lastName,gender):
        self.fName=firstName
        self.lName=lastName
        self.gender=gender
        Member.user_num+=1         #Increment Counter
    
    def first_Name(self):
        if self.fName in Member.not_allowed_name:
            raise ValueError ("Name Not Allowded")
        else:
         if self.gender == "male":
           return f'Hello Mr {self.fName}'

         elif self.gender == "female":
            return f'Hello Mis {self.fName}'

    def full_Name(self):
        
           return f'{self.first_Name()} {self.lName}'

    def get_all_data(self):

        return f'{self.first_Name()} your full name is : {self.full_Name()}'


member_one =Member("John","Smith","male")

member_two=Member("Julia","Smith","female")

print(Member.user_num)                              #Output ==>2
member_three=Member("Na","Smith","female")

member_four=Member("hala","Ahmad","female")
print(Member.user_num)                               #Output==>4
``` 

