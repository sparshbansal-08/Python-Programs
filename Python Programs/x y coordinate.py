x=int(input("enter first point"))
y=int(input("enter second point"))
if x>0 and y>0:
    print("1st quadrant")
elif x<0 and y>0:
    print("2nd quadrant")
elif x<0 and y<0:
    print("3rd quadrant")
elif x>0 and y<0:
    print("4th quadrant")
elif(x==0 and ((y>0)or (y<0))):
    print("on y axix")
elif (((x>0)or (x<0))and y==0):
    print("on x axis")
else:
    print("on origin")
