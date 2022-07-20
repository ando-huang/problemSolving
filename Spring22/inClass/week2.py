def foo(x):
    return x * x

def bar(x, y):
    if y == 1:
        return x % 2 == 0
    return abs(x)

# print(bar(1, 1))
# print(bar(2, 2))

x = 0
def foo(x):
	x += 1
	return x
print(x) # print statement 1
foo(x)
print(x) # print statement 2
