a=int(input("년도를 적으세요 :"))
if a%4 ==0 and not a%100 ==0 or a%400 ==0  :
    print(1)
else:
    print(0)
