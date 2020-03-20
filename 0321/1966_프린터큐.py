# priority = [(우선순위, 인덱스), (우선순위, 인덱스), ...)

t = int(input())
for _ in range(t):
    ans = 0
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    priority = []
    priority_max = max(p)

    for i in range(n):
        priority.append((p[i], i))

    while True:
        tmp_pri, tmp_i = priority.pop(0)

        if tmp_pri == priority_max:
            ans += 1
            if tmp_i == m:
                print(ans)
                break
            p[tmp_i] = 0
            priority_max = max(p)  # 최대값 갱신

        else:
            priority.append((tmp_pri, tmp_i))
