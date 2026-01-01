def square1(n):
    return n*n
def square2(list1):
    list2=[]
    len1=len(list1)
    for i in range(0,len1,1):
        n=list1[i]
        list2.append(square1(n))
    return list2
def cube1(n):
    return n*n*n
def cube2(list1):
    list2=[]
    len1=len(list1)
    for i in range(0,len1,1):
        n=list1[i]
        list2.append(cube1(n))
    return list2
    
    
n=5
list1=[5,6,7,8]

result=square1(n)
print("Square of",n,"is",result)

result=square2(list1)
print("Squares of",list1,"are",result)

result=cube1(n)
print("Cube of",n,"is",result)

result=cube2(list1)
print("Cubes of",list1,"are",result)
