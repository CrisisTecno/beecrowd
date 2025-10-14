

x,y,z =map(float, input().split())

A,B,C= sorted([x,y,z],reverse=1)
      
if(A >= B + C):
    print("NAO FORMA TRIANGULO")
    exit()

if (A**2) == (B**2) + (C**2):
    print("TRIANGULO RETANGULO")

if (A**2) > (B**2) + (C**2):
    print("TRIANGULO OBTUSANGULO")

if (A**2) < (B**2) + (C**2):
    print("TRIANGULO ACUTANGULO")

if A == B == C:
    print("TRIANGULO EQUILATERO") 

if ((A ==B ) and B!= C) or ((A ==C ) and A!= B) or ((C ==B ) and B!= A):
    print("TRIANGULO ISOSCELES")