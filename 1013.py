A,B,C = map(int,input().split())

if A > B:
    if A>C:
        print(f"{A} eh o maior")
    else:
        print(f"{C} eh o maior")
else:
    if B> C:
        print(f"{B} eh o maior")
    else:
        print(f"{C} eh o maior")

