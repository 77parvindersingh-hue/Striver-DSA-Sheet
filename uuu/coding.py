# # name = input()
# # print('My name is',name)
# # print('hello')


# # # directly printing in output.txt
# # print("hello")


# # # taking input from input.txt and printing it in output.txt
# # name = input()
# # age = int(input())
# # salary = float(input())
# # isadmin = bool(input())


# # print(name,type(name))
# # print(age,type(age))
# # print(salary,type(salary))
# # print(isadmin,type(isadmin))

# # #taking 3 space seprated integer value as integer
# # a,b,c = map(int,input().split())
# # print(a,b,c)

# # # taking multiple integer inputs
# # lst = list(map(int,input().split()))
# # print(lst)

# # DAY-3

# # working on a list
# # l = [1,2,3,4]
# # print(l)

# # # adding an element in a list
# # # append only add an element in the last
# # l.append(66)
# # print(l)
# # # but if we want to add in middle
# # l.insert(1,11)
# # print(l)
# # # to delete an element
# # l.pop(4) # 4 is the index 
# # print(l)
# # l.pop(1)
# # print(l)
# # # updating a lst 
# # l[2] = 12
# # print(l) #see in output.txt 3 is replaced by 12
# # # getting an element from the list
# # print(l[1]) # put the index of the element u want


# # # Tuples

# # n = (4,5,71,96748,6566)
# # print(n)
# # print(type(n))
# # # getting any data from a tuple
# # print(n[4]) # 4 is index here



# # # Dictionary

# # d = {'orange':5,'apple':4,'mango':12,'grapes':7}
# # print(d)
# # print(type(d))

# # # getting a data from a list
# # print(d['apple']) # here apple is the key

# # # adding an element 
# # d['banana'] = 8
# # print(d)

# # # updating a element in dict
# # d['orange'] = 13
# # print(d)

# # #remove an element from dict
# # del d['apple'] # the key and value of apple will be deleted
# # print(d)

# # # SET

# # s = {1,2,3,7,5,68,26,6,5}
# # print(s,type(s))

# # # adding element in set
# # # set always hold unique value
# # s.add(12)
# # s.add(7)
# # s.add(1)
# # #only 12 will be added as 7 and 1 are already present in the set 
# # print(s)

# # # getting a value in set
# # # it awlways give in true and false
# # # if value will be present it will give true 
# # print(14 in s) # false as 14 is not in set
# # print(1 in s)

# # # removing an element 
# # print(s.remove(1))
# # print(s)


# # #DAY-4

# # # Mutable - Something that can be changed
# # # eg - List, Dictionary, Set, etc.
# # # Immutable - something that can't be changed
# # # eg- int, float, bool, string, tuple, etc.

# # x = 7
# # print(x)


# # x = 5
# # print(x)
# # # since I said int is immutable but I am getting a updated value when
# # # I print it. So, the logic behind it is that its id are different 

# # x = 5
# # print(id(x))

# # x = 7
# # print(id(x))


# # # Data Conversion 

# # a = 4.5
# # print(a,type(a))

# # b = int(a)
# # print(b,type(b))

# # c = str(a)
# # print(c,type(c))

# # l = [1,2,3,4,5,6]
# # print(type(l))

# # s = set(l)
# # print(type(s))

# # t = tuple(l)
# # print(t,type(t))

# # # converting into a dict

# # colour = ['orange','red','brown','blue']
# # qty = [15,45,21,54,46]

# # d = dict(zip(colour,qty)) #we use zip function for dict.
# # print(d,type(d))

# # print(bool([]),bool({}),bool(()),bool(0),bool(0.0),bool(""))
# # # it will give false

# # print(bool([1,2]),bool({1,2}),bool((1,2)),bool(5),bool(0.2),bool("a"))


# # # use of converting in real life
# # # eg - u want to a list of unique elements from a mixed list 
# # lst = [1,6,4,2,26,74,5,6,45,25,1,2,3,4,5,6,7,5,6,1]

# # s = list(set(lst))
# # print(s) # a list of unique elements


