dic={'name':'lee','phone':'01077773333','birth':'0123'}
# key:value
# value에 리스트도 가능

print(dic.get('name'))
# key로 value 얻기
# dic['name']은 없을 경우 에러, get은 없으면 None 반환

print('name' in dic)
#있으면 True 없으면 False

dic['num']=123
print(dic)
# 딕셔너리 쌍 추가

del dic['phone']
print(dic)
# 딕셔너리 쌍 삭제

print(dic.keys())
# key 리스트 만들기, dic_keys 반환
# append,insert,pop,remove,sort 등의 함수는 못 씀
# 리스트로 만들려면 list(dic.keys())

print(dic.values())
# value 리스트 만들기

print(dic.items())
# key,value 쌍 얻기

dic.clear()
print(dic)
# 모든 쌍 지우기
