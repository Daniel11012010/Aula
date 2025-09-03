import random 

v = int(input("(Pedra:1/ Papel:2/ Tesoura:3): "))
m = random.randint(1,3)
b = {1:"pedra", 2:"papel", 3:"tesoura"}

print (f"Você escolheu:  {b[v]}")
print (f"Maquina colocou: {b[m]}")

if (v == 1 and m == 2):{
    print("Perdeu")}
    
if (v == 1 and m == 3):{
    print("ganhou")}
    
if(v == 2 and m ==1):{
    print("ganhou")}
    
if(v==2 and m == 3):{
    print("perdeu")}
    
if(v == 3 and m ==1):{
    print("perdeu")}
    
if(v==3 and m == 2):{
    print("ganhou")}
    
if(v==m):{
    print("empate")}
