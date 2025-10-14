

A,B,C = map(float,input().split())
if A+B>C and B+C>A and C+A>B:
    p = A+B+C
    print(f"Perimetro = {p:.1f}")
else:
    a1 = (A+B)*C/2
    print(f"Area = {a1:.1f}")