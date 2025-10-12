

a,b,c,d = map(int, input().split())

c1 = b>c
c2 = d >a
c3 = (c+d) > (a+b)
c4 = c >= 0 and d >= 0
c5= (a % 2 ==0)

if c1 and c2 and c3 and c4 and c5:
    print(f"Valores aceitos")
else:
    print(f"Valores nao aceitos")