#심볼 테이블 내용 확인

g_a = 1
g_s = '마이콜'


def g_f():
    l_a = 2
    print(g_a)
    g_a = 3
    l_s = '둘리'
    print(locals())


print(globals())
g_f()


print(g_a)
# error : local 테이블은