
def check(num):
    for _ in range(len(num) -1):
        a = num.pop(0)
        for n in num:
            if a in n:
                return "NO"
    return "YES"

# 입력받기
t = int(input())

for _ in range(t):
    n = int(input())
    number = []

    for _ in range(n):
        number.append(int(input()))
    # 크기 순 정렬
    number.sort()
    # pop(0)한 원소가 나머지 원소에 포함되어 있는지 체크
    number = list(map(str, number))
    result = check(number)

    print(result)
