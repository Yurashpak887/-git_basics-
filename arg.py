
l = [5,3]
def avg(*args):

    return sum(args) / len(args)

print(avg(5,2))
print(avg(*l))
