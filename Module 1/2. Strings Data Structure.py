s ="welcom to the geeks for geeks course"
print(s)

s_withslash="Welcome to geek\'s for geek\'s course"
print(s_withslash)

#Putting apostrophe's without a back slash creates an invalid syntax error 

s_backslashn= "Hi,\n I love cheese"
print(s_backslashn)

#\n is an escape sequence which skips to a new line

#you can make a raw sting by putting an r befoe a string 
raw_string= r"c:\project\name.py"
print(raw_string)

print("------------------------------------------------------------")

#reverse a string(Strings are immutable)

#method 1(for loop)


s = input("Enter a String:\n")
print("------------------------------------------------------------")
rev = ""  #inititalize an empty string 

for i in s:  #iterate through every character in the string 
    rev = i+rev       #update revere(take the character and add it in front of an already stored character until there is no more so it can out put what appears to be a reveres string )

print(rev)


#Method 2 (slicing)
s_rev = input("Enter a String:\n")
s_rev[::-1]
print(s_rev)

print("------------------------------------------------------------")

#sring comparison 

scomp1="geeks for geeks"  #g is smaller is i they go in alphabetical order


scomp2="ide"            #lower case character have a higher value than uppercase

#Strings compare character by character 

#doesnt matter how big the string

print(scomp1 < scomp2) #g come before i 
print(scomp1 <= scomp2)
print(scomp1 > scomp2)
print(scomp1 >= scomp2)
print(scomp1 == scomp2)
print(scomp1 != scomp2)

print("------------------------------------------------------------")

print("abcd > abc ","abcd">"abc")
print("ZAB>ABC","ZAB">"ABC")

print("abc>ABC","abc">"ABC")

print("x>abcd","x">"abcd")


#Strings Definitions
#1. Sting is a sequence of chraacters 
#2. Typically a small set of characters 

#lowercase starts from 97 - 122
#uppercase starts from 65-90

#lowercase has a bigger order than uppercase 
print(ord("a"))     # chr to ord  
print(ord("A"))
print(chr(97))      # ord to chr
print(chr(65))

print(ord("C"))

sindex= "Roblox"
print(sindex[::-1])  #reverse the string 
print(sindex[-3])     #returns the l in Roblox
print(sindex[0])      #returns the R in Roblox
print(sindex[0:2])


stringsub = "freeCodeCamp"
print(stringsub[0:5])  #returns a substring
#strings are immutable in python 

print("--------------------------------------------------")

#muliti line string       #use three quotes to do a multi line string 
multilinestring= """Hi      
My name is 
Travis """

print(multilinestring)


print("--------------------------------------------------")

#string formatting using f strings

#f strings are pretty good

names="ABC"
course="python course"

select= f"My name is {names} and I am taking the {course}"   #f strings are pretty good
print(select)


ab= 20
ba = 4

print(f"the sume of {ab} and {ba} is {ab + ba}")
print(f"the product of {ba} and {ab} is {ab * ba}")


exampletter1="def"
exampletter2="ABC"

print(f"the lowercase of {exampletter2} is {exampletter2.lower()}")
print(f"the uppercase of {exampletter1} is {exampletter1.upper()}")

#string operations

#1. Checking substrings 
s1= "geeks for geeks"
s2= "geekks"

print(s2 in s1)  #should return True
print(s1 in s2)  #should return False 

#2. Concatination 
s12="geeks"
s123= "like food"
s1234= "hot"

print(s12 + " " + s123 + " " + s1234)

#other example
sub= "welcome to the"
sub2= "show"
sub3= sub + " " + sub2
print(sub3)

#3. Checking Indexes
s1index = "geeksforgeeks"
s2index = "geeks"

print(s1index.index(s2index))
print(s1index.rindex(s2index))        # right index
print(s1index.index(s2index,1,13))    # start and end index

#string Operations Part 2
#Upper and Lower methods

s1str = "geeks"

print(len(s1str))

s2str = s1str.upper()

print(s2str)

s3str = s2str.lower()

print(s3str)

print(s1str.islower())

print(s2str.isupper())

st = "GeeksforGeeks Python Course"

print(st.startswith("Geeks"))

print(st.endswith("Course"))

print(st.startswith("Geeks", 1))     # start index

print(st.startswith("Geeks",8,len(st)))   # start index, last-index


s1 = "geeks for geeks"

print(s1.split())   # split by space ' '


s2 = "geeks, for, geeks"
print(s2.split(','))        # split by comma ','

l = ["geeksforgeeks","python","course"]

print(" ".join(l))          # join by space

print(", ".join(l))         # join by comma


print("strip methdo---------------------------------")

s1 = "__geeksforgeeks__"

print(s1.strip("_"))   # strip from both side


print(s1.lstrip('_'))  # strip from left side


print(s1.rstrip("_"))   # strip from right side

print("find method---------------------------------")

find_string="Geeks for geeks"
find_string2="geeks"

print(find_string.find(find_string2))

print("----------------------Pattern Searching in Python")

txt="Geek for Geeks"
ptt="Geeks"

txt1=input("Enter txt:")
ptt2=input("Enter txt:")


pos=txt1.find(ptt2)
while pos >= 0:
    print(pos)
    pos=txt1.find(ptt2, pos+1)


print("--------------------Find the Palindrome in a String")


#first Method
palistring1=input("Enter a String for a Anagram Check:") #User inputs a string 
#Two Pointers
low=0
high=len(palistring1)-1

while low < high:
    if palistring1[low]!= palistring1[high]:
        print("No")
        break
    low= low + 1
    high = high - 1
else:
        print("yes")


palistring2=input("Enter a String for a Palindrome Check:") #User inputs a string 

if palistring2 == palistring2[::-1]:
    print("yes")
else:
    print("No")


print("--------------------Check for Anagram")

anacheck1= input("string example1:")
anacheck2= input("string example2:")


def anagramcheck(anacheck1,anacheck2):
    if len(anacheck1) != len(anacheck2):    #Time Complexity is O(Log(n))
        return False

    anacheck1.sorted(anacheck1)
    anacheck2.sorted(anacheck2)
    return(anacheck1==anacheck2)


#More Efficcient Solution 
#Go over a more efficient solution and rewrite the code


