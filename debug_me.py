

def inner():
    print("Start inner")
    count = 1
    for i in range(3):
        count = count * i
    return count


def outer():
    print("Start outer")
    value = inner()
    print(value)


print("==Start==")
outer()

# before you ask, no this code has no bug ;)
