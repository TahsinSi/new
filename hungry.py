from collections import deque


container=deque()
str='every soul shall test death'

for i in str:
    container.append(i)

while container:
    print(container.pop(),end='')
