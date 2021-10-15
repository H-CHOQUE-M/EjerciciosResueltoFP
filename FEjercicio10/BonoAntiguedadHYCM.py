print("-----Bono por Antiguedad-----")

#Datos de entrada
bono=int(input("Ingrese sus anhos de antiguedad:"))


if bono==1:
 print("\nSu bono es de $100")
elif bono==2:
  print("\nSu bono es de $200")
elif bono==3:
  print("\nSu bono es de $300")
elif bono==4:
  print("\nSu bono es de $400")
elif bono==5:
  print("\nSu bono es de $500")
elif bono>5:
  print("\nSu bono es de $1000")
else:
  print("\nDatos incorrectos")