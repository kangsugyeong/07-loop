i = 0
while i < 10:
    i = i + 1
    print("*"*i)

# for i in range(1,11):
#     print("*"*i)

numbers_1 = []
numbers_2 = []
numbers_3 = []
for i in range(1,101):
    if i % 2 == 0:
        numbers_1.append(i)
    if i % 3 == 0:
        numbers_2.append(i)
    if i % 5 == 0:
        numbers_3.append(i)

print(numbers_1)
print(numbers_2)
print(numbers_3)

import random

random.randint(1,45)
i = 0
result = []
while i < 6:
    i = i + 1
    new_num = random.randint(1,45)
    if new_num in result

    result.append(random.randint(1,45))
print(result)


