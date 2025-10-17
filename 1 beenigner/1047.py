




h_i,m_i,h_f,m_f = map(int,input().split())
 
 
# ==> hi > hf    17 == 5         5   ==>  7 + 5    13 horas    24 -17 = 7
    
# ==> mi > mf    17 == 5   14       15      5     ==> 45 + 5 == 50

if h_i == h_f and m_f == m_i :
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    exit()

if h_i > h_f:    # 6 - 24hrs  + 3
    h_d = (24 - h_i) + h_f
else:
    h_d = h_f - h_i  
                            
if m_i > m_f:
    h_d -= 1
    m_d =  m_f + 60 - m_i 

else:
    m_d = m_f - m_i 

if h_d < 0:
    h_d += 24

print(f"O JOGO DUROU {h_d} HORA(S) E {m_d} MINUTO(S)")

