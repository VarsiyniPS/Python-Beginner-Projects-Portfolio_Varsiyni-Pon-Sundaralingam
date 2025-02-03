pesos=int(input('What do you have left in pesos?')) #Pesos =5600
soles=int(input('What do you have left in soles?')) #Soles =105
reais=int(input('What do you have left in reais?')) #reasis =280
PUSD= pesos*0.00024 #Colombian Pesos to USD 
SUSD= soles*0.27 #Peruvian Soles to USD 
BUSD= reais*0.16926 #Brazillian reais to USD 
TotalUSD=PUSD+SUSD+BUSD
print("total in USD:",TotalUSD,"USD") #Output=77.09
