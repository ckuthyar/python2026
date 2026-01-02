#Write a program to print 20 prime numbers in an order
#1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97

list1=[1,2,3]

'''
num1=4
is 4 divisible by 2 -  yes, it is not a prime. Exit the program

num1=5
is 5 divisible by 2 -  No. go to next step
is 5 divisible by 3 -  No. go to next step
is 5 divisible by 4 -  No. go to next step.......Add num1 to list1

num1=6
is 6 divisible by 2 -  Yes. it is not a prime. Exit the program

num1=7
is 7 divisible by 2 - No. go to next step
is 7 divisible by 3 - No. go to next step
is 7 divisible by 4 - No. go to next step
is 7 divisible by 5 - No. go to next step
is 7 divisible by 6 - No. go to next step......Add num1 to list1

num1=8
is 8 divisible by 2 - Yes. it is not a prime. Exit the program
'''
print(list1)

num1=4
isPrime=True
if num1%2==0:
    isPrime=False
        
if isPrime==True:
    list1.append(num1)
    print(list1)


    

num1=5
isPrime=True
if num1%2==0:
    isPrime=False
if num1%3==0:
    isPrime=False
if num1%4==0:
    isPrime=False

if isPrime==True:
    list1.append(num1)
print(list1)



num1=6
isPrime=True
if num1%2==0:
    isPrime=False
if num1%3==0:
    isPrime=False
if num1%4==0:
    isPrime=False
if num1%5==0:
    isPrime=False

if isPrime==True:
    list1.append(num1)
    print(list1)
    

num1=7
isPrime=True
if num1%2==0:
    isPrime=False
if num1%3==0:
    isPrime=False
if num1%4==0:
    isPrime=False
if num1%5==0:
    isPrime=False
if num1%6==0:
    isPrime=False

if isPrime==True:
    list1.append(num1)
    print(list1)







