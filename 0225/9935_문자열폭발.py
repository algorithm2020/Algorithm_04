# 참고링크 : https://ksshlee.github.io/baekjoon/%EB%B0%B1%EC%A4%80-9935-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%8F%AD%EB%B0%9C/

str = input()
bomb = input()

ans = []

for i in str:
    # 문자 하나씩 스택에 집어넣는다.
    ans.append(i)
    if len(ans) >= len(bomb):
        #뒤에서부터 검사!
        for j in range(-1, -len(bomb)-1, -1):
            if ans[j] != bomb[j]:
                break

        else:
            a = 0
            # bomb 길이만큼 pop
            while a < len(bomb):
                ans.pop()
                a += 1


if len(ans) == 0:
    print("FRULA")
else:
    print(''.join(ans))
