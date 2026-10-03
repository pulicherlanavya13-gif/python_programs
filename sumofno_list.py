#l=[10,20,30,40,50]
#sum=0
#for i in l:
 #   sum+=i
#print(sum)
#by using input
n=input().split(",")
sum=0
l=[int(i) for i in n]
for i in l:
    sum+=i
print(sum)
