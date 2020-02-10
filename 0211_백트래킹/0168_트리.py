#참고링크 : https://postbarca.tistory.com/26

def find(x):
    global count

    #리프노드인 경우
    if len(map[x]) == 0:
        count = count + 1
    else:
        for i in map[x]:
            find(i)


count = 0;
n = int(input())
l = list(map(int, input().split()))
map = [[] for _ in range(52)]

for i in range(0, n):
    #루트노드인 경우
    if (l[i] == -1):
        start = i
    else:
        #map[0] = [1, 2]
        #map[1] = [3, 4]
        map[l[i]].append(i)

t = int(input())
for i in range(n):
    if t in map[i]:
        map[i].remove(t)
        break
if start != t:
    find(start)
print(count)
