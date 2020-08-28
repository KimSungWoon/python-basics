

# 문제3. 다음과 같은 출력이 되도록 이중 for~in 문을 사용한 코드를 작성하세요.
print('\n------------구구단1---------------')
for i in range(1, 10):
    for j in range(1,10):
        print('%d X %d = %d'%(i,j ,i*j))

print('\n------------구구단2---------------')
for i in range(1, 10):
    for j in range(1,10):
        print('{0} X {1} = {2}'.format(i,j,i*j), end='\t')
    else:
        print('')

print('\n------------삼각형1-------------')
for i in range(10):
    for j in range(0, i+1):
        print("*", end = '')
    else:
        print('')

print('\n------------삼각형2-------------')
for i in range(10):
    print("*"*(i+1))

print('\n------------역삼각형2-------------')
for i in range(10,0,-1):
    print("*"*i)

