print("SUELDO SEMANAL")

#Datos de Entrada
HorasT=int( input( "Ingrese Las Horas Trabajadas:" ))
PH=int( input( "Ingrese el pago por hora:" ))

#Proceso
if HorasT>40:
  exedente=(HorasT-40)
  SUELDO=(40*PH)+(exedente*PH*2)
  print(f"\nEl pago semanal por las {PH} horas trabajadas es: S/.{SUELDO}")
else:
  SUELDO=(HorasT*PH)
  print(f"\nEl pago semanal por las {PH} horas trabajadas es: S/.{SUELDO}")