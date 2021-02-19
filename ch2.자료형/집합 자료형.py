s1=set([1,2,3])
print(s1)
#{1,2,3}


s2=set("Hello")
print(s2)
# {'l','o','e','H'}
# 중복 X
# 순서 없다

s3=set([2,3,4])
print(s1&s3)
#교집합
# {2,3}
print(s1|s3)
#합집합
# {1,2,3,4}
print(s1-s3)
#차집합
# {1}

s1.update([7,8,9,10])
print(s1)
#추가하기
#{1,2,3,7,8,9,10}

s1.remove(7)
print(s1)
#삭제하기
#{1,2,3,8,9,10}

