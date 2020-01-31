# DP(Dynamic Programming) 이란?
https://www.youtube.com/watch?v=FmXZG7D8nS4&t=702s
https://devmuseum.tistory.com/7
* 큰 문제를 작은 문제로 나눌 수 있다.
* 작은 문제에서 구한 정답을 큰 문제에서 사용한다. (미리 저장해놓고 필요할 때 불러와 사용한다)

# 문제 푸는 방법
* (1) Top Down 방식
** 문제를 작은 문제로 나눈다.
** 작은 문제를 푼다. (답을 저장해놓는다.)
** 작은 문제의 답으로 전체 문제를 푼다.



```{python}
d = [0]*100

def dp(x):
    if x==1 : return 1
    if x==2 : return 1
    if d[x] != 0 : return d[x]

    d[x] = dp(x-1) + dp(x-2)
    return d[x]

if __name__ == '__main__':
    print(dp(int(input())))
```

* (2) Bottom Up 방식
** 가장 작은 문제부터 푼다.
** 문제의 크기를 점점 늘려가며 전체 문제를 푼다.
