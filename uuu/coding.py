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




# # DAY - 9


# # Basic Maths Problems

# # Count the total integers in a number

# num = 123
# ans = len(str(num))
# print(ans)


# # OR

# def countnum(num):
#      return len(str(num))

# num = int(input())
# ans = countnum(num)
# print(ans)

# # OR

# print('using loop')

# num = int(input())
# cnt = 0
# while num>0:
#      num = num//10
#      cnt +=1
#      print(cnt)


# # Reverse a number 


# print('reverse number is :')


# def reversenum(num):
#     ans = 0
#     while num>0:
#          rem = num%10
#          ans = ans*10+rem
#          num = num//10
#     return ans
# num = int(input())
# ans = reversenum(num)
# print(ans)


# # Pallindrome

# print('Pallindrome true or false:')


# def reversenum(num):
#     ans = 0
#     while num>0:
#          rem = num%10
#          ans = ans*10+rem
#          num = num//10
#     return ans

# def pallindrome(num):
#      return num == reversenum(num)


# num = int(input())
# ans = pallindrome(num)
# print(ans)


# # Finding GCF

# print('gcf is ')

# def gcd(a,b):
#      divisor = min(a,b)
#      dividend = max(a,b)
#      while dividend%divisor!=0:
#           temp = dividend
#           dividend = divisor
#           divisor = temp%divisor
#      return divisor

# ans = gcd(10,12)
# print(ans)

# ans = gcd(17,11)
# print(ans)


# # Check whether a number is Armstrong



# def armstrong(num):
#      ans = 0
#      k = countnum(num) # this is used from count function made above
#      temp = num

#      while num>0:
#           rem = num%10
#           ans = ans + rem**k
#           num = num//10
#      return temp == ans

# ans = armstrong(153)
# print(ans) 

# ans = armstrong(13)
# print(ans) 


# # print all the divisors

# print('divisor is: ')

# def numdivisor(num):
#      for i in range(1,num+1):
#           if num%i==0:
#                print(i)

# numdivisor(12)

# # Check it is prime or not 

# print('it is prime or not')

# def isprime(num):
#      for i in range(2,num):
#           if num%i==0:
#                return False
#      return True

# ans = isprime(225)
# print(ans)

# ans = isprime(17)
# print(ans)


# # DAY - 10

# # ques- given a number. print its prime or not 

# num = int(input())

# def isprime(num):
#     for i in range(2,num):
#         if num%2==0:
#             return False
#     return True

# ans = isprime(num)
# print(ans)



# # given a series print its prime or not 

# series = list(map(int,input().split()))

# def isprime(num):
#     for i in range(2,num):
#         if num%2==0:
#             return False
#     return True

# for item in series:
#     ans = isprime(item)
#     print(item,ans)
# # ans = isprime(num)
# # print(ans)


# # The Sieve of Eratosthenes is one of the most efficient ways to find all prime numbers up to a specific 
# # limit, $n$. Instead of checking every single number to see if it’s prime (which takes a long time), 
# # this algorithm works by eliminating multiples.


# numbers = list(map(int, input().split()))
# def sieve(n):
#     # Create a boolean array "is_prime[0..n]" and initialize
#     # all entries it as true. 
#     is_prime = [True] * (n + 1)
#     is_prime[0] = is_prime[1] = False # 0 and 1 are not prime
    
#     p = 2
#     while (p * p <= n):
#         # If is_prime[p] is not changed, then it is a prime
#         if is_prime[p] == True:
#             # Update all multiples of p
#             for i in range(p * p, n + 1, p):
#                 is_prime[i] = False
#         p += 1     
    
#     # Return list of primes
#     return [i for i in range(n + 1) if is_prime[i]]

# for n in numbers:
#     print(f"Primes up to {n}: {sieve(n)}")



# # DAY - 11


# # Recursion: It is a process of calling a function again and again until a specific condtion is met


# # Questions - 

# # 1. Print a Name n times

# def printN(n):
#     if n==0:
#         return
#     print('raj')
#     printN(n-1)

# printN(5)


# # 2. Print 1 to n using recursion

# def print1toN(i,n):
#     if i>n:
#         return
#     print(i)
#     print1toN(i+1,n)

# print1toN(1,7)

# # 3. Print n to 1 using recursion

# print('n to 1 using recursion')


# def printnto1(i,n):
#     if i<n:
#         return
#     print(i)
#     printnto1(i-1,n)

