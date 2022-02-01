
def find_rooms(hour, city, rooms):
    for room in rooms[city]:
        if hour in rooms[city][room]:
            print(room, end=" ")
            return

rooms = {}
with open('input.txt', 'r') as input:
    c = int(input.readline())
    unions = {}
    for i in range(c):   
        city, k = input.readline().split()
        _temp_union = set()
        _rooms = {}
        for j in range(int(k)):       
            schedule, name = input.readline().split()
            _rooms[name] = set()
            for num, hour in enumerate(schedule):
                if hour == '.':
                    _rooms[name].add(num)
                    _temp_union.add(num)
        rooms[city] = _rooms
        unions[city] = _temp_union
    m = int(input.readline())
    requests = []
    for i in range(m):
        requests.append(input.readline().split()[1:])

for i in requests:
    suggested_union = set([i for i in range(24)])
    for city in i:
        suggested_union.intersection_update(unions[city])
    if not suggested_union:
        print("No")
        continue
    else:
        print("Yes", end=" ")
        hour = suggested_union.pop()
        for city in i:
            find_rooms(hour, city, rooms)
    print()