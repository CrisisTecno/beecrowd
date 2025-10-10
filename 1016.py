

dis = float(input())

X1= 60  #VELOCIDAD 1 KM/H
X2= 90  #VELOCIDAD 2 KM/H
XRes=30 #KM/H * [1H/60MIN] ==> 30/60 = 1/2KM/MIN

# 1KM --> 2MIN 
tg= dis *2
# 60/110 => 0.54 
# 90/110 => 0.81 

#  6600-9900
#

# t1=X1/dis *60  # [km/h]/[km] * [60min/1h]
# t2=X2/dis *60 # [km/h]/[km]

# tg = t2 -t1
print(f"{tg:.0f} minutos")