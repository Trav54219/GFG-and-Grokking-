#sorting algorthims 
    #Bubble Sort 
        #Time Complexity O(n^2)

arr=[10,8,20,5]
arr2=[20,5,40,60]


print("-------------------------Bubble Sort---------------")
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

print(bubble_sort(arr))
    #Selection Sort
        #Time Complexity O(n^2)
print("-------------Selection Sort-------------")
def selectionsort(arr):
    n=len(arr)
    for i in range(n-1):  # Traverse through all array elements
        min_ind=i        # Find the minimum element in remaining
                            # unsorted array
        for j in range(i+1,n):
            if arr[j]< arr[min_ind]:  # Swap the found minimum element with
                min_ind=j            # the first element   
        arr[min_ind],arr[i]=arr[i], arr[min_ind]

(print(selectionsort(arr)))


    #Insertion Sort
        #Time Complexity O(n^2)
print("--------------Insertion Sort---------------")
def insertionSort(arr):
    for i in range(1,len(arr)):
        x = arr[i]
        j = i-1
        while j>=0 and x<arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = x

        
(print(insertionSort(arr)))






