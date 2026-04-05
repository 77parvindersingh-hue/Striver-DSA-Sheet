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
l = [1,2,3,4]
print(l)

# adding an element in a list
# append only add an element in the last
l.append(66)
print(l)
# but if we want to add in middle
l.insert(1,11)
print(l)
# to delete an element
l.pop(4) # 4 is the index 
print(l)
l.pop(1)
print(l)
# updating a lst 
l[2] = 12
print(l) #see in output.txt 3 is replaced by 12
# getting an element from the list
print(l[1]) # put the index of the element u want


# Tuples

n = (4,5,71,96748,6566)
print(n)
print(type(n))
# getting any data from a tuple
print(n[4]) # 4 is index here



# Dictionary

d = {'orange':5,'apple':4,'mango':12,'grapes':7}
print(d)
print(type(d))

# getting a data from a list
print(d['apple']) # here apple is the key

# adding an element 
d['banana'] = 8
print(d)

# updating a element in dict
d['orange'] = 13
print(d)

#remove an element from dict
del d['apple'] # the key and value of apple will be deleted
print(d)

# SET

s = {1,2,3,7,5,68,26,6,5}
print(s,type(s))

# adding element in set
# set always hold unique value
s.add(12)
s.add(7)
s.add(1)
#only 12 will be added as 7 and 1 are already present in the set 
print(s)

# getting a value in set
# it awlways give in true and false
# if value will be present it will give true 
print(14 in s) # false as 14 is not in set
print(1 in s)

# removing an element 
print(s.remove(1))
print(s)