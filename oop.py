class Member:

    not_allowed_name=["ha","ba","Na"]
    user_num=0

    def __init__(self ,firstName,lastName,gender):
        self.fName=firstName
        self.lName=lastName
        self.gender=gender
        Member.user_num+=1
    
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

    def Delete_User(self):
        
        Member.user_num-=1
        return f'new member is deleted'


member_one =Member("John","Smith","male")
print (member_one.full_Name())
print(member_one.get_all_data())
member_two=Member("Julia","Smith","female")
print(member_two.full_Name())
print(Member.user_num)
member_three=Member("Na","Smith","female")
# print(member_three.get_all_data())
# member_two =Member()
print(Member.user_num)
member_four=Member("hala","Ahmad","female")
print(Member.user_num)

print(Member.Delete_User(member_four))

# print (member_one.__class__)
# print(dir(Member))
