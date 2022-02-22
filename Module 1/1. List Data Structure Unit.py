#List Data Structure 
#Dynamic Size
#Allows different sizes
print('___________________List (Dyanmic Sized Array) Introduction__________________')
print('___________________List Item Access__________________')
#Number inside are all indicies
l = [10,20,30,40,50]
print(l)
print(l[3])
print(l[-1])
print(l[-2])
print(l[1])
print(l[1:3])
print(l[-4])
print('___________________Accessing using negative indecies__________________')
#Accessing using negative indecies
print(l)
print(l[-2])
print(l[4])
print(l[3])
print(l[-4])
print(l[-4:-2])


print('_____________Insert and Search________________')

l.append(80) #This is the element 
print(l)
l.insert(2,75)         #inserts 75 at index 2
l.insert(4,90)         #inserts 90 at index 4
print(l)
print(15 in l)
print(90 in l)
print(20 in l)
print(l.count(30))
print(l.index(10)) #Does the first index of a function 
print(l.index(10,0,5)) 

print('____________Removal of items_____________')

l = [10, 20, 30, 40, 50, 60, 70, 80]
l.remove(20) # .remove  only  remove the value.
print(l)
print(l.pop()) # .pop return the removal item as output if nothing its just going to pop the last item 
print(l)
print(l.pop(2)) 
print(l)
del l[1]       #deletes items at index 
print(l)
del l[0:2]     #deletes the range of numbers from the two indexes
print(l)

print('________Some general purpose__________')

l=[10,40,20,50,90]
l.append(1000)
print(max(l))    #returns maximum 
print(min(l))   #returns minimum
print(sum(l))    #returns sum
l.reverse()     #reverses list
print(l)
l.sort()    #sorts list
print(l)

print('__________Average or Mean of a List __________')

#Average or Mean of a List 
l=[10,20,30,40]
def average_list(l):  #get the average of the list
    total_sum89 = 0
    for x in l:
        total_sum89 = total_sum89+x
    n=len(l)
    return total_sum89/n

#different way to do it 
def average_list2(l):
    return sum(l)/len(l)

print(average_list(l))
print(average_list2(l))

print('__________seperate even and odd__________')

#seperate even and odd

def getevenodd(l):
    even= [] # inititalize both empoty lists # Even List 
    odd= [] # odd list 

    for x in l:  # loop thriugh array d
        if x % 2 ==0:
            even.append(x)
        else:
            odd.append(x)
    return even, odd
l= [10,11,12,16]

print(getevenodd(l))

print('____________Get Smaller_____________')

l = [8,100,20,40,3,7]
x = 10
def getsmaller(l,x):   #Get elements smaller than the target 
    res = []
    for e in l:
        if e<x:
            res.append(e)
    
    return res
    


print(getsmaller(l,x))

print('_____________Slicing (List, Tuple, And String)________________')



#List slicing 
listslicing=[10,20,30,40,50]
print(listslicing[0:5:2])   # start:0, stop:5, step:2
print(listslicing[:4])       # start: 0, stop:4, step:1
print(listslicing[2:])
print(listslicing[1:4])
print(listslicing[4:1:-1])
print(listslicing[-1:-6:-1])  # Starts at -1 goes to -6 and decriments 
print(listslicing[::-1])
print(listslicing[0:5])
print(listslicing[:])         #returns the whole list 

#Slicing Difference Between List Tuple String 
l2=listslicing[:]


t1=(10,20,30)
t2=t1[:]

s1="geeks"
s2=s1[:]

print(listslicing is l2) #False #you always get a different list if you copy its not the same one 
print(t1 is t2) #True
print(s1 is s2) #True


print('____________List comprehension ___________')

#List comprehension 
listcomp = [x for x in range(11) if x % 2 ==0]
print(listcomp)

listcomp3 = [x for x in range(11) if x%2!=0]
print(listcomp3)

#which is the same as 
l7=[]
for x in range(11):
    if x %2==0:
        l7.append(x)

l8=[]
for x in range(11):
    if x%2 != 0:
        l8.append(x)


print('____________Set, Dict Comprehensions___________')


#Set, Dict Comprehensions
new_set={10,20,3,4,10,20,7,3}
new_list=[1,2,3,4,5]
s12={x for x in new_set if x%2==0}

