n=input().split(",")
l=[int(i) for i in n]
max=l[0]
min=l[0]
for i in l:
    if max<i:
        max=i
    if min>i:
        min=i
print(max,min)