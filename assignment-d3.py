#q1lambda
q1 = lambda x, y ,z : max (x,y,z)
print(q1(1,2,3))
#  q2:fibonacci seq:
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main(n):
    return [fibonacci(i) for i in range(n)]

# Generate the first 10 Fibonacci numbers
x = main(10)
print(x)

