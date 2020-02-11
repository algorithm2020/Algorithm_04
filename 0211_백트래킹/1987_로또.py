# 6개 고르는 경우의 수 (백트래킹)

def go(idx, selected, n, lotto_):

    if selected == 6:
        print(' '.join(map(str, a)))
        return
    if idx == n:
        return

    #숫자를 뽑는다.
    a[selected] = lotto_[idx]
    go(idx+1, selected+1, n, lotto_)

    #숫자를 안 뽑는다.
    a[selected] = 0
    go(idx+1, selected, n, lotto_)



#입력받기
while True:
    lotto = list(map(int, input().split()))
    if lotto.pop(0) == 0:
        break

    a = [0] * 6
    go(0, 0, len(lotto), lotto)
    print()

