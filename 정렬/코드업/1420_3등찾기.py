
s = {}
n = int(input())

for _ in range(n):
    name, score = input().split()
    s[name] = int(score)

# 값 기준으로 딕셔너리 정렬하기 (key만 출력됨)
result = sorted(s, key=lambda x : s[x], reverse=True)
#result = sorted(s.items(), key=lambda x : x[1], reverse=True)
print(result[2])

