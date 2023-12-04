
# define a function to find the nth Fibonacci number using recursion
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
num_index = int(input("Enter the index of the Fibonacci number to find: "))
print(fibonacci(num_index))

