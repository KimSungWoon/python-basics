#
def sum(*args):
    return args =


#가변 사용해라
print(sum())
print(sum(1,2))
print(sum(1,2,5,7,2,3))

def _print(*args, sep=' ', end='\n'):
    for c in args:
        print(c, end='')
        print(sep, end='')

    print(end, end='')