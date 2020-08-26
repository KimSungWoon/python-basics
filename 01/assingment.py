# 치환 문자

a = 1
b = a + 1
print(a, b)

# 변수 할당값 오류
# 1 + a = c

# 세미 콜론으로 치환 문을 구분할 수 있다.
e = 3.5 ; f= 5.3
print(e,f)

# 여러 개를 한번에 치환할 수 있다.
e, f = 3.8 , 8.3
print(e,f)

# 같은 값을 여러 변수에 할당할 수 있다.
x = 30
y = 30
x = y = z = 30

# 동적 타이핑(실행중에 변수의 타입을 결정한다.)
a = 1
print(type(a))
a = 'hello'
print(type(a))
a = 3.14
print(type(a))
a = True
print(type(a))

# 확장 치환문
a = 10
# a = a + 10
a += 10
a -= 10
print(a)

# swap
x = 10
y = 20
print('=====before swap =====')
print(x, y)

#
# 코드를 짜서
#
print('=====after swap =====')

print(x, y)