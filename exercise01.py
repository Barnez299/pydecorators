from decorator_template import timer


@timer
def waste_time(number):
    total = 0
    for num in range(number):
        total += sum(n for n in range(num))
    return total

print(waste_time(10))
print(waste_time(1000))
print(waste_time(10000))