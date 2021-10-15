print("""""""""Precio Descuento""""""""")
#Datos de Entrada
precio=int( input( "Ingrese el precio de articulo:" ))

#Proceso
if precio>=200:
  descuento=precio*0.15
  PT=precio-(descuento)
  print("\nSe le aplico el 15%")
  
elif precio>100 and precio<200:
  descuento=precio*0.12
  PT=precio-(descuento)
  print("\nSe le aplico el 12%")

elif precio<100:
  descuento=precio*0.10
  PT=precio-(descuento)
  print("\nSe le aplico el 10%")

else:
  print("Datos incorrectos")
#Datos de salida
print(f"El precio con descuento aplicado es: $ {PT}")
print(f"El  descuento aplicado es: $ {descuento}")

