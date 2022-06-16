def ultimate(power):
    def supreme(func):
        def inner(list):
            return [func(val[0], val[1])**power for val in list]
        return inner
    return supreme

@ultimate(2)
def add(x,y):
    return x+y

print(add([(1, 3), (3, 17), (5, 5), (6, 7)]))
