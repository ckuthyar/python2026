n=1234
list1=[]

temp1=n%10
temp2=n//10
digit4=temp1
list1.append(str(temp1))

n=temp2
temp1=n%10
temp2=n//10
list1.append(str(temp1))


n=temp2
temp1=n%10
temp2=n//10
list1.append(str(temp1))


n=temp2
temp1=n%10
temp2=n//10
list1.append(str(temp1))
print(list1)
s1="".join(list1)
print(s1)
