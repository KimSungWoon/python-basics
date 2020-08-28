#zip() 사용 예
# for 한번 하면 다음 시퀀스는 돌지 않음

seq1 = {'foo','bat','baz'}
seq2 = {'one','two','three'}

z = zip(seq1,seq2)
print(z,type(z))

for t in z:
    print(t)

z = zip(seq1,seq2)
for index, t in enumerate(z):
    print(index, t)

z = zip(seq1,seq2)
for (a,b) in z:
    print(a,b)