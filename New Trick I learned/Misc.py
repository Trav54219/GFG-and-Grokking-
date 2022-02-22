arr=[10,20,30,40,60,90]
target=60
def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return arr[mid]
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

print(binary_search(arr,target))



        