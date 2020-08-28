# a = 23
# a = 20 + 3
#
# print(a, type(a))
# print(isinstance(a, int))
#
# # 2진수, 10진수, 8진수. 16진수
# b = 0b1101
# c = 0o23
# d = 0x23
# print(b)
# print(c)
# print(d)
#
#
# # 3.x에서는 int, long 합쳐졌다. 따라서 표현범위가 무한대이다.
#
# e = 2**1024
#
# print(e, type(e))
# print(e.bit_length())
#
# #변환함수
# print(bin(38))
# print(oct(38))
# print(hex(38))
#
# # 생성
# l1 = []
# l2 = [1, True, "ptthon", 3.14]
#
# #
# # 인덱싱(sequence 타입 특징)
# print(l2[0], l2[1],l2[2], l2[3])
# print(l2[-4], l2[-3], l2[-2], l2[-1])
#
# print(l2[1:4])
# print(l2[:])
# print(l2[2:])
# print(l2[3:0:-1])
# print(l2[len(l2)::-1])
#
# # 반복(씨퀀스 특징)
# l3 = l2 * 2
# print(l3)
#
# # 연결(씨퀀스 특징)
# l4 = [1, 2, 3]
# print(l4)
#
# #길이 (씨퀀스 특징)
# print(len(l4))
#
# #in,not in(씨퀀스 타입 특징)
# print(5 not in l4)
# print('python' in l4)
#
# #삭제(변경 가능한 객체)
# del l4[2]
# print(l4)
#
# #변경 가능한 객체
# l5 = [1,2,3,4]
# l5[3] = l5[3] +10
# print(l5)
#
# # 삭제(slicing을 이용한...)
# l6 = [1,12,123,1234]
# l6[1:2] = []
# print(l6)
#
#
# # 삽입(slicing을 이용한...)
# l7 = [1,12,123,1234,12345]
# l7[1:1] = [12]
# print(l7)
#
# # 마지막 삽입
# l7[5:] =[123456 , 1234567]
# print(l7)
#
# # 처음 삽입
# l7[:0] = [-123,-12,-1,0]
# print(l7)
#
# # 치환(slicing을 이용한...)
# l8 = [1,12,123,1234,12345]
# l8[0:2] = [10,20]
# print(l8)
#
# l8[0:2] = [100]
# print(l8)
#
# l8[1:2] = [200]
# print(l8)
#
# l8[2:4] = [300,400,500,600]
# print(l8)
#
# print('================객체함수===============')
# l9 = [1, 3, 4]
#
# # 중간삽입
# l9.insert(1,2)
# print(l9)
#
# # 마지막 삽입
# l9.append([5,6])
# print(l9)
#
# # 처음 삽입
# l9.insert(0,0)
# print(l9)
#
# # reverce
# l9.reverse()
# print(l9)
#
# #삭제(값으로 삭제 동질한 객체를 삭제 한다.==)
# l9.remove(4)
# print(l9)
#
# # 없는 객체 삭제할 경우
# try:
#     l9.remove(3)
# except ValueError as e:
#     print('없는 객체 삭제할 경우 예외 발생')

# # 확장
# l9.extend([-1, -2, -3])
# print(l9)

# stack v = s[len(s)]
s = []
s.append(10) # push
s.append(20) # push
s.append(30) # push
print(s)
print(s.pop())
print(s.pop())
print(s)

# queue로 사용하기
q = [1,2]
q.append(3)
q.append(4)
q.append(5)

print(q)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))
print(q)

#  sort
l10 = [1,5,3,9,8,11]
l10.sort()
print(l10)

l11 = ['10', 2, '33', 9, '8', 4, 11]
l11.sort(key=str)
print(l11)

l11.sort(key=int)
print(l11)

#cf : sorted 전역 함수 정렬할 수 있는 알고리즘 삽입 가능.

l12 = [19,46,37,28,91,55,64]
l13 = sorted(l12)
print(l13)

def f(i):
    return i / 10

l14 = sorted(l12, key=f, reverse = 0)
print(l14)