try:
    4/0
except ZeroDivisionError as e:
    print(e)
else:
    print("success")
finally:
    print("fin")
#division by zero 출력
#만약 ZeroDivisionError오류나면 메시지 출력
#오류 안나면 success 출력
#finally는 예외 여부와 관계없이 실행
#finally는 보통 f.close() 씀
#에러 무시할 때에는 except ~~~~: 뒤에 pass씀



