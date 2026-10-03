def calculateroots(a,b,c):
    d=(b**2)-4*a*c
    root1=(-b+(d**0.5))/2*a
    root2=(-b-(d**0.5))/2*a
    return root1,root2
roots=calculateroots(1,-3,2)
print(roots)