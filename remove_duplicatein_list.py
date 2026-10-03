n=input().split(",")
l=[int(i) for i in n]
l1=[]
for i in l:
   if i in l1:
     continue
   else:
     l1.append(i) 
print(l1)
##by using set
n=input().split(",")
l=[int(i) for i in n]
s=set(l)
newl=list(s)
print(newl)