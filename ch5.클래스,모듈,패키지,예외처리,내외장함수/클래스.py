class Simple:
    pass
#아무것도 없음

class service:
    a="hello"
    def sum(self,b,c):
        result=b+c
        print("%s+%s=%s입니다" %(b,c,result))

m=service()
m.sum(3,5)



class service2:
    a="hello"
    def setname(self,name):
        self.name=name
    def sum(self,b,c):
        result=b+c
        print("%s님 %s+%s=%s입니다"%(self.name,b,c,result))
    
n=service2()
n.setname("lee")
n.sum(3,5)
#이름 입력 안하면 더하기 에러남


class service3:
    a="hello"
    def __init__(self,name):
        self.name=name
    def sum(self,b,c):
        result=b+c
        print("%s님 %s+%s=%s입니다"%(self.name,b,c,result))
l=service3("lee")
l.sum(4,8)
#처음에 이름 넣어야함!!


class FourCal():
    def setdata(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def sub(self):
        return self.a-self.b
    def div(self):
        return self.a/self.b
aa=FourCal()
aa.setdata(5,2)
print(aa.sum())
print(aa.mul())
print(aa.sub())
print(aa.div())


class HousePark:
    lastname="박"
    def setname(self,name):
        self.name=name
        self.fullname=self.lastname+name
    def travel(self,tr):
        print(self.lastname+self.name+tr+"여행을 가다")
    

pp=HousePark()
pp.setname("응용")
print(pp.lastname)
print(pp.fullname)
pp.travel("부산")




class HouseKim(HousePark):
    lastname="김"
#클래스 상속
#괄호 안에 넣어주면 HousePark에 있는 함수 그대로 실행됨
#함수 다르게 실행하려면 같은 이름으로 다른 내용으로 쓰면 됨

pp.setname("ㅇㅇ")
print(pp.fullname)

class ParkFriends:
    lastname="박"
    def __init__(self,name):
        self.fullname=self.lastname+name
    def travel(self,where):
        print(self.fullname+", "+where+"여행을 가다")
    def __add__(self,other):
        print(self.fullname+", "+other.fullname+"는 친구이다")

class KimFriends(ParkFriends):
    lastname="김"

pf=ParkFriends("응용")
pf.travel("서울")
pf2=KimFriends("가가")
pf+pf2
#박응용, 김가가는 친구이다 출력
#연산자 이용
#연산자 오버로딩

