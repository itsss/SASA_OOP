# -*- coding: utf-8 -*-
"""
Title       sasa_food_menu
Author      ITSC (Taewon Kang)
Date        2018.10.24
"""

import requests
import datetime
from bs4 import BeautifulSoup as bs

now = datetime.date.today()

# pip3 install -U beautifulsoup4
# pip3 install -U requests

PERSONAL_INFO = {
    'id': '',
    'passwd': ''
}
# 달빛학사의 ID와 PW 입력

menu = ['아침', '점심', '저녁']  # 아침, 점심, 저녁 출력

# Session을 활용하기 위해 with를 사용함
with requests.Session() as sess:
    page = sess.get('https://go.sasa.hs.kr')
    # 페이지를 가져와서 html 파싱을 시도
    html = page.text
    soup = bs(html, 'html.parser')

    # CSRF 방지용 input value 가져오기
    csrf = soup.find('input', {'name': 'csrf_test_name'})
    # 두 Dictionary 합치기
    PERSONAL_INFO.update({'csrf_test_name': csrf['value']})
    # 만들어진 로그인 데이터로 로그인 시도
    login_req = sess.post('https://go.sasa.hs.kr/auth/login', data=PERSONAL_INFO)

    # 로그인 성공 여부 확인
    if login_req.status_code != 200:
        raise Exception('로그인 되지 않았습니다!')

    # 급식 페이지에 접속
    data = bs(sess.get('https://go.sasa.hs.kr/main/foodList').text, 'html.parser')
    # 급식 데이터를 크롤링함
    result = data.select('div.timeline-body')

    # SASA FOOD MENU와 오늘 날짜 표시
    print('=' * 50)
    print('SASA FOOD MENU', end=': ')
    print(now)
    print('=' * 50)
    a = []
    for i in result:
        a.append(i.getText().strip())

    # 출력하기 위해 reverse하고 pop함
    a.reverse()
    for i in range(3):
        print(menu[i], end=': ')
        b = str(a.pop())
        print(b.strip())

# 실행 결과 예시:
# ==================================================
# SASA FOOD MENU: 2018-10-24
# ==================================================
# 아침: 찰현미밥 / 황기닭곰탕 / 가래떡버섯불고기 / 찐김치만두 / 총각김치 / 우리밀팬더쇼콜라 / 빅요구르트 /
# 점심: 봉골레파스타 / 바베큐폭립 / 아보카도패스츄리피자 / 그린샐러드와 파인드레싱 / 오이피클 / 배추김치 / 썬업과일쥬스 / 쌀밥(자율) /
# 저녁: 찰현미밥 / 사골조랭이떡국 / 닭살버섯전 / 갈비김치찜 / 데친오징어 /  브로콜리와 초장 / 구운김 / 골드파인애플 / 방울토마토 /
