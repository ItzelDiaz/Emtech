import csv
lista_datos=[] #lista que va a contener toda la DB

with open("synergy_logistics_database.csv","r") as archivo:
  lector= csv.reader(archivo)

  for linea in lector:
    lista_datos.append(linea) #mueve cada fila de la base a lista_datos

Opcion=int(input("¡BIENVENIDO A SYNERGY LOGISTICS! \n Elija una opción: \n 1. Para ver el análisis sobre las rutas más demandadas, \n 2. Para ver los medios de transporte que generan mayor valor o \n 3. Para ver los países que generaron el 80% de los ingresos de la compañía.\n Ingrese una opción:"))


##TODO ESTO SIRVE

def top(direccion):
  #direccion="Exports"
  contador=0
  
  rutas_contadas=[]
  rutas_ordenadas=[]

  for ruta in lista_datos:
    if ruta[1]==direccion:
      ruta_actual=[ruta[2],ruta[3]] #lista con origen y destino

      if ruta_actual not in rutas_contadas:
        suma=0
        for movimiento in lista_datos:
          if ruta_actual==[movimiento[2], movimiento[3]] and movimiento[1]==direccion:
            contador+=1
            suma+=int(movimiento[9])
        
        rutas_contadas.append(ruta_actual)
        rutas_ordenadas.append([ruta[2],ruta[3],contador,suma])
        contador=0
        

  rutas_ordenadas.sort(reverse=True, key=lambda x: x[3])
  #print(rutas_ordenadas)
  print("\n-----***-----\n")
  top10_valor=rutas_ordenadas[0:10]
  print("TOP 10 DE RUTAS CON MAYOR APORTE:",direccion,"\n")
  for top in top10_valor:
    print("La ruta ",top[0],"-",top[1],"tuvo",top[2],"ocurrencias y aportó un valor de $",top[3])

  orden_demanda=rutas_ordenadas
  orden_demanda.sort(reverse=True, key=lambda x: x[2])
  #print(orden_demanda)
  print("\n-----***-----\n")
  top10_demanda=orden_demanda[0:10]
  print("TOP 10 DE RUTAS MÁS DEMANDADAS:",direccion,"\n")
  for top in top10_demanda:
    print("La ruta ",top[0],"-",top[1],"tuvo",top[2],"ocurrencias y aportó un valor de $",top[3])

  #VERIFICAR SI LAS RUTAS ORDENADAS POR DEMANDA O POR VALOR SON LAS MISMAS EN EL TOP10  
  # lista_booleanos=[]
  # for i in range(len(top10_demanda)):
  #   if top10_demanda[i][0]==top10_valor[i][0] and top10_demanda[i][1]==top10_valor[i][1]:
  #     lista_booleanos.append("MISMA RUTA")
  #   else:
  #     lista_booleanos.append("DIFERENTE RUTA")
  # print(lista_booleanos)

 
if Opcion==1:
  top("Exports")
  top("Imports")
  

#----------------------
##OPCIÓN 2
#---------------------

transportes=[]
for registro in lista_datos:
  transportes.append(registro[7]) #agrega a transportes todos los transportes que aparecen en la columna transport_mode
  medios_transporte=set(transportes) #convierte a conjunto para quitar los que se repiten 
  medios_transporte.remove("transport_mode") #quita la primera entrada



def top_transportes(direccion):
  sumas_transportes=[]
  for transporte in medios_transporte:
    contador=0
    suma=0
    for registro in lista_datos:
      if registro[7]==transporte and registro[1]==direccion:
        contador+=1
        suma+=int(registro[9])
    sumas_transportes.append([transporte,contador,suma])
    sumas_transportes.sort(reverse=True, key=lambda x: x[2])
    sumas_transportes=sumas_transportes[0:3]
  print(sumas_transportes)

if Opcion==2:
  print("\n-----***-----\n")
  print("TRANSPORTES CON MAYOR APORTACIÓN DE ACUERDO A LAS EXPORTACIONES")
  top_transportes("Exports")
  print("\n-----***-----\n")
  print("TRANSPORTES CON MAYOR APORTACIÓN DE ACUERDO A LAS EXPORTACIONES")
  top_transportes("Imports")


#---------------------
#OPCIÓN 3.
#-------------------- 
#Hice las uniones primero (países que exportan, países que importan y países con doble flujo)
#Después hice funciones para llamar sólo a los países que importan o sólo a los que exportan

lista_datos.pop(0)
origen=[]
for registro in lista_datos:
  origen.append(registro[2]) #agrega los países de origen
  origen.append(registro[3]) #agrega los países de destino
  lista_paises=list(set(origen)) #convierte a conjunto para quitar los que se repiten 
  lista_paises.sort()
#print(lista_paises)


