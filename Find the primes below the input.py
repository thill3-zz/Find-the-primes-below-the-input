# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
print("Print this line")
print("Testing")
x = 2
if x == 2:
        print("x plus one is", x+1)
print("Goodbye World!")
integerOne = 5/7
print("IntegerOne is", integerOne)
StringOne = "This is a string with a'p'o's't'r'o'p'h'e's'."
print(StringOne)
StringTwo = "Let's"
StringThree = "Go"
StringFour = "Place."
print(StringTwo + " " + StringThree + " " + StringFour)
a,b = 3,4
print("a=",a)
print("b=",b)
print(b,a)
print(StringTwo, a)

mystring,myfloat,myint = "hello",10.0,20
print(mystring)
print(myfloat)
print(myint)

mylist = []
mylist.append(1)
print(mylist)
mylist.append(2)
print(mylist)
mylist.append(3)
print(mylist)
print([mylist[1]])
for i in mylist:
        print(i**2)

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")
second_Name = names[1]

print(numbers)
print(strings)
print(names)
print(second_Name)

number = 1+2*3/4%5
string = "Hello"
print(number)
print(2*string)

even_numbers = [0,0,0,0]
odd_numbers = [0,0,0,0]
for i in range(1,9):
    if i % 2.0 == 0.0:
        indexI = int(i/2-1)
        even_numbers[indexI] = i
    else:
        index = i/2.0-.5
        indexI = int(index)
        odd_numbers[indexI] = i
for j in range(0,4):
    print("j=",j)
    print("even_numbers[",j,"] =", even_numbers[j])
    print("odd_numbers[",j,"] =", odd_numbers[j])
all_numbers = [0,0,0,0,0,0,0,0]
for r in range(0,4):
    all_numbers[2*r] = odd_numbers[r]
    all_numbers[2*r+1] = even_numbers[r]

matrix = [1,2,3]*4

x_list = ["x"] * 10
y_list = ["y"] * 10
big_list = x_list + y_list
for i in range(0,20):
    print(i, big_list[i])

text1 = "This is testing script number 1"
text2 = "testing text number 2"
no1 = 23
no2 = 37
print("Your first Text is - %s. \nYour first number is - %d. \nYour second text is - %s. \nYour second number is - %d." % (text1, no1, text2, no2))

no3 = 37.52798
print("Your number as a float is %f.\nYour number as a digit is %d.\nYour number with only two digits is %.2f" %(no3, no3, no3))

List1 = [1,2,"Douglas"]
print("MyList: %s" % List1)

data = ["Hello", "John", "Doe"]
, ".", "Your", "current", "balance", "is", "$", "53.44", "."]

%s4 %s5 %s6 %s7 %s8 %s9""%s10""%s11" % data)
print(len(data))
print("List: %s" % data)

data = ("John", "Doe", 53.44)
formatString = ("Hello %s %s. Your current balance is $%.2f." % data)
print(formatString)

string = "hello john doe."
for i in range (0, len(string)):
    if i % 4 == 0:
        print(string[i].upper())
    else:
        print(string[i])

string = "hello john doe."
lowersearch = "Hello"
lowersearch = lowersearch.upper()
print(string.startswith(lowersearch))

string = "hello john doe."
splitstring = string.split("o")
print(splitstring)

s = "Strings at a b home!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

for i in range (0,11):
    if i % 3 == 0:
        print(i, "is divisible by 3.")
    elif i % 3 == 1:
        print(i, "is divisible my 3 with remainder 1.")
    else:
        print (i%3 == 2)
        print (i%3 is 2)

# change this code
number = 16
second_number = 0
first_array = [1,4,5]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
"""
import math
startList = []
primes = [1]
top = input('Top of range = ')
for i in range(1,int(top)+1):
    startList.append(i)
for j in startList:
    count = 1
    index = int(math.floor(j/2+.5))
    for k in range (2,index+1):
        if math.gcd(j, k) != 1:
            count += 1
        else:
            if count == 1 and k == index:
                if primes[len(primes)-1] != j:
                    primes.append(j)
print(primes)