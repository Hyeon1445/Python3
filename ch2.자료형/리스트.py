a=['a',1,2,'b',123]
a[1:4]=[]
print(a)
# 리스트 요소 삭제하기1


del a[0]
print(a)
#리스트 요소 삭제하기2

print(a[0])
#삭제하고 나면 앞으로 땡겨와서 인덱스 0부터 채워짐

a.append(4)
print(a)
# 리스트에 요소 추가
a.append(['b',5])
#리스트를 추가하면 [123,4,['b',5]] 이렇게 추가됨
print(a)

d=['a','c','b']
d.sort()
print(d)
e=[1,5,8,3,9,7]
e.sort()
print(e)
#리스트 정렬 
#sort함수는 정렬해서 저장함. 반환은 따로 안함

e.reverse()
print(e)
# 거꾸로 뒤집기 (역순 정렬 아님)


print(e.index(8))
#인덱스 반환, 존재하지 않으면 에러

e.insert(3,4)
#인덱스3위치에 4삽입, 삽입 위치 뒤는 한칸씩 밀림
print(e)

e.remove(7)
print(e)
#처음 등장하는 7 삭제, 한칸씩 땡겨서 빈자리 메꾸기

print(e.pop(1))
print(e)
# 인덱스 1 위치의 값을 pop한다 (반환 & 삭제)

f=[1,1,1,1,12,3,4,5,1,1,1]
print(f.count(1))
#1의 개수 세기

e.extend(f)
print(e)
#e에 f붙이기,확장
