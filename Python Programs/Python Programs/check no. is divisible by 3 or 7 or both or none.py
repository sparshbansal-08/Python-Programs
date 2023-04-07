a=int(input("enter any no."))
if a%3==0 and a%7==0:
    print('divisible by 3 and 7')
elif a%7==0:
    print('divisible by 7')
elif a%3==0:
    print('divisible by 3')
else:
    print('not divisible')