# # DAY-5

# # Slicing - helps us to extract data from a list or a string

#  = 'Sanjay Bisht'
# prinnamet(name[0:12])
# print(name[0:12:1])
# #syntax = print(name[str.index:end index : step])
# print(name[0::2])
# print(name[0:]) # by default it will take step=1 and end index will
#                 # be 12
# print(name[-1::-1])
# print(name[-1:-12:-2])
# print(name[0:5]) #it always print -1 end index  value

# # same u can apply for a list

# # ques- prove list is mutable
# l = [1,2,3,4]
# print(l,id(l))
# l.append(5)
# print(l,id(l))
# # since the id of list is same therefore list is mutable

# # Condiional Statement 

# # If-Else 
# target = 125
# runs = 120
# if runs>target:
#     print('we won')
# else:
#     print('we lost')

# # If-Elif
# marks = int(input(''))
# if marks>=90:
#     print('A')
# elif marks>=75:
#     print('B')
# elif marks>=60:
#     print('C')
# elif marks>=33:
#     print('D')
# else:
#     print("FAIL")


# DAY-6

# LOOPs

# loops have three parts:
# 1. Condition
# 2. Operation
# 3. Updation


# While Loop

# pushup = 1
# while pushup<=15:
#     print('Do one pushup')
#     pushup = pushup+1

# # For Loop

# # Print name Raj 20 times
# for Raj in range(1,20):
#     print('raj')

# for num in [2,4,5,6]:
#     print(num)

# # print numbers from 1 to 10
# for num in range(1,11):
#     print(num)

#     #    OR

# for num in [1,2,3,4,5,6,7,8,9,10]:
#     print(num)

# # Loop to print list and index both together'
# l = [1,2,3,45,6,7]
# n = len(l)
# for i in range(n):
#     print(i,l[i])

# # question find the index of 17 in the list
# l = [1,2,3,4,56,7,17,56,76,78,64]
# k = 17

# n = len(l)

# ans = -1
# for i in range(n):
#     if l[i] == k:
#         ans = i
#         break
# print(ans)       


# DAY-7

# # Functions in Python

# # print sum of 3 numbers

# def sum(a,b,c):
#     print(a+b+c)

# sum(5,12,7)

# # use function and print a list and add it

# def sum(lst):
#     for num in lst:
#         print(num)
#     sm = 0
#     for num in lst:
#         sm = sm + num
#     print(sm)
   
# lst = [1,2,3,4,5,6,7,8,9]
# sum(lst)
 

# # Create a list and add 1 in every element

# def update(lst):
#     n = len(lst)
#     for i in range(n):
#         lst[i] = lst[i]+1

# lst = [1,2,3,4,5,6]
# update(lst)
# print(lst)

# Time Complexity
# Time complexity is a way of describing how the runtime of an algorithm
# grows as the size of the input (usually denoted as n) increases. 
# It isn’t about measuring seconds or minutes—since those depend on
# your hardware—but rather about counting the number of operations
# performed.

# Think of it as the "efficiency grade" of your code.
# Types of Time Complexity
# 1. Best Time
# 2. Worst Time
# 3. Average Time

# space complexity measures how much memory (RAM) your algorithm 
# needs to run as the input size ($n$) grows.
# Space complexity is actually the sum of two parts:

# Auxiliary Space: Extra or temporary space used by the algorithm
# (e.g., creating a new temporary list).

# Input Space: The space occupied by the input itself.
# Why Space Complexity Matters
# In modern computers, RAM is plentiful, but it isn't infinite. Understanding space
# complexity is critical when:
# 1. Working with Big Data: Processing a 10GB datasetwith an $O(n)$ algorithm might crash a machine with
# 8GB of RAM.
# 2. Embedded Systems: Coding for hardware with very limited memory (like a smartwatch or a sensor).
# 3. In-place Algorithms: Some algorithms, like Heapsort, are famous because they sort data using $O(1)$
# extra space, making them very memory-efficient


# # DAY - 8

# # Pattern Problemss