# printnto1(7,1)


# # 4. Sum of n numbers

# print('sum of n numbers')

# n =5
# sm = 0
# for i in range(1,n+1):
#     sm = sm+i
#     print(sm)

# # Recursion approcach

# print('recursion approach')

# def sum(i,n,sm):
#     if i>n:
#         return sm
#     return sum(i+1,n,sm+i)

# ans = sum(1,7,0)
# print(ans)

# #  5. Factorial of a number

# print('factorial of a number')

# def fact(i,n,ans):
#     if i>n:
#         return ans
#     return fact(i+1,n,ans*i)

# a = fact(1,5,1)
# print(a)


# # DAY - 12


# # 1. Check whether a string is a palidrome or not by recursion 

# string = input()

# def ispal(s,e,string):
#     if s>e:
#         return True
#     if string[s]!=string[e]:
#         return False
#     return ispal(s+1,e-1,string)

# ans = ispal(0,len(string)-1,string)
# print(ans)


# # Fibonacci series
# print('Fibonacci seriers')
# n = int(input("Enter the number of terms: "))

# def print_fibonacci_series(n):
#     a, b = 0, 1
#     for i in range(n + 1): # +1 to include the nth term
#         print(f"Term {i}: {a}")
#         # Update a and b for the next iteration
#         a, b = b, a + b

# print_fibonacci_series(n)

# print('OR')

# print('Fibonacci seriers')

# n = int(input())

# def fib(n):
#     if n <=1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)

# ans = fib(n)
# print(ans)


# # HASHING: Count frequency of each element in an array

# arr = [10,5,15,10,7,5,14,15,10,2,2,3,5,8,7]
# print(arr)

# d = {}
# for item in arr:
#     d[item] = d.get(item,0) +1 # .get() method is used to retrieve the value of a specific key 
#                                # from a dictionary.

# print(d)

# # revesing a array

# l = list(map(int,input().split()))
# print('original list: ',l)

# n = len(l)
# for i in range(n//2):
#     l[i],l[n-1-i] = l[n-1-i],l[i]
# print('reverse list: ',l)


# # DAY - 13

# arr = [10,5,15,10,7,5,14,15,10,2,2,3,5,8,7]
# print(arr)

# d = {}
# for item in arr:
#     d[item] = d.get(item,0) +1

# # find max and min count

# mxcount = 0
# mxvalue = -1 # always take a small value

# mncount = 1000000000    # always take a large value
# mnvalue = -1


# for key,count in d.items():
#     if mxcount<count:
#         mxvalue = key
#         mxcount = count

#     if mncount>count:
#         mnvalue = key
#         mncount = count

# print('max count is:',mxcount,'max value is:',mxvalue)
# print('min count is:',mncount,'min value is:',mnvalue)


# # Sorting

# # 1. Selection sort 

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         findex = i
#         for j in range(i+1,n):
#             if arr[j]<arr[findex]:
#                 findex = j
#         arr[findex],arr[i] = arr[i],arr[findex]
#         return arr
    
# arr = [64, 25, 12, 22, 11]
# sorted_list = selection_sort(arr)
# print(sorted_list)


# # Bubble sort              

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
       
        
       
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 # Swap the elements
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
            
#     return arr

# # Example usage:
# test_list = [64, 34, 25, 12, 22, 11, 90]
# print(f"Sorted array: {bubble_sort(test_list)}")     


# # DAY - 14

# # Insertion Sort

# print('result of Insertion sort is')


# def insertionsort(arr):
#     n = len(arr)

#     for i in range(1,n):
#         j = i
#         while j>0 and arr[j]<arr[j-1]:
#             arr[j],arr[j-1] = arr[j-1],arr[j]
#             j -=1
#     return arr

# arr = [12,45,11,10,5,12,3,48,4]
# ans = insertionsort(arr)
# print(ans)


# # Merge sort

# print('result of merge sort is')


# def mergesort(arr, s, e):
#     if s >= e: # Base case: if the section has 1 or 0 elements, it's sorted
#         return

#     mid = (s + e) // 2
#     mergesort(arr, s, mid)
#     mergesort(arr, mid + 1, e)

#     # Create temporary copies of the sub-arrays
#     left = arr[s:mid+1]
#     right = arr[mid+1:e+1]

#     i, j, k = 0, 0, s

#     # Merge the two halves back together in order
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             arr[k] = left[i]
#             i += 1
#         else:
#             arr[k] = right[j]
#             j += 1
#         k += 1

