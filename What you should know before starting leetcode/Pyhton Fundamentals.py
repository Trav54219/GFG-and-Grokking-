#Print Statements 
print("Example Print Statement") #Prints a String 

#Data types
print(type(True))
print(type(5))
print(type("letter"))
print(type(8.0))

#Variables
variable=9
variable=1 #Origionally 9 but it is now 1
print(variable)

#Integers, Floats , complex numbers 

complex_number=complex(2,19)
print(complex_number)

mathematics=34-10 #Does simple computations 

print(mathematics)

floating_number=98.9
random=105
print(floating_number)


#math
print(int(random)-float(floating_number))

#Booleans 
right=True
wrong=False

#Strings
example_string="Egg, Cheese and Bacon Sandwich"
print(example_string)

new=example_string[-1] #Gets the last character in the string 
print(new)

empty=""
print(empty)

how_long=len(example_string)
print(how_long)

last=example_string[len(example_string)-1]

print(last)

random_character=example_string[-5]
print(random_character)

#You can do forward and reverse indexing 
#Strings are immutable in Python so you cant update them 

#verifiying the id of a string 

str1 = "hello"
print(id(str1))

str1 = "bye"
print(id(str1))

#slicing with a step 

my_string = "This is MY string!"
print(my_string[0:4]) # From the start till before the 4th index
print(my_string[1:7])
print(my_string[8:len(my_string)]) # From the 8th index till the end

#reverse stepping with a string 
my_string = "This is MY string!"
print(my_string[13:2:-1]) # Take 1 step back each time
print(my_string[17:0:-2]) # Take 2 steps back. The opposite of what happens in the slide above


my_string = "This is MY string!"
print(my_string[:8])  # All the characters before 'M'
print(my_string[8:])  # All the characters starting from 'M'
print(my_string[:])  # The whole string
print(my_string[::-1])  # The whole string in reverse (step is -1)
print(my_string[1::])



print(10*5) #50

print(10%3) #1

print(19.0-15.5) #3.5

print(float(30)+float(60)) #90.0

print(10 - 5)

float1 = -18.678
float2 = 3.55
print(float1 - float2)

num = 20
flt = 10.5
print(num - flt)

print(40 * 10)

float1 = 5.5
float2 = 4.5
print(float1 * float2)

print(10.2 * 3)

print(40 / 10)

float1 = 5.5
float2 = 4.5
print(float1 / float2)
print(12.4 / 2)

print(43 // 10)

float1 = 5.5
float2 = 4.5
print(5.5 // 4.5)
print(12.4 // 2)

print(10 % 2)

twenty_eight = 28
print(twenty_eight % 10)

print(-28 % 10)  # The remainder is positive if the right-hand operand is positive
print(28 % -10)  # The remainder is negative if the right-hand operand is negative
print(34.4 % 2.5)  # The remainder can be a float
