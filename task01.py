number = int(input("Введите целое число >= 2: "))

fib1 = 0
fib2 = 1
fib_sum = 0
index = 2

while number >= fib_sum:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    index +=1

if fib1 == number:
    print(index-1)
else: print(-1)