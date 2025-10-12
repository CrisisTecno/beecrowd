
t= int(input())
v= int(input())
# d = v * t ===> v = [km/h]*[h]  = [km]
d=t*v  #===> [km]
#12km/l 1l/12km => [L/km] * [km] == [L]

lg=d*1/12

print(f"{lg:.3f}")