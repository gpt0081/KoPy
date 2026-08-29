for number in range(1, 8):
    if number % 2 == 0:
        print(number, "짝수")
    else:
        print(number, "홀수")

target = 5
for candidate in range(10):
    if candidate == target:
        print("찾음:", candidate)
        break
else:
    print("찾지 못함")
