person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left." % (person,coins) # %s method
print(message)

message = "\n{} has {} coins left.".format(person,coins) # .format + {} method
print(message)

message = "\n{1} has {0} coins left.".format(coins,person)
print(message)

message = "\n{person} has {coins} coins left.".format(
    coins=coins,person=person
    )
print(message)

player = {'person': 'Dave','coins': 3}

message = "\n{person} has {coins} coins left.".format(**player) # Dictionary method
print(message)

###################
# F-strings!  This is the way.

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2*5} coins left."
print(message)

message = f"\n{person.lower()} has {2*5} coins left."
print(message)

message = f"\n{player['person']} has {2*5} coins left."
print(message)

###################
# You can pass formatting options

num = 10
print(f"\n2.25 times {num} is {2.25*num:.2f}")

for num in range(1,11):
    print(f"\n2.25 times {num} is {2.25*num:.2f}")

for num in range(1,11):
    print(f"\n{num} divided by 4.52 is {num/4.52:.2%}")