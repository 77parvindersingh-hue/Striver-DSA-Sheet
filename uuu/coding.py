# name = input()
# print('My name is',name)
# print('hello')


# # directly printing in output.txt
# print("hello")


# # taking input from input.txt and printing it in output.txt
# name = input()
# age = int(input())
# salary = float(input())
# isadmin = bool(input())


# print(name,type(name))
# print(age,type(age))
# print(salary,type(salary))
# print(isadmin,type(isadmin))

# #taking 3 space seprated integer value as integer
# a,b,c = map(int,input().split())
# print(a,b,c)

# # taking multiple integer inputs
# lst = list(map(int,input().split()))
# print(lst)

# DAY-3

# working on a list
# l = [1,2,3,4]
# print(l)

# # adding an element in a list
# # append only add an element in the last
# l.append(66)
# print(l)
# # but if we want to add in middle
# l.insert(1,11)
# print(l)
# # to delete an element
# l.pop(4) # 4 is the index 
# print(l)
# l.pop(1)
# print(l)
# # updating a lst 
# l[2] = 12
# print(l) #see in output.txt 3 is replaced by 12
# # getting an element from the list
# print(l[1]) # put the index of the element u want


# # Tuples

# n = (4,5,71,96748,6566)
# print(n)
# print(type(n))
# # getting any data from a tuple
# print(n[4]) # 4 is index here



# # Dictionary

# d = {'orange':5,'apple':4,'mango':12,'grapes':7}
# print(d)
# print(type(d))

# # getting a data from a list
# print(d['apple']) # here apple is the key

# # adding an element 
# d['banana'] = 8
# print(d)

# # updating a element in dict
# d['orange'] = 13
# print(d)

# #remove an element from dict
# del d['apple'] # the key and value of apple will be deleted
# print(d)

# # SET

# s = {1,2,3,7,5,68,26,6,5}
# print(s,type(s))

# # adding element in set
# # set always hold unique value
# s.add(12)
# s.add(7)
# s.add(1)
# #only 12 will be added as 7 and 1 are already present in the set 
# print(s)

# # getting a value in set
# # it awlways give in true and false
# # if value will be present it will give true 
# print(14 in s) # false as 14 is not in set
# print(1 in s)

# # removing an element 
# print(s.remove(1))
# print(s)


# #DAY-4

# # Mutable - Something that can be changed
# # eg - List, Dictionary, Set, etc.
# # Immutable - something that can't be changed
# # eg- int, float, bool, string, tuple, etc.

# x = 7
# print(x)


# x = 5
# print(x)
# # since I said int is immutable but I am getting a updated value when
# # I print it. So, the logic behind it is that its id are different 

# x = 5
# print(id(x))

# x = 7
# print(id(x))


# # Data Conversion 

# a = 4.5
# print(a,type(a))

# b = int(a)
# print(b,type(b))

# c = str(a)
# print(c,type(c))

# l = [1,2,3,4,5,6]
# print(type(l))

# s = set(l)
# print(type(s))

# t = tuple(l)
# print(t,type(t))

# # converting into a dict

# colour = ['orange','red','brown','blue']
# qty = [15,45,21,54,46]

# d = dict(zip(colour,qty)) #we use zip function for dict.
# print(d,type(d))

# print(bool([]),bool({}),bool(()),bool(0),bool(0.0),bool(""))
# # it will give false

# print(bool([1,2]),bool({1,2}),bool((1,2)),bool(5),bool(0.2),bool("a"))


# # use of converting in real life
# # eg - u want to a list of unique elements from a mixed list 
# lst = [1,6,4,2,26,74,5,6,45,25,1,2,3,4,5,6,7,5,6,1]

# s = list(set(lst))
# print(s) # a list of unique elements


# DAY-5

# Slicing - helps us to extract data from a list or a string

name = 'Sanjay Bisht'
print(name[0:12])
print(name[0:12:1])
#syntax = print(name[str.index:end index : step])
print(name[0::2])
print(name[0:]) # by default it will take step=1 and end index will
                # be 12
print(name[-1::-1])
print(name[-1:-12:-2])
print(name[0:5]) #it always print -1 end index  value

# same u can apply for a list

# ques- prove list is mutable
l = [1,2,3,4]
print(l,id(l))
l.append(5)
print(l,id(l))
# since the id of list is same therefore list is mutable

# Condiional Statement 

# If-Else 
target = 125
runs = 120
if runs>target:
    print('we won')
else:
    print('we lost')

# If-Elif
marks = int(input(''))
if marks>=90:
    print('A')
elif marks>=75:
    print('B')
elif marks>=60:
    print('C')
elif marks>=33:
    print('D')
else:
    print("FAIL")