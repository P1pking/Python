

name = "Dave"
count = 1

def another():
    color = "blue"
    global count # calling "global" variable
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Dave")


another()
# important not to polute the "global scope" which is why it is important to try to put a lot of things in functions