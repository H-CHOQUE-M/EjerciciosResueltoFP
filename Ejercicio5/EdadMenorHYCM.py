print("Nombre y Edad de la persona de menor Edad")

#Datos de Entrada
Nom1 =  input ( "Ingrese el Nombre 1:" )
Edad1 = int ( input ( "Ingrese la edad 1:" ))
Nom2 =  input ( "Ingrese el Nombre 2:" )
Edad2 = int ( input ( "Ingrese la edad 2:" ))
Nom3 =  input ( "Ingrese el Nombre 3:" )
Edad3 = int ( input ( "Ingrese la edad 3:" ))
#Proceso
if Edad1 < Edad2 and Edad1 < Edad3:
  print(f"\nLa edad menor es de {Nom1} ({Edad1} anhos)")

elif Edad2 < Edad1 and Edad2 < Edad3:
  print(f"\nLa edad menor es de {Nom2} ({Edad2} anhos)")

elif Edad3 < Edad1 and Edad3 < Edad2:
  print(f"\nLa edad menor es de {Nom3} ({Edad3} anhos)")
else:
  print("Datos ingresados incorrectos")