aportaciones_pais=[]
for pais in lista_paises: #itera sobre cada país de la lista
  cuenta_pais=0
  suma_pais=0
  for registro in lista_datos: #itera sobre toda la BD
    if (registro[1]=="Exports" and registro[2]==pais) or (registro[1]=="Imports" and registro[3]==pais): #toma los orígenes de exports o los destinos de imports
      cuenta_pais+=1 #suma las veces que apareció
      suma_pais+=int(registro[9]) #suma los valores de cada ruta
      
  aportaciones_pais.append([pais,cuenta_pais, suma_pais]) #lista de listas, cada lista tiene un país de todos los que aparecen en la BD, las veces que exportó y tuvo ingresos ("Export"(origin) o "Imports" (destination)) y la suma de todos los movimientos con la condición anterior
paises_generadores=[]
for aportacion_pais in aportaciones_pais:
  if aportacion_pais[1]!=0: #quita los países que no aportan valor a la empresa (son destinos de exports o origen de imports)
    paises_generadores.append(aportacion_pais)
paises_generadores.sort(reverse=True, key=lambda x: x[2]) #ordena de acuerdo al valor aportado
#print(paises_generadores)

suma_total=0
for pais_generador in paises_generadores:
  suma_total+=int(pais_generador[2]) #suma los valores aportados por todos los países
percentil80=suma_total*0.8

# percentiles=[]
# suma=0
# i=0
# while suma+paises_generadores[i][2] <= percentil80: #while que suma hasta el 80% de los ingresos y se asegura de no sumar la siguiente entrada si rebasa este porcentaje 
#   suma+=paises_generadores[i][2]
#   percentiles.append([paises_generadores[i][0],paises_generadores[i][2]/suma_total,suma/suma_total])  #lista que contiene el nombre del país, el % que aporta a todos los ingresos, el %acumulado
#   i+=1
# print(percentiles) #Noté que la última entrada aporta sólo el 5% y el acumulado sólo es el 75%, por lo que la siguiente entrada debería estar más cerca del 80%, por lo que hice el siguiente while

#Este ciclo va a tener como resultado la unión de los países importadores, exportadores y los que tienen doble aportación (doble flujo)
suma=0
i=0
percentiles_union=[] #percentiles=[nombre del pais, % que aporta al total de ingresos, %acumulado]
while suma <= percentil80: #cuando entra al ciclo sólo checa que la suma aún no haya rebasado el 80% de los ingresos
  suma+=paises_generadores[i][2] #suma el valor aportado
  percentiles_union.append([paises_generadores[i][0],paises_generadores[i][2]/suma_total,suma/suma_total]) #lista [nombre del país, % que aporta al total de ingresos, % acumulado]
  i+=1
#print(percentiles)


def funcion_destino(direccion):
  if direccion=="Exports":
    k=2 #Si la dirección es exports, va a tomar el origen
  elif direccion=="Imports":
    k=3 #Si la dirección es Imports va a tomar destination

  lista_datos.pop(0)
  origen=[]
  for registro in lista_datos:
    if registro[1]==direccion:
      origen.append(registro[k]) #llena la lista de países con las condiciones de exports([2]), imports([3])
      paises_exportadores=list(set(origen)) #convierte a conjunto para quitar los que se repiten 
      #paises_exportadores.sort() 

#Da como resultado una lista [nombre del país, veces que tuvo aportaciones, monto de las aportaciones ]
  pais_exportador_suma=[]
  suma_pais_exportador=0
  for pais_exportador in paises_exportadores:
    cuenta_pais_exportador=0
    suma_pais_exportador=0
    for registro in lista_datos:
      if registro[1]==direccion and registro[k]==pais_exportador:
        cuenta_pais_exportador+=1
        suma_pais_exportador+=int(registro[9])
    pais_exportador_suma.append([pais_exportador,cuenta_pais_exportador, suma_pais_exportador])
    pais_exportador_suma.sort(reverse=True, key=lambda x: x[2]) #ordena de acuerdo a las aportaciones
  return(pais_exportador_suma)

#funcion_destino("Exports")
#funcion_destino("Imports")


def percentil(alfa,direccion): #Toma como argumentos el percentil (tomaremos el 80 esta vez y la direccion (imports o exports))
  global funcion_destino 
  A= funcion_destino(direccion) #asigna la lista de listas "pais_exportador_suma" a la variable A
  suma=0
  for i in A: #itera sobre cada lista de "pais_exportador_suma"
    suma+=i[2] #suma cada monto aportado por país
  percentil=suma*alfa 
  suma_destino=0
  percentiles=[] #[nombre del psís, % que aporta a los ingresos totales, %acumulado]
  i=0
  while suma_destino+A[i][2]<=percentil:
    suma_destino+=A[i][2]
    percentiles.append([A[i][0],A[i][2]/suma,suma_destino/suma])  
    i+=1
  print(percentiles)

if Opcion==3:
  print("\n-----***-----\n")
  print("PAÍSES IMPORTADORES, EXPORTADORES Y CON DOBLE FLUJO CON MAYOR APORTACIÓN")
  print(percentiles_union)
  print("\n-----***-----\n")
  print("PAÍSES IMPORTADORES CON MAYOR APORTACIÓN")
  percentil(0.8,"Imports")
  print("\n-----***-----\n")
  print("PAÍSES EXPORTADORES CON MAYOR APORTACIÓN")
  percentil(0.8,"Exports")
