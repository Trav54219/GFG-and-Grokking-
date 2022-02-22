#Time Complexities

#O(1)-Constant
    #Ex:  Odd or Even Number
    #     Look up Table(on average)
  
#O(log(n))-Logarithmic
    #Ex:  Finding element on sorted array with binary search

#O(n)- Linear
    #Ex:  Find max element in an unsorted array
    #     Duplicate elements in array with Hashmap 

#O(n(logn(n)))-Loglinear
    #Ex:  Sorting elements in array with merge sort

#O(n^2)- Quadratic
    #Ex:  Duplicate elements in an array
    #     Sorting array with bubble sort 

#O(n^3)- Cubic
    #Ex:  3 variables equation solver

#O(2^n)- Exponential
    #Ex:  Find all subsets

#O(n!)- Factorial
    #Ex:  Find all permutaions of a given set/string


print("_________________Analysis of Algorithms Background___________________")

    
#Sum of first n natural numbers
#We mainly measure order of growth in 

def fun1(n):
    return n * (n+1)/2

print(fun1(5))

def fun2(n): #O(n)
    count=0
    for i in range(1,n+1):
        count=count+i
    return count



print(fun2(5))


def fun3(n):     #O(n^2)
    sum=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum=sum+1
    return sum

print(fun3(5))

#The main Idea of an algorithm is to measure order or growth of the inpit size

print("_________________Analysis of Common Loops___________________")
n=5
c=10
i=0
while i<n:  #O(n) Time Complexity
    i=i+c

#Equivilant Code
i=1 
while i <n:  #O(Log(n))
    i=i*c

i=n
while i>1: #O(Log(n))
    i=i/c


i=2
while i<n:  #O(log(log(n)))
    i=i**c


#subsequent loops
i=0
while i<n:  #O(n)
    i=i+2
i=1
while i<n: #O(log(n))
    i=i*3
i=1
while i<100: #O(1)
    i=i+1

    #Order of Growth of the whole thing is #O(n)

#Nested Loop Example
i=0
while i<n:  #O(n(log(n)))
    j=1
    while j<n:
        j=j*2
    i=i+1


#Mixed Loops Example 
i=0
while i<n:  #Time comeplexity of this whole thing is #0(n^2)
    j=1
    while j<n:
        j=j*2
    i=i+1
i=0
while i<n:
    j=1
    while j<n:
        j=j+1
    i=i+1




print("_________________Analysis of Recursion___________________")
def fun(n):
    if n==1:
        return 
    for i in raneg(n):
        print("GFG")
    fun(n/2)
    fun(n/2)

def fun2(n): #O(1) Time complexity 
    if n==1:
        return 
    print(n)
    fun2(n-1)


#Recurion Tree Method 
#Divide every recurion into two parts: 1. Recursive part and Non Recursive Part d\

print("_________________Space Complexity___________________")
def getSum1(n):  #O(1) Space Complexity 
    return n*(n+1)/2

def getSum2(n): #O(1) Space Complexity 
    sum=0
    i=1
    while i<n:
        sum=sum+i
        i=i+1
    return sum


l=[1,2,3,4,5]
def letSum(l):  #Space is proportional to the length of the list so its going to be O(n) Space
    sum=0       #O(1) Auxilary Space 
    for x in l:
        sum=sum+x
    return sum

#Auxilary Space: Order of Growth of extra space other than input or output
#Auxilary Space is the space above 

def fun4(n):
    if n <=0:    #O(n) Space 
        return 0  #O(n) Auxilary Space
    else:
        return n+fun(n-1)
