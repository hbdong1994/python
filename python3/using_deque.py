from collections import deque

d = deque(maxlen=10)   # 双端队列 限定长度 如果超出长度 会从另一侧pop出去

for i in range(13):
    d.append(i)

print(d)


dd = deque([1, 2, 3, 4, 5])
dd.extendleft([-2, -1, 0])
dd.extend([6, 7, 8])

print(dd)
