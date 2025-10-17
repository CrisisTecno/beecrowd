dic = {
    400:15,
    800:12,
    1200:10,
    2000:7,
    float('inf'):4,
}

salario = float(input())
for i,j in dic.items():
    #400.1
    if salario> i:
        continue
    else:
        incremento = j/100 * salario
        print(f"Novo salario: {(salario+incremento):.2f}")
        print(f"Reajuste ganho: {incremento:.2f}")
        print(f"Em percentual: {(j):.0f} %")
        break
    
#     Novo salario: 880.01
# Reajuste ganho: 80.00
# Em percentual: 10 %a
