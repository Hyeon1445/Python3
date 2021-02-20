def sum(a,b):
    return a+b


print(sum(3,5))
#8


def sum_all(*nums):
    sum=0
    for i in nums:
        sum+=i
    print(sum)

sum_all(1,2,3,4,5,6)
#21
#return 없을 수 있음
#입력 개수 모를때 *변수명
#입력값들을 튜플로 만들어줌!
# def sum_all(a,*nums) 이런식으로도 가능

def sum_and_mul(a,b):
    return a+b, a*b
print(sum_and_mul(1,5))
#반환 여러개면 튜플로 반환(6,5)

c,d=sum_and_mul(3,5)
print(c)
#8

#def say(a,b,c=TRUE):
#c에 입력 없으면 무조건 true
#초기 입력인 c는 무조건 맨뒤


#global a
#전역변수
# global보다는 return이 낫다

