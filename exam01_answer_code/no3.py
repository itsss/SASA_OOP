'''
한국에서는 보편적으로 날짜를 표기할 때 '년','월','일' 을 활용한다.

보편적인 표기 방식에 맞게 출력하는 함수(kor_date)를 작성하였다.
이를 참고하여, 다음 Code의 실행 결과를 작성하시오.
'''

def kor_date(year, month, day):
    return "{}년 {}월 {}일".format(year, month, day)

print(kor_date(1,1,1))  # 1년 1월 1일
print(kor_date(2, day=3, month=4))  # 2년 4월 3일