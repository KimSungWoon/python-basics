# packing 은 tuple로만 가능하다.

t = 10, 20 , 30, 'python'
print(t,type)

#unpacking
a, b, c, d = t
print(a, b, c, d)

# 오류 : 패킹 되어있는 객체가 더 많은 경우
# x, y, z = t

# 패킹 되어있는 객체가 더 적은 경우
# l,m,n,o,p = t

#unpaking 확장
t2 = (1,2,3,4,5)
a, *b = t2
print(a,b)

*a, b = t2
print(a,b)

a, *b, c = t2
print(a,b)
a, b, *c = t2
print(a,b)
