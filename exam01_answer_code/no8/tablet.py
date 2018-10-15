'''
browser.py, tablet.py, music.py 파일 3개는 모두 같은 위치에 존재한다.
tablet.py 파일 내 'tablet()' 함수가 실행된 결과가 아래와 같다고 할 때,
tablet() 함수가 정상적으로 실행되기 위한 Line 1, 2를 작성하시오.

https://go.sasa.hs.kr 에 접속합니다.
달빛학사 에 접속합니다.
교가 재생합니다.
다음 곡을 재생합니다.

'''

import browser
from music import *

def tablet():
    browser.url('https://go.sasa.hs.kr')
    browser.search('달빛학사')
    play('교가')
    next_play()

tablet()