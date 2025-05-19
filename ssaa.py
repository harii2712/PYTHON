a=[55,44,33,22]
min=a[0] #min=55
c=[]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
          b=a[i]-a[j]#11 22 33 11 22 11 
          if(b<min):#11<55
              min=b #min=11

for i in range(0,len(a)):
    for j in range(i+1,len(a)):
          b=a[i]-a[j]
          if(b==min):
              c.append(a[i])
              c.append(a[j])

c.sort()
print(c)





