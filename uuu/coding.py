name = input()
print('My name is',name)
print('hello')


# directly printing in output.txt
print("hello")


# taking input from input.txt and printing it in output.txt
name = input()
age = int(input())
salary = float(input())
isadmin = bool(input())


print(name,type(name))
print(age,type(age))
print(salary,type(salary))
print(isadmin,type(isadmin))

#taking 3 space seprated integer value as integer
a,b,c = map(int,input().split())
print(a,b,c)

# taking multiple integer inputs
lst = list(map(int,input().split()))
print(lst)