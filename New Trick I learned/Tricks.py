#Rounding up without the round operator


import math
year=1905
def centuryfromyear(year):
    return math.ceil(year/100)

print(centuryfromyear(year))


my_string = "Hello"


def exclamation(my_string):
    my_string = "!!" + my_string + "!!"
    return my_string


exclamation(my_string)
print(my_string)


#Getting the frequency of elements in a hashmap 
#And adding to a Hashmap
lst1=["tree","tree","dog","bark","wet","wet","wet"]
hashmap={}

for elem in lst1:
    if elem in hashmap:
        hashmap[elem]+=1
    else:
        hashmap[elem]=1

print(hashmap)

#for values in hashmap.values():
  #  if values >2:
      #  return h

new_hash=dict()
for i in range(1,11):
    new_hash[i]=1


print(new_hash)


#Kudane Algorithms Pseudocode
