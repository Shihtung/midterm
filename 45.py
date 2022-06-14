a=int(input('輸入月份'))
b=int(input('輸入日期'))
s=(a*2|b)%3
if s==0:
    print('普通')
elif s==1:
    print('吉')
elif s==2:
    print('大吉')
elif a>12 or b<1 or a<1 or b>31:
    print('輸入錯誤')