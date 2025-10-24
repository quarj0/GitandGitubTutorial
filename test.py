# fibonacci number generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
        
# test case 
def test_fibonacci():
    assert list(fibonacci(0)) == []
    assert list(fibonacci(1)) == [0]
    assert list(fibonacci(2)) == [0, 1]
    assert list(fibonacci(5)) == [0, 1, 1, 2, 3]
    assert list(fibonacci(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    
if __name__ == "__main__":
    test_fibonacci()
    print("All tests passed.")
    
# Run the test cases to verify the correctness of the fibonacci function
test_fibonacci()
if __name__ == "_main_":
    n = 10
    print(f"First {n} Fibonacci numbers:")
    for num in fibonacci(n):
        print(num, end=' ')
        print()
