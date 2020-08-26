#helloworld.py

# 블록 시작(전역범위)
print('hello world')
a = 2
if a < 1:# 블록 시작(조건문)
    b = 1
    print(a)
    print('big')           # 블록 끝




def my_func(i):
    print('새블록 시작(함수정의)')
    if i > 10:
        print('블록시작 (조건문)')
    print('big')
    print('....')
    print('블록 끝(함수정의)')

#함수 호출
my_func(20)