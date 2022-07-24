def fizzBuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 != 0:
            i = "Fizz"
        elif i % 15 == 0:
            i = "FizzBuzz"
        elif i % 5 == 0 and i % 3 != 0:
            i = "Buzz"
        elif i % 3 != 0 and i % 5 != 0:
            i = i
        print(i)

n = int(input().strip())
fizzBuzz(n)