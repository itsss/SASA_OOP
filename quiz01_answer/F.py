'''
문제 F: [PYTHON] Class 만들어 보기 / 라면

세종이는 학교에 있으면 좋을것 같은 기계로, 라면 끓이는 기계가 있었으면 좋겠다고 생각했다.
전혀~ 관련 없지만, 라면을 넣고 maker() 를 호출하면 라면을 만들어주는 클래스를 제작해보고자 한다.

세종이가 만들어야 하는 클래스(RamenMaker)는, 클래스 생성시(__init__) 라면의 이름(문자열 한개)을 매개변수로 받고,
클래스의 maker() 메소드를 호출하면 라면명에 " making complete" 을 붙여서 출력한다.

완성하시오!

입력
없음.

출력
코드가 뒤에 붙어 자동으로 출력됨.

출력 예시
raccoon making complete
udon making complete
'''

class RamenMaker:
    def __init__(self, a):
        self.a = a

    def maker(self):
        return self.a + ' making complete'

# 선 입력 Rear Code
rm1 = RamenMaker('raccoon')
rm2 = RamenMaker('udon')

print(rm1.maker())
print(rm2.maker())