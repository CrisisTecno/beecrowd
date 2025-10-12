
n1,n2,n3,n4 = map(float,input().split())
# 2, 3, 4 e 1  ==> 11
prom1 = (n1*2 + n2*3 + n3*4 + n4*1)/10
print(f"Media: {prom1:.1f}")
if prom1 <5:
    print (f"Aluno reprovado.")
elif prom1 < 7:
    print(f"Aluno em exame.")
    exam=float(input())
    print(f"Nota do exame: {exam:.1f}")
    prom2 = (exam + prom1)/2
    if prom2 < 5: #4.9999999 /= 5
        print (f"Aluno reprovado.")
    else:
        print(f"Aluno aprovado.")
    print(f"Media final: {prom2:.1f}")
else:
    print(f"Aluno aprovado.")