print(s12)

s12={x for x in new_set if x%2 != 0}
print(s12)

s15={x:x**2 for x in new_list}
print(s15)

#d2 = {x:f"ID{x}" for x in range(5)} # dictionary comprehension
#print(d2)

l2 = [101,103,102]
l3 = ['gfg','ide','corse']

d3 = {l2[i]:l3[i] for i in range(len(l2)) }   # dictionary comprehension
print(d3)




d4 = dict(zip(l2,l3))
print(d4)


print('____________Inverting Dict___________')
d1 = {101:'gfg',103:'practice',102:'ide'}
d8 = {v:k for (k,v) in d1.items() }  #Inverts the dictionary where key is value and value is key 
print(d8)





print('---------------------------------------------------')
#O(n^2)
def getMax(new_list):
    for x in new_list:
        for y in new_list:
            if y>x:
                break
            else:
                return x
    return None
print(getMax(new_list))

#O(n)
def getMax2(new_list):
    if not new_list:
        return None
    else:

        res = new_list[0]                  # assume l[0] is the max
        for i in range(1, len(new_list)):  # iterate through index 1 to last
            if new_list[i] > res:           # check whether current element is greater than res
                res = new_list[i]          # if current element is greater than res ,update res to current
        return res

print(getMax2(new_list))
print('---------------------------------------------------')
def getSecMax(new_list):
    if len(new_list) <= 1:
        return None
    lar = getMax(new_list)
    slar = None

    for x in new_list:

        if x != lar:
            if slar == None:
                slar = x
            else:
                slar = max(x, slar)
    return slar
print(getSecMax(new_list))


print("--------------------------------------------------")
def isSorted(new_list):
    i = 1
     
    while i< len(new_list):
         
        if new_list[i]<new_list[i-1]:
             
            return False
        i=i+1
        
    return True
print(isSorted(new_list))

def isSorted2(l):
    new_list3 = sorted()
    
    if new_list==new_list3:
        return True
    else:
        return False

#print(isSorted2(new_list))
print("--------------------------------------------------")


#reverse a list in Python 
l23=[10,20,30,40]
rev_list=[10,20,30,40]
rev_list2=[10,20,30,40]
rev_list3= [10,20,30,40]

#method 1
rev_list.reverse()
print(rev_list)

#method 2
new_revl2 = rev_list2[::-1]
print(new_revl2)

#method 3
rev_list3= list(reversed(rev_list3))
print(rev_list3)

#swapping method
def reverse_list(l23):
    se=0 #left pointer
    es=len(l23)-1 #right pointer

    while se<es:
        l23[se],l23[es]=l23[es],l23[se]
        se=se+1
        es=es-1

(reverse_list(l23))

print(l23)


#rotate list by 1 
 
rotate_list= [10,20,30,40]

#using list slicing
x = rotate_list[1:] + rotate_list[0:1]


print(x)

#using pop  and append method 
rotate_list2=[10,20,30,40]
rotate_list2.append(rotate_list2.pop(0))

print(rotate_list2)

rotate_list3=[10,20,30,40]
    


#rotate by d places 
lro=[10,20,30,40,50]
d=2
lro=lro[d:]+lro[:d]
print(lro)

from collections import  deque
lro2=[10,20,30,40,50]
d=2

dq=deque(lro2)
dq.rotate(-d)
lro2 =list(dq)
print(lro2)

def leftRotate(lro2,d):
    for i in range(0,d):
        lro2.append(lro2.pop(0))

lro2=[10,20,30,40,50]
d=3
leftRotate(lro2,d)
print(lro2)

def reverse(lro2,b,e):
    while b<e:
        lro2[b],lro2[e]=lro2[e],lro2[b]
        b=b+1
        e=e-1


def leftRotate(l,d):
    n=len(lro2)
    reverse(lro2,0,d-1)
    reverse(lro2,d,n-1)
    reverse(lro2,0,n-1)


lro2=[10,20,30,40,50]
d=3
leftRotate(lro2, d)
print(lro2)

    

#Advantages and Disadvantages of a List in Python
#Advantages: Random Access, Cache Friendly
#Disadvantages: Insertion, Deletion are slow