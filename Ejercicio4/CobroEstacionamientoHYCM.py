print("""""""""Cobro del Estacionamiento""""""""")
#Datos de Entrada
HorasT=int( input( "Ingrese Las Horas Transcurridas:" ))

#Proceso
if HorasT<=2:
  Total=HorasT*5
  
elif HorasT<=5:
  Total=((HorasT-2)*4)+10

elif HorasT<=10:
  Total=((HorasT-5)*3)+22
  
elif HorasT>10:
  Total=((HorasT-10)*2)+37
else:
  print("Datos incorrectos")
#Datos de salida
print(f"\nEl pago  por las {HorasT} horas transcurridas es: S/.{Total}")