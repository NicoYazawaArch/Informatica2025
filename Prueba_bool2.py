a=True
b=False
c=True
d=False
#z= a and b or c and not d
z= a and (b or c) and not d
print(z)