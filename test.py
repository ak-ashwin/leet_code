import time

start_time = time.time()

numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = []
squared_odd_numbers = []
total = 0  # filter for odd numbers
for number in numbers:
    if number % 2 == 1:
        odd_numbers.append(number)  # square all odd numbers
for number in odd_numbers:
    squared_odd_numbers.append(number * number)  # calculate total
for number in squared_odd_numbers:
    total += number  # calculate average

print(total)
print("--- %s seconds ---" % (time.time() - start_time))

from functools import reduce

start_time = time.time()

numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = filter(lambda n: n % 2 == 1, numbers)
squared_odd_numbers = map(lambda n: n * n, odd_numbers)
total = reduce(lambda acc, n: acc + n, squared_odd_numbers)
print(total)

print("--- %s seconds ---" % (time.time() - start_time))
