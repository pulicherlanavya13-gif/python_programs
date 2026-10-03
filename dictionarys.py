my_dict={"Name":"Navya","age":19}
print(my_dict["Name"])
my_dict["age"]=20
print(my_dict)
for i,j in my_dict.items():
    print(i,j)
##by using user input
dict={}
Name=input()
age=int(input())

dict["Name"]=Name
dict["Age"]=age