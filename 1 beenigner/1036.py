

a,b,c = map (float,input().split())
if a == 0 or (4*a*c) > (b**2):
    print("Impossivel calcular")
else:
    raiz = (((b**2)-(4*a*c))**(1/2))
    x2 = (-b+raiz)/(2*a)
    print(f"R1 = {x2:.5f}")
    x1 = (-b-raiz)/(2*a)
    print(f"R2 = {x1:.5f}")