# # write a code to print
# # *****
# # *****
# # *****
# # *****
# # *****

# n = 5

# for i in range(n):
#     print("*****")

# #     OR
# print('or another ')


# n = 5
# for i in range(n):
#     for j in range(n):
#         print('*',end='')
#     print()
# # time complexit for it will be O(n**2) as one for i loop n times and one j loop n time 

# # write a code to print
# # *
# # **
# # ***
# # ****
# # *****

# n = 5

# for i in range(n):
#     for j in range(i+1):
#         print('*',end='')
#     print()


# # WAP to print
# # 1
# # 12
# # 123
# # 1234
# # 12345

# n = 5

# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end='')
#     print()


# # WAP to print
# # 1
# # 22
# # 333
# # 4444
# # 55555


# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(i+1,end='')
#     print()


# # WAP to print
# # *****
# # ****
# # ***
# # **
# # *

# n = 5 
# for i in range(n):
#     for j in range(n-i):
#         print('*',end='')
#     print()


# # WAP to print
# # 12345
# # 1234
# # 123
# # 12
# # 1

# n = 5

# for i in range(n):
#     for j in range(n-i):
#         print(j+1,end='')
#     print()


# # WAP to print
# # 1
# # 2 3
# # 4 5 6
# # 7 8 9 10 
# # 11 12 13 14 15

# n = 5
# k = 1

# for i in range(n):
#     for j in range(i+1):
#         print(k,end=' ')
#         k += 1
#     print()


# # WAP to print
# # A 
# # AB 
# # ABC 
# # ABCD
# # ABCDE

# def numtochar(num):
#     return chr(num+65)

# n = 5

# for i in range(n):
#     for j in range(i+1):
#         print(numtochar(j),end='')
#     print()


# # WAP to print
# # A 
# # BB 
# # CCC
# # DDDD
# # EEEEE



# def numtochar(num):
#     return chr(num+65)

# n = 5

# for i in range(n):
#     for j in range(i+1):
#         print(numtochar(i),end='')
#     print()




# DAY - 9


# Basic Maths Problems

# Count the total integers in a number

num = 123
ans = len(str(num))
print(ans)


# OR

def countnum(num):
     return len(str(num))

num = int(input())
ans = countnum(num)
print(ans)

# OR

print('using loop')

num = int(input())
cnt = 0
while num>0:
     num = num//10
     cnt +=1
     print(cnt)


# Reverse a number 


print('reverse number is :')


def reversenum(num):
    ans = 0
    while num>0:
         rem = num%10
         ans = ans*10+rem
         num = num//10
    return ans
num = int(input())
ans = reversenum(num)
print(ans)


# Pallindrome

print('Pallindrome true or false:')


def reversenum(num):
    ans = 0
    while num>0:
         rem = num%10
         ans = ans*10+rem
         num = num//10
    return ans

def pallindrome(num):
     return num == reversenum(num)


num = int(input())
ans = pallindrome(num)
print(ans)


# Finding GCF

print('gcf is ')

def gcd(a,b):
     divisor = min(a,b)
     dividend = max(a,b)
     while dividend%divisor!=0:
          temp = dividend
          dividend = divisor
          divisor = temp%divisor
     return divisor

ans = gcd(10,12)
print(ans)

ans = gcd(17,11)
print(ans)


# Check whether a number is Armstrong



def armstrong(num):
     ans = 0
     k = countnum(num) # this is used from count function made above
     temp = num

     while num>0:
          rem = num%10
          ans = ans + rem**k
          num = num//10
     return temp == ans

ans = armstrong(153)
print(ans) 

ans = armstrong(13)
print(ans) 


# print all the divisors

print('divisor is: ')

def numdivisor(num):
     for i in range(1,num+1):
          if num%i==0:
               print(i)

numdivisor(12)

# Check it is prime or not 

print('it is prime or not')

def isprime(num):
     for i in range(2,num):
          if num%i==0:
               return False
     return True

ans = isprime(225)
print(ans)

ans = isprime(17)
print(ans)

