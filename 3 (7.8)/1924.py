a, b = map(int,input().split())
week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
b=b%7
if a == 1:
    print(week[b])
elif a == 2:
    b += 3
    if b >=7:
        b-=7
    print(week[b])
elif a == 3:
    b += 3
    if b >=7:
        b-=7
    print(week[b])
elif a == 4:
    b+=6
    if b >=7:
        b-=7
    print(week[b])
elif a == 5:
    b += 1
    if b >=7:
        b-=7
    print(week[b])
elif a == 6:
    b += 4
    if b >=7:
        b-=7
    print(week[b])
elif a == 7:
    b += 6
    if b >=7:
        b-=7
    print(week[b])
elif a == 8:
    b += 2
    if b >=7:
        b-=7
    print(week[b])
elif a == 9:
    b += 5
    if b >=7:
        b-=7
    print(week[b])
elif a == 10:
    print(week[b])
elif a == 11:
    b += 3
    if b >=7:
        b-=7
    print(week[b])
elif a == 12:
    b += 5
    if b >=7:
        b-=7
    print(week[b])