#     # KEY FIX: Copy remaining elements of left[] if any
#     while i < len(left):
#         arr[k] = left[i]
#         i += 1
#         k += 1

#     # Copy remaining elements of right[] if any
#     while j < len(right):
#         arr[k] = right[j]
#         j += 1
#         k += 1

#     return arr

# arr = [12, 45, 7, 5,694, 12, 3, 53, 6, 487]
# # Note: Use len(arr)-1 to sort the entire list
# mergesort(arr, 0, len(arr) - 1) 
# print(arr)



# # Quick sort

# print('result of quick sort is')

# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1  # Index of smaller element
    
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
            
#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     return i + 1

# def quick_sort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
        
#         # Separately sort elements before and after partition
#         quick_sort(arr, low, pi - 1)
#         quick_sort(arr, pi + 1, high)

# # Example usage:
# data = [10, 7, 8, 9, 1, 5]
# quick_sort(data, 0, len(data) - 1)
# print(data)


# # Built in Python function for Sorting 

# arr = [8,5,6,4,74,5]

# arr.sort()
# print(arr)

# # or
# print('or')
# arr = [8,5,6,4,74,5] 

# arr1 = sorted(arr)

# print('orignal array',arr)
# print('sorted array',arr1)


# arr = [[4,5],[2,4],[1,2],[1,4],[6,7]]
# arr.sort()
# print(arr)


# # DAY - 15

# # ARRAYS

# # Largest element in an array 



# def find_largest(arr):
   
    
#     # Initialize max with the first element
#     max_val = arr[0]
    
#     for num in arr:
#         if num > max_val:
#             max_val = num
            
#     return max_val

# arr = [12,467,161,21,2,62,196,236]
# ans = find_largest(arr)
# print('largest element is:',ans)

# # Smallest element in an array 

# def find_smallest(arr):
   
    
#     # Initialize max with the first element
#     min_val = arr[0]
    
#     for num in arr:
#         if num < min_val:
#             min_val = num
            
#     return min_val

# arr = [12,467,161,21,2,62,196,236]
# ans = find_smallest(arr)
# print('smallest element is:',ans)



# # Finding second smallest in an array 

# def find_second_smallest(arr):
    

#     smallest = float('inf')
#     second_smallest = float('inf')

#     for num in arr:
#         if num < smallest:
#             second_smallest = smallest
#             smallest = num
#         elif num < second_smallest and num != smallest:
#             second_smallest = num

#     # Return None if no unique second smallest exists (e.g., [10, 10])
#     return second_smallest if second_smallest != float('inf') else None

# # Test
# arr = [12, 467, 161, 21, 2, 62, 196, 236]
# ans = find_second_smallest(arr)
# print('Second smallest element is:', ans)


# # Finding second smallest in an array 

# def find_second_largest(arr):
    

#     largest = -float('inf')
#     find_second_largest = -float('inf')

#     for num in arr:
#         if num > largest:
#             second_largest = largest 
#             largest = num
#         elif num > second_largest and num != largest:
#             second_largest = num

#     # Return None if no unique second smallest exists (e.g., [10, 10])
#     return second_largest if second_largest != -float('inf') else None

# # Test
# arr = [12, 467, 161, 21, 2, 62, 196, 236]
# ans = find_second_largest(arr)
# print('Second largest element is:', ans)


# DAY - 16

# Checking is the array sorted or not 

# Usig Iteration

arr = [1,2,3,4,5,6,7]

n = len(arr)

issort = True

for i in range(n-2):
    if arr[i]>arr[i+1]:
        issort = False
        break
print(issort)

# Time Complexity O(n)

# Using Recursion

def issort(arr):

    if len(arr) <= 1:
        return True 
    
    if arr[0] > arr[1]:
        return False
    
    return issort(arr[1:]) 


arr = [1,2,3,4,5,6,7,8]
ans = issort(arr)
print(ans)

# Time complexity O(n**2)



# Linear Search Using Recursion

def linear_search(arr, target, index):
    
    if index >= len(arr):
        return -1   # If elememnt not found in array 
    

    if arr[index] == target:
        return index  # if target is the first index
    
    return linear_search(arr, target, index + 1) # when we have to find in array


data = [10, 50, 30, 70, 80]
result = linear_search(data, 20,0)

if result != -1:
    print(result)
else:
    print("Item not found.")


 