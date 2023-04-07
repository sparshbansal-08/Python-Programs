print("Enter the amount:")
amt=int(input())
tt=amt//2000
fh=(amt-tt*2000)//500
th=(amt-tt*2000-fh*500)//200
hh=(amt-tt*2000-fh*500-th*200)//100
print("2000:",tt)
print("500:",fh)
print("200:",th)
print("100:",hh)
