'''
관리하는 강의실을 저장하고 출력해주는 'ManagementPlace' Class를 다음과 같이 작성하였다.
'ManagementPlace' Class를 기반으로, 'n1' 객체를 만들어 아래와 같은 결과가 나오도록 Code를 작성하시오.
'''

class ManagementPlace:
    def __init__(self, user):
        self.user = user
        self.place = []

    def set_place(self, place):
        self.place.append(place)

    def etc(self):
        print("[ %s ]의 강의실" % self.user)
        print(self.place)

a = ManagementPlace('kadragon')
a.set_place('A401')
a.set_place('A306')
a.set_place('A501')
a.etc()