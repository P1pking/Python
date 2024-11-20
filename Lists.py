users = ['Dave','John','Sara']

data = ['Dave', 42, True]

emptylist = []

#check if item is in list
print("Dave" in emptylist)

print(users[0])
print(users[-2])

print(users.index('Sara'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

#add name/item to list
users.append('Elsa')
print(users)

users += ['Jason']
print(users)

users.extend(['Robert','Jimmy'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Bob')
print(users)

users[2:2] = ['Eddie','Alex']
print(users)

users[1:3] = ['Robert','JPJ']
print(users)

users.remove('Bob')
print(users)

#"pop" and return last item in list
print(users.pop())
print(users)

#delete item(s) or entire list
del users[0]
print(users)

#del data
data.clear()
print(data)

users[1:2] = ['dave']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4,42,78,1,5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(nums)
mycopy.sort()
print(mycopy)
print(nums)

#what type?
print(type(nums))

mylist = list([1,"Neil", True])
print(mylist)


#Tuples
#tuples cannot be changed, but can be copied/duplicated
mytuple = tuple(('Dave','42',True))

anothertuple = (1,4,2,8,2,2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one,*two,hey) = anothertuple
print(one)
print(two)
print(hey)

#count occurunce of item
print(anothertuple.count(2))