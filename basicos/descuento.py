comp = float(input("Total compra :  "))
 
if comp >1000:
    desc = comp * 0.2
else:
    desc = 0
 
tot_pag = comp - desc
 
print ("Debe pagar :  " , tot_pag)