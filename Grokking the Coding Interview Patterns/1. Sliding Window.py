#Sliding Window can be used for Linked List and Array Problems
#Calculate the contiguos amount of elements of something 

#Sliding Window General Formula 

def sliding_window(nums):
    #Interate over elements
        #Expand Window
        #Meet the condition to stop expansion 
            #Process the current window
            #Contract the window 






#Example 1 Find the average fo all contiguous subarrays of size k

K=5
array1=[1, 3, 2, 6, -1, 4, 1, 8, 2] 
#Brute Force approach (Very inefficient because there is a lot of overlap)
def findconsubarrays(array1,K):
    res=[]     
    for i in range(len(array1)-K+1):
        _sum=0.0
        for j in range(i, i+K):
            _sum += array1[j]
        res.append(_sum/K)
    return res 

print(findconsubarrays(array1d, K))


print("chicken")


#Slidning Window approach 
def slidingwindow(array, K):
    result = []
    windowSum=0.0
    windowStart = 0
    for windowEnd in range(len(array)):
        windowSum += array[windowEnd]  # add the next element
    # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if windowEnd >= K - 1:
            result.append(windowSum / K)  # calculate the average
            windowSum -= array[windowStart]  # subtract the element going out
            windowStart += 1  # slide the window ahead

    return result
            
print(slidingwindow(array, K))
    

#Understanding the Algorithm 
   #Def Function(Arr, Size):
        #window Sum =0.0
        #Window Start=0(or the first index)
        #For Window End in range(length of array)
            #Window_sum increment Arr[Window_end]
            #Window Sum decrement arr[Window_start] (Subrtract the element going out)
            #Window Start increment by 1 (Slide the window ahead)


#My Understanding of the Algorithm

#Function Definition (Arr,k(usually the size constraint))
    #Initialize Result
    #Initialize Start of the Window 
    #Initialize the Window Computational Value (Usually Zero)
    #For loop which is gonna be the length of the array (Iterator Signifying the Window End)
        #Sum gets updated as the window goes frome left to right
        #Condition to properaly size the window 
            #Subtract the element going out
            #move the window Foward
            #Computation based on teh condition of problem 

