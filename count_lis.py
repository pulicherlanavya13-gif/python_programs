n=input().split(",")
l=[int(i) for i in n]
value=int(input("value u want to count"))
count=0
for i in l:
    if i==value:
        count+=1
print(count) 
#by using count()
n=input().split(",")
l=[int(i) for i in n]
value=int(input("enter value"))
print(l.count(value))