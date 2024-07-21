a = int(input())

for i in range(a):
    b = []
    c = input()
    for j in c :
        if j == '(' :
            b.append(j)
        elif j == ')':
            if len(b) != 0:
                b.pop()
            else :
                print("NO")
                break
    else:
        if len(b) == 0:
            print("YES")
        else:
            print("NO")
