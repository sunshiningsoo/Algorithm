from collections import deque
import sys

input = sys.stdin.readline

subin, sistar = map(int, input().split())


# 2배로 가거나
# 지금 +1 로 가거나
# 지금 -1 로 가거나

world = [0] * 100001

def solution():
    q = deque()
    q.append([subin, 0])
    answer = 0

    while q:
        next_node, next_weight = q.popleft()
        world[next_node] = next_weight

        if next_node == sistar:
            answer = next_weight
            break

        if next_node >= 1 and world[next_node-1] == 0:
            q.append([next_node-1, next_weight+1])
        if next_node < 100000 and world[next_node+1] == 0:
            q.append([next_node+1, next_weight+1])
        if next_node*2 < 100001 and world[next_node*2] == 0:
            q.append([next_node*2, next_weight+1])

    return answer


a = solution()
print(a)

