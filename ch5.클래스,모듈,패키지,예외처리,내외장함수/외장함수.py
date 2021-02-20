import sys

#print(sys.argv)
#cmd창에서 python 외장함수.py you need python 치면 ['외장함수.py','you','need','python']출력


#sys.exit()
#스크립트 강제종료


print(sys.path)
#파이썬 모듈둘이 저장되어 있는 위치 나타낸다
#맨 처음꺼가 현재 디렉터리



#sys.path.append("C:/python/modules")
#모듈의 경로 추가하기


import pickle
f=open("test.txt",'wb')
data={1:'python',2:'you need'}
pickle.dump(data,f)
f.close()
#pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
#dump 함수를 이용하여 딕셔너리 개체인 data를 그대로 파일에 저장

f=open('test.txt','rb')
data1=pickle.load(f)
print(data1)
#{1:'python',2:'you need'}
#pickle.dump에 의해 저장된 파일을 pickle.load를 이용해서 원래 있떤 딕셔너리 객체 상태 그대로 불러온다


import os
print(os.environ)
#내 시스템의 환경 변수값 알기

print(os.environ['PATH'])
#PATH환경 변수

#os.chdir("C:\WINDOWS")
#디렉터리 위치 변경하기

print(os.getcwd())
#현재 디렉터리 위치 리턴

os.system("dir")
#시스템 자체의 프로그램이나 기타 명령들을 파이썬에서 호출
# 시스템 명령어인 dir호출


#f=os.popen("dir")
#시스템 명령어를 실행시킨 결과값을 읽기 모드 형태의 파일 객체로 리턴
#print(f.read())


#os.mkdir(디렉터리)
#디렉터리 생성 make directory


#os.rmdir(디렉터리)
#디렉터리 삭제 remove directory
#디렉터리가 비어 있어야 삭제 가능


#os.unlink(파일이름)
#파일을 지운다


#os.rename(src,dst)
#src라는 이름의 파일을 dst라는 이름으로 바꾼다


import shutil
#파일을 복사해주는 파이썬 모듈

#shutil.copy("src.txt","dst.txt")
#src.txt의 내용이 dst.txt에 복사


import glob
#glob.glob("C:\Python\q*")
#q로 시작하는 파일들 읽어들인다


import tempfile
#파일을 임시로 만들어 사용한다
filename=tempfile.mktemp()
#mktemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 리턴
print(filename)
f=tempfile.TemporaryFile()
#임시 저장 공간으로 사용될 파일 객체 리턴
#기본적으로 wb
f.close()
#TemporaryFile()에서 리턴된 파일 객체는 close 하면 자동으로 사라짐


import time
print(time.time())
#현재 시간을 실수 형태로 리턴

print(time.localtime(time.time()))
#연도,월,일,시,분,초,,,,

print(time.asctime(time.localtime(time.time())))
#'Sat Apr 28 20:50:20 2001'
#localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 리턴

print(time.ctime())
#'Sat Apr 28 20:56:31 2001'
#asctime과 다른점은 항상 현재 시간만을 리턴

#time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))
#여러 포멧 코드 제공

for i in range(5):
    print(i)
    time.sleep(1)
#시간 간격 두기


import calendar
#print(calendar.calendar(2015))
#한 해의 전체 달력 보기


#print(calendar.prcal(2015))
#한 해의 달력 보기


calendar.prmonth(2015,12)
#한 달의 달력 보기

print(calendar.weekday(2021,2,20))
#요일 리턴(숫자)

print(calendar.monthrange(2021,2))
#그 달의 1일이 무슨 요일인지, 그 달이 며칠까지 있는지 튜플 형태로 리턴


import random
print(random.random())
#0.0~1.0 실수
print(random.randint(1,10))
#1~10 정수

import webbrowser
#webbrowser.open("http://google.com")
#웹 브라우저를 자동으로 실행시키고 해당 주소로 가게 해줌
#webbrowser.open_new("http://google.com")
#웹 브라우저가 실행된 상태이더라도 새로운 창으로 해당 주소가 열리도록 함



