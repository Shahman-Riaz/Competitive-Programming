def factorial(n):
    # Write your code here
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n * factorial(n - 1)

n = int(input().strip())
print(factorial(n))