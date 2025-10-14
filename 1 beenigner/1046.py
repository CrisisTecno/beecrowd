

i,f = map(int,input().split())

if i > f:
    r1= 24 - i
    total = r1+f 
else:
    total = f -i

if total == 0:
    total=24
print(f"O JOGO DUROU {total:.0f} HORA(S)")