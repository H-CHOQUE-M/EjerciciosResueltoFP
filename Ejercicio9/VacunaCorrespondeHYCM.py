print("-----Tipo de Vacuna-----")

#Datos de entrada
edad=int(input("Ingrese edad:"))
sexo=int(input("Ingrese un numero,\n1.Si es hombre\n2.Si es mujer\n:"))


if sexo==1 and edad<16:
 print("Le corresponde la vacuna A")
elif sexo==2 and edad<16:
  print("Le corresponde la vacuna A")
elif sexo==1 and edad>=16 and edad<=69:
  print("Le corresponde la vacuna A")
elif sexo==2 and edad>=16 and edad<=69:
  print("Le corresponde la vacuna B")
elif sexo==1 and edad>=70:
  print("Le corresponde la vacuna C")
elif sexo==2 and edad>=70:
  print("Le corresponde la vacuna C")
else:
  print("Datos incorrectos")