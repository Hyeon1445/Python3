f=open("newfile.txt",'w')
# w로 열고 write하면 새로 써지고
# a로 열고 write하면 추가로 써짐
# r읽기 w쓰기 a추가
for i in range(1,5):
    data="%d번째 줄\n" %i
    f.write(data)
f.close()

f=open("newfile.txt",'r')
line=f.readline()
#readline은 한줄 읽어온다
#readlines는 모든 줄을 읽어서 리스트로 리턴
#read()는 파일 내용 전체를 문자열로 리턴
print(line)
f.close()


with open("second.txt",'w') as f:
    f.write("Hello world!!!")
#with 벗어나는 순간 close는 자동으로 됨
