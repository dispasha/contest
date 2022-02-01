with open('input.txt', 'r') as input:
    n, k = map(int, input.readline().split())
    positions = list(map(int, input.readline().split()))

needed_nums = set([i for i in range(1,k+1)])
temp_nums = needed_nums.copy()
min_suggestion = float('inf')

for i in reversed(range(n)):
    position = positions[i]
    if positions[i] in temp_nums:
        temp_nums.discard(position)
        if not temp_nums:
            _n = i+2
            break
if _n > n: _n = n
for i in range(_n):
    if positions[i] not in needed_nums: continue
    try:
        if positions[i] == positions[i+1]: continue
    except:
        pass
    temp_nums = needed_nums.copy()
    temp_sum = 0
    for j in range(i, n):
        position = positions[j]
        temp_sum += position
        if position in temp_nums:
            temp_nums.discard(position)
            if not temp_nums:
                if temp_sum < min_suggestion:
                    min_suggestion = temp_sum
                    break
    
print(min_suggestion)
            

