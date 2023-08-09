from random import randrange

# Q. n면체 주사위 위젯의 전체 코드를 작성해봅시다.

class FunnyDice:
    def __init__(self, n=6):
        # MARK: Safety code
        n = int(n)
        if (n < 1):
            n = 1
        
        self.n = n
    
    def throw(self):
        self.val = randrange(0, self.n) + 1
    
    def getval(self):
        return self.val
    
    def setval(self, val:int):
        if (val < 1 or val > self.n):
            msg = "|  __ 입력하신 `{0}`은(는) 주사위에 없는 숫자 입니다. 주사위는 `1` ~ `{1}`까지 있습니다. __".format(val, self.n)
            raise ValueError(msg)

        self.val = val

def get_inputs():
    n = int(input("|  → 주사위 면의 개수를 입력해주세요: "))

    return n

def main():
    print("|" + "=" * 20)
    print("|")
    print("|")
    n = get_inputs()
    mydice = FunnyDice(n)
    mydice.throw()
    print("|  행운의 숫자는? {0}".format(mydice.getval()))
    print("|")
    print("|")
    print("|  いかさまサイコロって知ってますか？")
    print("|  사기 주사위(혹은 조작된 주사위, 아카사마 주시위) 라고 들어보셨나요?")
    print("|  한번 체험을 해봅시다!")
    val = int(input("|  → 내가 나오게 하고 싶은 주사위의 눈의 숫자를 입력해주세요: "))
    mydice.setval(val)
    print("|  행운의 숫자는? {0}".format(mydice.getval()))
    print("|")
    print("|")
    print("|  도박중독 상담은 국번없이 1336 입니다.")
    print("|")
    print("|")
    print("|" + "=" * 20)

if __name__ == '__main__':
    main()

