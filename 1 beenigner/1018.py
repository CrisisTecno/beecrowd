total2= int(input())
cortes= [100,50,20,10,5,2,1]

print(f"{total2}")
total3 =total2
for corte in cortes:
    numero_billetes =total3 //corte
    total3 = total3 - (numero_billetes*corte)
    print(f"{numero_billetes} nota(s) de R$ {corte},00")

c100 = total2 // 100
# c100 => 5  ->500
total = total2 - (c100*100) #576-500
#total = 76
c50 =total // 50
total = total - (c50*50)
c20 =total // 20
total = total - (c20*20)
c10 =total // 10
total = total - (c10*10)
c5 =total // 5
total = total - (c5*5)
c2 =total // 2
total = total - (c2*2)
print(f"{total2}")
print(f"{c100} nota(s) de R$ 100,00")
print(f"{c50} nota(s) de R$ 50,00")
print(f"{c20} nota(s) de R$ 20,00")
print(f"{c10} nota(s) de R$ 10,00")
print(f"{c5} nota(s) de R$ 5,00")
print(f"{c2} nota(s) de R$ 2,00")
print(f"{total} nota(s) de R$ 1,00")