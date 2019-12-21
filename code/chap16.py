# 队列
# author :captain

import queue

line=queue.Queue()
print(line.empty())
for i in range(50):
    line.put("路人"+str(i))
for j in range(line.qsize()):
    print(line.get())