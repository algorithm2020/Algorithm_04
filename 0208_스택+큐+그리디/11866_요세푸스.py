# people : 1번부터 n번까지 사람
# people이 비면 종료
# k번째를 제거하면 그 자리부터 + (k-1) 번째 자리를 제거한다.
# 인덱스는 리스트의 길이로 나눈 나머지로 계산한다. !! (원 순회)

n, k = map(int, input().split())
people = []
for i in range(1, n+1):
    people.append(i)
result = []

# 맨처음 단계
out_idx = (k-1)%len(people)
result.append(people.pop(out_idx))

# 두번째 단계부터 반복 시작
while people:
    # 맨 오른쪽 사람이 pop 됐던 경우는 첫번째 사람부터 시작
    if out_idx == len(people):
        out_idx = 0
        out_idx = (out_idx + (k - 1)) % len(people)
    else:
        out_idx = (out_idx + (k-1)) % len(people)
    result.append(people.pop(out_idx))

# 결과출력
print("<", end='')
print(", ".join(map(str, result)), end='')
print(">", end='')
