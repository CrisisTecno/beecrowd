

cod, cantidad, precio = map(float,input().split())
cod2, cantidad2, precio2 = map(float,input().split())

total = cantidad*precio + cantidad2*precio2

print(f"VALOR A PAGAR: R$ {total:.2f}")