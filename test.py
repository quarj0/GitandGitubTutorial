# fibonacci number generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
        
if __name__ == "_main_":
    n = 10
    print(f"First {n} Fibonacci numbers:")
    for num in fibonacci(n):
        print(num, end=' ')
        print()