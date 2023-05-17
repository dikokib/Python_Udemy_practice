class Person(object):
    #__init__は呼び出し時に初めに読み込まれる
    def __init__(self) -> None:
        print('実行確認')

    def say_something(self):
        print('hello')

    #__del__は呼び出し終了時に読み込まれる
    def __del__(self):
        print('実行終了')

person = Person()
#person.say_something()