#Boolean

print(True)
type(True)

my_str = "Sree"
my_str.isalnum()
print(my_str.isalnum())
my_str.isalpha()
print(my_str.isalpha())
my_str.isdecimal()
print(my_str.isdecimal())

print("------")
print(True and True)
print(True or False)
print(True and False)
print(False or False)
print(True or True)

print("----")

str = "Sree"
exam = "Hello"

print(str.isalpha() or exam.isdecimal())
print(str.isdecimal() and exam.isalnum())


print("------#List")
print(type([]))

lst = ['Sree', 'Ram', 2,0,0,4]
print(type(lst))
##indexing
print(lst[2])

##appending
lst.append("Programmer")
print(lst)

##insert
lst.insert(2, 'Hello')
print(lst)

##extend
lst.extend([21, 11])
print(lst)

##Sum
lst = [1,2,3,4,5]
print(sum(lst))

#SETS
## No duplicate content

set_s = set()
print(type(set_s))

set = {1,2,3,4,5,3}
print(set)
set.add("Me")
print(set)
