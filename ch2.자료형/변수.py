a,b=('aaa','bbb')
(c,d)=('ccc','ddd')
[e,f]=['eee','fff']
g=h='ggg'


b,c=c,b
print(c)
# 바꾸기
# c='bbb'
# b='ccc'

del(c)
#메모리에 생성된 변수 없애기'

m=[1,2,3]
n=m
m[1]=4
print(n)
#n도 같이 바뀜
#[1,4,3]
print(m is n)
#True 동일한 객체

x=[1,2,3]
y=x[:]
# y=copy(x)와 같다!
x[1]=4
print(x)
print(y)
#[:] 이용해서 복사함
#x=[1,4,3]
#y=[1,2,3]
print(x is y)
#False 다른 객체

