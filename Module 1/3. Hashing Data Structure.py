#Time complexity 
    #Hash Map usually has a key value pair 
    #Search, Insert, Delete = O(1) or constant time  

#Instances in which hashing is not usuful for 
      #1.Finding closest value
      #2. Prefix Searching 
      #3. Sorted Data

#Applications of Hashing 
    #1. Dictionaries
    #2. Database Indexing 
    #3. Cryptography
    #4. Caches 
    #5. Symbol Tables in Compilers
    #6. Getting Data from Databases


#Set in Python 
    #1. Distinct elements 
    #2. Unordered
    #3. No Indexing 
    #4. Uses Hashing Internally 
    #5. Union , Intersection, Set Dilligence



s1={10,20,30}

s2=set([30,20,10])

s3={}
s4=set()
print(s1)
print(s2)
print(type(s3)) #Shows the type 
print(type(s4))

#Methods
(s1.add(80))
print(s1)

s2.update([10,90]) #adds new items to the set 
print(s2)

s2.update([10,89],[87,76]) #cant predict the order in which teh items are added 
print(s2)

new_set={10,20,30,40}
new_set.discard(10)
new_set.discard(30)
print(new_set)

new_set.clear() #clear function which wipes the set 
print(new_set)

new_set.add(109) #Add function 
print(new_set)

print(len(new_set)) #get the length of the set 
print(109 in new_set)
print(20 in new_set)

set_1={10,40,80,90}
set_2={56.90,87}

print(set_1.union(set_2))
print(s1.intersection(s2))
print(s1.difference(s2))


#Dictionaries in Python 
    #1. Collection of Key value Pairs 
    #2. Unordered 
    #3. All Keyys must be disctint 
    #4. Values must be repeated 

hashmap={110: "xyz",
        101: "abc",
        105: "bcd",
        104: "abc"}

print(hashmap[104],hashmap[105])

print("---------------Creating Dictionary")

#Creating a dictionary 

d={}  #empty dictionary
d["eggplant"]=105
d["sausage"]=789
d["water"]=865

print(d)
print(d["sausage"])

print(hashmap.get(110))
if "xyz" in hashmap:
    print("LETS GOOO")
else:
    print("NOOOOOOO")

#Other example cases
d12={110:"abc",
    101:"xyz",
    105:"pqr",
    106:"bcd"}

d12[110]="suck my dick"

print(len(d12))
print(d12)

(d12.pop(110))  #pop gives you the value that was deleted
print(d12)

del d12[101]  #del does not 
print(d12)

d12.popitem()#delets the last inserted key value pair

print(d12)

print("----------------Pratcie probelems")

#Return distinct items from a list 
l=[1,2,3,4,5,6,7,8,9,8]
#Method 1: count distinct items in a list 
def distinct(l):
    res=1
    for i in range(1, len(l)): 
        if l[i] not in l[0:i]:
            res=res+1

    return res

print(distinct(l))

#Method 2: Set method 
def fun2(l):
    s=set(l)
    return len(s)

print(fun2(l))


#Subarray with sum 0 in Python 
l_sub=[1,4,13,-3,-10,5]
l_sub2=[-1,4,-3,5,1]
l_sub3=[3,1,-2,5,6]
l_sub4=[5,6,0,8]
 

#O(n)^2
def subarray(l_sub):
    n=len(l_sub)
    for i in range(n):
        for j in range(i+1,n+1):
            if sum(l_sub[i:j])==0:
                return True
    return False

print(subarray(l_sub))


#O(n)
def isZeroSum(l_sub):
    pre_sum = 0

    h = set()

    for i in range(len(l)):
        pre_sum += l[i]
        if pre_sum == 0 or pre_sum in h:
            return True
        h.add(pre_sum)

    return False

print(isZeroSum(l_sub))


#Check for Palindormic Permutation 
stringpalin="geeksgeeks"


from collections import Counter
def isPalin(stringpalin):
    cnt=Counter(s)
    odd=0
    for freq in cnt.values():
        if freq %2 !=0:
            odd=odd+1
            return True
            if odd>1:
                return False
    return True