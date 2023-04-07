L=eval(input())
while(L.count(L[0])!=len(L)):
    c=len(L)
    i=0
    while i<c-1:
        if L[i]+L[i+1]=="RG" or L[i]+L[i+1]=="GR":
            L[i]="B"
            del L[i+1]
            c-=1
        elif L[i]+L[i+1]=="GB" or L[i]+L[i+1]=="BG":
            L[i]="R"
            del L[i+1]
            c-=1
        elif L[i]+L[i+1]=="RB" or L[i]+L[i+1]=="BR":
            L[i]="G"
            del L[i+1]
            c-=1
        i+=1
print(f'"{L[0]}"')
