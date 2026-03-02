saldo = 1000

deposito = int(input("ingrese cuanto desea depositr: ")) 
saldo_actual = deposito + saldo
print("usted deposito con exito:", deposito)
print("su saldo ahora es:", saldo + deposito)

retiro = int(input("ingrese cuanto desea retirar: "))

if retiro <= saldo_actual:
   print (f"usted ha retirado {retiro} con exito") 
   print ("su saldo ahora es:", saldo_actual - retiro)

else:
   print("monto insuficiente")
   

