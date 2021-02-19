print("숫자 2개 출력 : %d, %d" %(5,3))

a="hobby"
print(a.count('b'))
# b 개수 세기

print(a.find('b'))
# b가 처음 나온 위치 반환, 존재하지 않으면 -1반환

print(a.index('b'))
# b가 처음 나온 위치 반환, 존재하지 않으면 에러

c=','
print(c.join('abcd'))
#abcd에 ,를 사이마다 넣기 a,b,c,d

print(a.upper())
d="HELLO"
print(d.lower())

e="  hello  "
print(e.lstrip())
# 왼쪽 공백 제거
print(e.rstrip())
# 오른쪽 공백 제거
print(e.strip())
# 양쪽 공백 제거

f=a.replace("obby","ello")
#replace(바꾸고싶은거,바꾼뒤)
print(f)

g="hello world !!!"
h=g.split()
#문자열 나누기 , 비워두면 공백 기준 자르기
print(h)

i="a,b,c,d"
j=i.split(',')
print(j)


number=10
day="three"
print("I ate {0} apples. so I was sick for {1} days".format(number,day))
print("I ate {num1} oranges and {num2} apples".format(num1=3,num2=5))
# 문자열 사이에 숫자와 문자열 대입하기


print("{0:=^10}".format("hi"))
#====hi====
#hi========는 ^대신 <
#========hi는 ^대신 >
#=비워두면 공백으로 채움


print("{{abc}}".format())
#{}를 문자로 포함

print(str(123)+"hi")
#숫자랑 문자열을 그냥 더하면 에러남. 문자열로 바꿔서 더한다
