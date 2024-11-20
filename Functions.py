def hello_world():
    print("Hello world!")

# ctrl d
hello_world()


def sum(num1=0,num2=0):
    if(type(num1) is not int or type(num2) is not int):
        return 0
    return num1+num2


total = sum(7,2)
print(total)
# * makes data inside function a tuple
def multiple_items(*args):
    print(args)
    print(type(args))



multiple_items("Dave","John","Sara")
# kwargs = key word arguments
def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))



mult_named_items(first="Dave", last="Gray")