print("Binary Search---------------")
#binary search is an optimal searching algorithm for a sorted array/list
l=[10,20,30,40,50,60]

def binarysearch(l,x):
    low = 0  #Two pointers 
    high = len(l)-1 
    while low<=high:  #condition
        mid=(low+high)//2   #defining mid 
        if l[mid]==x: #first case 
            return mid
        elif l[mid]<x: #second case 
            low=mid+1
        else:           #third case 
            high=mid-1
    return -1

print(binarysearch(l,30))

print("Binary Search recusive case-----------")  
def binarysearch2(l,x, low, high):
    if low> high:
        return -1
    mid=(low+high)//2
    if l[mid]==x:
        return mid
    elif l[mid]>x:
        return binarysearch2(l,x,low,mid-1)
    else:
        return binarysearch2(l,x,mid+1,high)


#Anlysis of a Binary Search is O(log(n))


print("Index of the first occurrance")

def firstIndex(l, x):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] > x:
            high = mid - 1
        elif l[mid] < x:
            low = mid + 1
        else:
            if mid == 0 or l[mid - 1] != l[mid]:
                return mid
            else:
                high = mid - 1
    return -1

print(firstIndex(1,30))


print("Last Occurance-----------")
def lastOccur(l, x):
    low = 0
    high = len(l) - 1

    while low <= high:

        mid = (low + high) // 2

        if l[mid] < x:
            low = mid + 1

        elif l[mid] > x:
            high = mid - 1

        else:

            if mid == len(l) - 1 or l[mid] != l[mid + 1]:
                return mid
            else:
                low = mid + 1
    return -1

print("count coccurances in a sorted array----------------")
def countOccurr(l, x):
    first = firstIndex(l, x)

    if first == -1:
        return 0

    else:
        return lastOccur(l, x) - first + 1

for i in range(1,100):
    print(i)
