class Counter:
    def __init__(self, start=0):
        if start < 0:
            raise ValueError("시작 값은 0 이상이어야 합니다.")
        self.value = start

    def increase(self, amount=1):
        if amount < 0:
            raise ValueError("증가량은 0 이상이어야 합니다.")
        self.value += amount
        return self.value


counter = Counter(2)
print(counter.increase())
print(counter.increase(3))

try:
    counter.increase(-1)
except ValueError as error:
    print("오류:", error)
