# 1~ 20 합을 구하기

s = 0
count = 0
while count < 10:
    print(count)
    s += (count+1)
    count += 1

print(s)


#break

for n in range(10):
    if n > 5:
        break
    print(n , end = '')


i = 0
while i < 10:
    if i > 5:
        break
    print(i, end = '')
    i += 1
print("\n----------------------------------------")

# continue


i = 0
while i < 10:
    if i <=5:
        i += 1
        continue
    print(i, end='')
    i += 1
print('\n===============================')

# 무한루프
i = 0
while True:
    print(i, end='')
    if i > 5:
        break
    i += 1