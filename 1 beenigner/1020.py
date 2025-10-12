dias =int(input())
cortes=[365,30,1]

for corte in cortes:
    numero  =  dias //corte
    dias = dias  - (numero*corte)
    if corte == 365:
        print(f"{numero} ano(s)")
    elif corte == 30:
        print(f"{numero} mes(es)")
    else:
        print(f"{numero} dia(s)")