# 생성

t = () #공 튜플
t = (1 ,) #항목이 하나인 튜픙을 생성할 때는 반드시 코마를 사용한다.

t = (1, 2, 3)

print(t, type(t))

print("================ 시퀀스 타입 특징=================")
#인덱싱(시퀀스 타입)
print(t[-2], t[-1], t[0], t[1], t[2])

#slicing(시퀀스 타입 특징)
print(t[1:3])
print(t[:])

#반복

t2 = t*2
print(t2)

#연결

t3 = t +(4,5,6)
print(t3)

#길이
print(len(t3))

# in, not in
print(4 in t3)
print(7 not in t3)

#튜플은 변경 불가
try:
    t4 =('apple','banana', 10 ,20)
    t4[2] = 90
except TypeError as e:
    print('튜플은 변결 불가 - 불멸성')

#튜플을 이용한 여러 값의 대입

x, y, z = 10, 20, 30
print(x, y, z)

#튜플 이용해 여러 값 치환

x, y = 10, 20
x, y = y, x
print(x, y)

print('===============객체함수 =====================')
t5 = (20,30,40,50,20)
print(t5.index(50))
print(t5.count(20))

# 변환 : tuple => set
s = set(t5)
print(t5)

#변환 : tuple => list
L = list(t5)
L.insert(0,10)
print(L, type(L))

t5 = tuple(L)
print(t5)

t5 = tuple(set(t5))

