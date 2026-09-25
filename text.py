numbers = []

for i in range(8):
    n = int(input("Enter a number: "))
    numbers.append(n)

largest = numbers[0]
second = numbers[0]

for n in numbers:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print("Second largest:", second)