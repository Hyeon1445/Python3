print(abs(-3))
#3
#절대값

print(all([1,2,3]))
#True
print(all([0,1,2]))
#False
#하나라도 거짓이면 false

print(any([0,1,2,3,4]))
#True
#하나라도 참이면 True
print(any([0,""]))
#False

print(chr(97))
#아스키코드에 해당하는 문자 출력 'a'
print(ord('a'))
#아스키코드 리턴 97

print(dir([1,2,3]))
print()
print(dir({'1':'a'}))
#dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌
#여기에서는 리스트와 딕셔너리 객체 관련 함수들(메서드)를 보여줌

print(divmod(7,3))
# 몫과 나머지를 튜플 형태로 리턴, 소수도 가능
#(2,1)
print(divmod(1.3,0.2))
#(6.0,0.0999999999999999998)

for i,name in enumerate(['aaa','bbb','ccc']):
    print(i,name)
#순서가 있는 자료형 ( 리스트, 튜플, 문자열 )을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴


print(eval('1+2+3'))
#6
print(eval("'hi'+'aaa'"))
#hiaaa
print(eval('divmod(4,3)'))
#(1,1)
#실행 가능한 문자열을 입력으로 받아 결과값 리턴



def positive(x):
    return x>0

print(list(filter(positive,[1,3,-2,5,-8,7,9,-100])))
#정의된 함수를 기준으로 걸러줌
#여기서는 양수값만 반환
#[1,3,5,7,9]

print(hex(234))
#정수값을 16진수로
#0xea

print(oct(34))
#정수값을 8진수로
#0o42


a=100
print(id(100))
print(id(a))
b=a
print(id(b))
#100,a,b의 주소값은 같다
#객체의 고유 주소값(레퍼런스) 리턴


inp=input()
#값 입력받기
inp=input("입력 : ")

print(int('3'))
print(int(3.14))
#3
#정수리턴
print(int('111',2))
#int(x,radix) radix진수로 표현된 x값을 10진수로 변환
#7
print(int('1A',16))
#26



class person:
    pass

aaa=person()
print(isinstance(aaa,person))
#aaa가 person 클래스에 의해서 생성된 인서턴스임을 확인
#True

add=lambda a,b:a+b
print(add(5,8))
#13
#def보다 간결하게 함수 만든다

ccc="hello world!!!"
print(len(ccc))
#길이 반환
#14

print(list("hello"))
#['h','e','l','l','o']


def two_times(x):
    return x*2

print(list(map(two_times,[1,2,3,4,5])))
#[2,4,6,8,10]
#반복 가능한 자료형을 입력으로 받는다
#수행된 결과를 반환

print(max([1,2,3,4,5]))
#5
print(max("python"))
#'y'
#min도 똑같이 씀


#fread=open("read_mode.txt",'r')
#r읽기
#w쓰기
#a추가
#b바이너리 모드로 파일 열기 r,w,a와 함께 씀 (rb,wb,ab)


print(pow(2,4))
#16
#2^4
print(2**4)
#2^4


print(list(range(5)))
#[0,1,2,3,4]
print(list(range(5,10)))
#[5,6,7,8,9]
print(list(range(1,10,2)))
#[1,3,5,7,9]
print(list(range(0,-10,-2)))
#[0,-2,-4,-6,-8]

k=[5,8,7,2,6]
k.sort()
print(k)
#2,5,6,7,8
#반환값은 따로 없고
#sort는 리스트 자체를 정렬해서 다시 저장함
m=[4,8,6,3,7]
sorted(m)
print(m)
print(sorted(m))
#3,4,6,7,8
#sorted는 반환값이 있고
#정렬되어 저장되지는 않는다

print(str(123))
#문자열 형태로 객체 반환

print(tuple("abc"))
#('a','b','c')

print(type([]))
#출력값 <class 'list'>
#자료형을 알려줌

print(list(zip([1,2,3],[4,5,6])))
#[(1,4),(2,5),(3,6)]
print(list(zip([1,2,3],[4,5,6],[7,8,9])))
#[(1,4,7),(2,5,8),(3,6,9)]
#동일한 개수로 이루어진 자료형을 묶어준다
