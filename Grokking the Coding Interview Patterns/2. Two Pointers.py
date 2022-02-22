#In problems where we deal with sorted arrays (or LinkedLists) and need to find a set of elements that fulfill certain constraints, 
# the Two Pointers approach becomes quite useful. The set of elements could be a pair, a triplet or even a subarray 


#Two Pointers only works when the array is sorted 

#Two Pointers Time Complexity: O(N)
#Two Pointers Space Complexity: O(1)



#Problem 1: Pair with a target Sum(EASY)
arr=[1,2,3,4,6]
target_sum= 6 


    #Two Pointer Approach 

def two_pointer(arr,target_sum):
    left=0
    right = len(arr) - 1
    while(left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]

        if target_sum > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum
    return [-1, -1]


#Hashmap approach 


def two_p(array,target):
    l=0
    r=len(arr)-1
    while l<r:
        curr=array[l]+array[r]
        if curr==target:
            return [l,r]
        if curr>target:
            left +=1
        else:
            right-=1
    return [-1,-1]