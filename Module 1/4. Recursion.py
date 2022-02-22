#Recursion Background

def fun1():
    print("fun1() caled")

def fun2():
    print("before fun1()called")
    fun1()
    print("after fun1() called")


print ("before fun2()")
fun2()
print("After fun2()")


#function calls execute in a last in first out manner


#example recursive function
def func1(n):
    if n<=0: #so it can handle negative numbers
        return
    print("GFG")
    func1(n-1)

func1(3)
print("-------------------------------Stop")

#applications of recursion

    #Algorithms Techniques based on recrusion 
        #1. Dynamic Prgramming 
        #2. Backtracking 
        #3. Divide and Conquer (Binary Search, QuickSort, MergeSort )

    #Many problems that are recursive in Nature 
        #1. Tower of Hanoi 
        #2. DFS based traversals (DFS of a graph and InOrder, PreOrder, PostOrder Traversal)



print("Practice for Recrusion Part 1---------------------")

def func2(n):
    if n==0:
        return
    print(n)
    func2(n-1)
    print(n)

func2(3)


print("-----------")
#elements to a recursive function 
#1. The base case
#2. The recursive call with at leats one change to the parameter so that all approaches towards a base case

def func3(n):
    if n==0:
        return
    func3(n-1)
    print(n)
    func3(n-1)

func3(3)


print("Practice for Recrusion Part 2---------------------")

def func4(n):
    if n <=1:
        return 0
    else:
        return 1 + func4(n//2)

func4(16)

def fun5(n):   #decimal to binary conversion 
    if n==0:
        return
    fun5(n//2)
    print(n%2)

print(fun5(13))

print("Sum of Natural Numbers Using recursion---------------------")

nat=int(input("Enter a Nat:"))
sum=nat*(nat+1)/2
print("total is", sum)


print("Print N to 1--------------------")

def ntoone(n):
    if n==0:
        return
    print(n)
    ntoone(n-1)

print(ntoone(5))


print("Print 1 to N--------------------")

def oneton(n):
    if n==0:
        return 
    oneton(n-1)
    print(n)

print("Print Sum of Digits Using Recursion--------------------")
def dsum(n):
    if n < 10:
        return n
    else:
        return dsum(n//10) + n%10

print(dsum(253))


print("Tower of Hanoi-------------------")
def TOH(n,A,B,C):
    if n==1:
        return("Move 1 from",A,  "to", C)
    else:
        TOH(n-1, A, B,C)
        print("Move", n, "from", A, "to", C)
        TOH(n-1, B, A, C)

print(TOH(2,'A','B','C'))