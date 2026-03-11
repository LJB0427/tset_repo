import random

i = 0
n = 20
print("[%d자리의 랜덤 숫자 뽑기]" %n)       #연속되지 않는

num1 = random.randrange(1,10)
print("%d" %num1, end='')

while i < n:
    num2 = random.randrange(1,10)
    if num1 == num2:
        num2 = random.randrange(1,10)
    else:
        print("%d" %num2, end='')
        num1 = num2
        i += 1
print("")