

# A=float(input())
# B=float(input())
# C=float(input())
A,B,C = map(float,input().split())
Pi = 3.14159
ia=(A*C)/2
ib= (C**2)*Pi
ic=((A+B)*C)/2
ide=B**2
ie= A*B

print(f"TRIANGULO: {ia:.3f}")
print(f"CIRCULO: {ib:.3f}")
print(f"TRAPEZIO: {ic:.3f}")
print(f"QUADRADO: {ide:.3f}") 
print(f"RETANGULO: {ie:.3f}") 