'''
정수 1개를 입력받아 합계를 저장하고 이를 출력해주는 'Calculator' Class를 만들어 활용하고 있었다.
이를 기반으로 List를 매개변수로 받아, 담고 있는 정수를 모두 더해주는 'UpCalculator' Class를 만들고자 한다.

다음 Code를 참고하여, 'Calculator' Class를 상속하고, 1개의 함수만을 가지고 있는 'UpCalculator' Class를 작성하시오.
'''

class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, first):
        self.result += first

    def print_result(self):
        print(self.result)

class UpCalculator(Calculator):
    def adder(self, a):
        for i in a:
            self.result += i

c1 = UpCalculator()
c1.adder([1,2,3,4,5])
c1.print_result()