

dic={
    "aguia" :"vertebradoavecarnivoro",
    "pomba" :"vertebradoaveonivoro",
    "homem" :"vertebradomamiferoonivoro",
    "vaca" :"vertebradomamiferoherbivoro",
    "pulga" :"invertebradoinsetohematofago",
    "lagarta" :"invertebradoinsetoherbivoro",
    "sanguessuga" :"invertebradoanelideohematofago",
    "minhoca" :"invertebradoanelideoonivoro",
}

x = input()
y = input()
z = input()


for i, j in dic.items():
    if j == x+y+z:
        print(i)