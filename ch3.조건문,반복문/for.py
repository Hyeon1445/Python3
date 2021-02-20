arr=['one','two','three','four','five']
for i in arr:
    print(i)

# one two three four five 출력

a=[(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first+last)
# 3 7 11

for i in range(3):
    print(i)
#0 1 2

for i in range(3,10):
    print(i)
#3 4 5 6 7 8 9

for i in range(len(arr)):
    print(i)
#0 1 2 3 4


b=[1,2,3,4]
c=[]
for i in b:
    c.append(i*5)
print(c)
# 5 10 15 20

d=[num*5 for num in b]
print(d)
#5 10 15 20

d=[num*5 for num in b if num%2==0]
print(d)
# 10 20