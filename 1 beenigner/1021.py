
total = float(input())
cortes=[100,50,20,10,5,2] 
print(f"NOTAS:")
for corte in cortes:
    numero_billetes_corte= total // corte   #75.2 //50 = 1billete de 50
    total= total -numero_billetes_corte*corte 
    print(f"{numero_billetes_corte:.0f} nota(s) de R$ {corte:.2f}")

cortes_moneda=[1.0,0.50,0.25,0.10,0.05,0.01]
print(f"MOEDAS:")
for cut2 in cortes_moneda:
    #0.05  0.04 0.03 0.02 0.01
    #0.01//0.01 = 0
    if cut2 == 0.01:
        print(f"{(total* 100):.0f} moeda(s) de R$ {cut2:.2f}")
    numero_monedas_corte= total // cut2
    total= total -numero_monedas_corte*cut2
    if cut2 != 0.01:
        print(f"{numero_monedas_corte:.0f} moeda(s) de R$ {cut2:.2f}")
# toal = >2 