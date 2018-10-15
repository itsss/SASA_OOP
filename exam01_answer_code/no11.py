'''
Decorator를 학습한 세종이는 본인이 작성한 함수를 테스트 할 때 사용할 Decorator를 작성했다.

세종이가 작성한 Decorator function_debug의 적용 결과가 다음과 같을 때 'function_debug'를 작성하시오.
'''

def function_debug(or_func):
    def wp_func(*args, **kwargs):
        print('=== function debug ===')
        return or_func(*args, **kwargs)
    return wp_func

@function_debug
def sasa_teacher(teacher_name):
    print('SASA Teacher [%s]' % teacher_name)

@function_debug
def sasa_teacher_room(teacher_name, room):
    print('SASA Teacher [%s] in [%s]' % (teacher_name, room))

sasa_teacher('kadragon')
sasa_teacher_room('kadragon', 'A204')