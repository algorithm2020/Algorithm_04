def check(num):
    for idx, target in enumerate(num[:-1]):
        if num[idx+1].startswith(target):
            return 'NO'
    return 'YES'

# 입력받기
t = int(input())

for _ in range(t):
    n = int(input())
    number = []

    for _ in range(n):
        number.append(int(input()))
    # 크기 순 정렬
    number.sort()
    # 원소가 그다음 원소에 포함되어 있는지 체크
    number = list(map(str, number))
    result = check(number)

    print(result)
