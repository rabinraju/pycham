n = 5


def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)


print("the factorial is:",fact(n))


s = 4

def factorial(s):
    if s == 1:
        return s
    else:
        return s * factorial(s - 1)
print("the factorial is:",factorial(s))