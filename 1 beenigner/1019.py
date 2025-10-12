
seg = int(input())
#seg
cortes=[3600,60,1]
strf=""
for corte in cortes:
    numero =seg //corte
    seg = seg - (numero*corte)
    if corte!=1:
        strf =strf+ str(numero)+":"
    else:
        strf =strf+ str(numero)
print(strf)