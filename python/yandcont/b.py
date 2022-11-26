n = int(input())
log = []
rockets = {}

for _ in range(n):
    info = input().split()
    id = int(info[3])
    status = info[4]
    time = int(info[2]) + int(info[1]) * 60 + int(info[0]) * 1440
    log.append([time,status,id])

log = sorted(log, key=lambda x:x[0])

for log_info in log:
    time, status, id = log_info
    if id not in rockets:
        rockets[id] = []
    rockets[id].append([status, time])
    
for rocket in sorted(rockets):
    ans = 0
    temp = 0
    for event in rockets[rocket]:
        status = event[0]
        time = event[1]
        if status == 'A':
            temp = time
        elif status == 'B':
            ans += time - temp
            temp = time
        elif status == 'C':
            ans += time-temp
            temp = time
        else:
            ans += time - temp
            temp = time
    print(ans, end = ' ')