def trace(x):
    if x%2 == 0:
        return x/2
    else:
        return (3*x)+1

def branch(x):
    if x%2 == 0:
        if (x-1)%3 == 0:
            num = (x-1)%3
    else:
        num = 0
    return [x*2 , num]

def col(x):
    while x > 1:
        x = trace(x)
        return x

def grow(x):
    step = branch(x)
    for i in step:
        if i == 0:
            continue
        else:
            branch(i)

print(col(43))
