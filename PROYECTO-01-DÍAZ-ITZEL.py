from lifestore_file import lifestore_products, lifestore_searches, lifestore_sales


administradores=[["a", ""], ["Administrador 2","000"],["Administrador 3","000"]]

usuarios=[["b", ""], ["Usuario 2","123"],["Usuario 3","123"]]

user=input("Ingrese usuario: ")
password=input("Ingrese contraseña: ")

es_admin=0
for administrador in administradores:
  if user==administrador[0] and password==administrador[1]:
    print("¡Bienvenido a lifestore", user, "!")
    es_admin=1
    break
  else:
    continue

for usuario in usuarios:
  if user==usuario[0] and password==usuario[1]:
    print("¡Bienvenido a lifestore", user, "!")
    es_admin=2
    break
  else:
    continue

if es_admin==1:
  print("\nSi deseas visualizar los productos con mayores ventas, elige 1. \nSi deseas visualizar los productos con mayores búsquedas, elige 2. \nSi deseas visualizar los productos con menores ventas, elige 3. \nSi deseas visualizar los productos con menores búsquedas, elige 4.\nSi deseas visualizar los productos con mejores y peores reseñas, elige 5. \nSi deseas visualizar un resumen de los ingresos y ventas anuales, elige 6.")
  opcion=input("Elige una opción:")
  continuar="No"
elif es_admin==2:
  print("No eres administrador, pero puedes visualizar los productos con mejores y peores reseñas.")
  continuar=input("¿Deseas verlos? (Sí/No): ")
  opcion="0"
else:
  for i in list(range(2)):
    print("La cuenta con la que intentas ingresar al sistema no existe. Por favor inténtalo de nuevo.")
    user=input("Ingrese usuario: ")
    password=input("Ingrese contraseña: ")
    i+=1  
    #print(i)
    es_admin=0
    for administrador in administradores:
      if user==administrador[0] and password==administrador[1]:
        print("¡Bienvenido a lifestore", user, "!")
        es_admin=1
        continuar="No"
        break
      else:
        continue

    for usuario in usuarios:
      if user==usuario[0] and password==usuario[1]:
        print("¡Bienvenido a lifestore", user, "!")
        es_admin=2
        continuar="No"
        break
      else:
        continue    

    if es_admin==1:
      print("\nSi deseas visualizar los productos con mayores ventas, elige 1. \nSi deseas visualizar los productos con mayores búsquedas, elige 2. \nSi deseas visualizar los productos con menores ventas, elige 3. \nSi deseas visualizar los productos con menores búsquedas, elige 4.\nSi deseas visualizar los productos con mejores y peores reseñas, elige 5. \nSi deseas visualizar un resumen de los ingresos y ventas anuales, elige 6.")
      opcion=input("Elige una opción: ")
      continuar="No"
      break

    elif es_admin==2:
      opcion=0
      print("No eres administrador, pero puedes visualizar los productos con mejores y peores reseñas.")
      continuar=input("¿Deseas verlos? (Sí/No): ")
      opcion=0
      break
    else:
      if i==2:
        print("Ha excedido el número máximo de intentos. \nNo podrá acceder al programa.")
      continuar="No"
      opcion=0



#----------VENTAS------

#ORDENA VENTAS POR PRODUCTO

contador=0
total_ventas=[] #[[id, nombre, contador],[id2, nombre2, contador2]]
for producto in lifestore_products:
  for venta in lifestore_sales:
    if producto[0]==venta[1]:
      contador+=1     
  formato_ideal=[producto[0],producto[1],contador]
  total_ventas.append(formato_ideal)
  contador=0

##ordena por el número de ventas de menor a mayor
total_ventas_ordenadas=[]
while total_ventas:
  minimo=total_ventas[0][2]
  lista_actual=total_ventas[0]
  for cuenta_ventas in total_ventas:
    if cuenta_ventas[2] < minimo:
      minimo=cuenta_ventas[2]
      lista_actual=cuenta_ventas
  total_ventas_ordenadas.append(lista_actual)
  total_ventas.remove(lista_actual)
#print(total_ventas_ordenadas)  

#--------------
#MAYORES Y MENORES VENTAS POR PRODUCTO-----
#----------

#------MAS VENDIDOS------

#Quita las ventas que son 0, las que son 1 y las que son 2
total_ventas_hechas=[]
for total in total_ventas_ordenadas:
  if total[2]!=0 and total[2]!=1 and total[2]!=2:
    total_ventas_hechas.append(total)

#print(total_ventas_hechas)
#len(total_ventas_hechas) #Sólo 42 productos se vendieron
#Sólo 27 productos se vendieron más de una vez
#Sólo 20 productos se vendieron más de dos veces

#Lista ordenada de más vendido (50 ventas) a menos vendidos (2 ventas)
mas_vendidos=list(reversed(total_ventas_hechas))
#print(mas_vendidos)
#len(mas_vendidos)=20
if int(opcion)==1:
  
#Muestra los 20 productos "más vendidos" (con 3 o más ventas)
  print("\n**VENTAS POR PRODUCTO**\n")
  print("\n**PRODUCTOS MÁS VENDIDOS**\n")
  for mas_vendido in mas_vendidos:
    print("El producto ", mas_vendido[0], ": ", mas_vendido[1], "se vendió ", mas_vendido[2], "veces.\n")


#-----------------
##MENOS VENDIDOS
#-----------

#Lista ordenada de menos vendidos (0 ventas a 2 ventas)

menos_vendidos=[]
for no_ventas in total_ventas_ordenadas:
  if no_ventas[2]==1 or no_ventas[2]==2:
    menos_vendidos.append(no_ventas)
#print(menos_vendidos)
#len(menos_vendidos) 
#productos vendidos 0 veces o 1 o 2 son 76

#rezagados es una lista de 54 elementos con los productos que no se vendieron
rezagados=[]
for rezagado in total_ventas_ordenadas:
  if rezagado[2]==0:
   rezagados.append(rezagado)

if int(opcion)==3:
  print("\n***PRODUCTOS MENOS VENDIDOS***\n")
  for menos_vendido in menos_vendidos:
    if menos_vendido[2]==1:
      print("El producto ", menos_vendido[0], ": ", menos_vendido[1], "se vendió ", menos_vendido[2], "vez.\n")
    else:
      print("El producto ", menos_vendido[0], ": ", menos_vendido[1], "se vendió ", menos_vendido[2], "veces.\n")
  print("\n***PRODUCTOS REZAGADOS***\n")
  for rezagado in rezagados:
    print("El producto ", rezagado[0], ": ", rezagado[1], "NO se vendió.\n")

#------VENTAS POR CATEGORÍA

##ORDENA VENTAS POR CATEGORIAS
#categorias=[nombre categoria]
categorias=[[lifestore_products[0][3]]]
for producto in lifestore_products:
  contador_c=0
  for categoria in categorias:
    if categoria[0]==producto[3]:
      contador_c=1
  if contador_c==0:
    categorias.append([producto[3]])

#Suma las ventas hechas de acuerdo a la categoría
for categoria in categorias:
  suma_cat=0
  for producto in total_ventas_ordenadas:
    for productocatalogo in lifestore_products:
      if producto[0]==productocatalogo[0] and productocatalogo[3]==categoria[0]:
        suma_cat+=producto[2]
  categoria.append(suma_cat)
#categorias=[categoria,ventas por categoria]

#-----------

##---MAYORES Y MENORES VENTAS POR CATEGORÍA
#-------------------

##ordena por el número de ventas de menor a mayor
ventas_ordenadas_cat=[]
while categorias:
  minimo_cat=categorias[0][1]
  lista_ventas_cat=categorias[0]
  for cuenta_ventas_cat in categorias:
    if cuenta_ventas_cat[1] < minimo_cat:
      minimo_cat=cuenta_ventas_cat[1]
      lista_ventas_cat=cuenta_ventas_cat
  ventas_ordenadas_cat.append(lista_ventas_cat)
  categorias.remove(lista_ventas_cat)

len(ventas_ordenadas_cat)

peores_ventas_cat=ventas_ordenadas_cat[0:4]
mejores_ventas_cat=list(reversed(ventas_ordenadas_cat))

mejores_cat=mejores_ventas_cat[0:4]
if int(opcion)==1:
  print("\n**VENTAS POR CATEGORÍAS**\n")
  print("Las categorías más vendidas fueron:\n")
  for mejor_cat in mejores_cat:
    print(" ",mejor_cat[0], "con",mejor_cat[1],"ventas registradas.")
if int(opcion)==3:  
  print("\nLas categorías menos vendidas fueron:\n")
  for peor_cat in peores_ventas_cat:
    if peor_cat[1]!=1:
      print(" ", peor_cat[0], "con",peor_cat[1],"ventas registradas.")
    else:
      print(" ",peor_cat[0], "con",peor_cat[1],"venta registrada.")

#------------
##-----------BÚSQUEDAS POR PRODUCTO-------
#-----------

#Crea una lista que ligue el id con el número de búsquedas realizadas
contadorb=0
total_busquedas=[] #[[id, nombre, contador],[id2, nombre2, contador2]]
for productob in lifestore_products:
  for busqueda in lifestore_searches:
    if productob[0]==busqueda[1]:
      contadorb+=1
      
  formato_idealb=[productob[0],productob[1],contadorb]
  total_busquedas.append(formato_idealb)
  contadorb=0
#total_busquedas está ordenada de menor a mayor por id

##ordena por el número de búsquedas de menor a mayor
total_busquedas_ordenadas=[] #[[id, producto, # de busquedas],[]]
while total_busquedas:
  minimob=total_busquedas[0][2]
  lista_actualb=total_busquedas[0]
  for cuenta_busqueda in total_busquedas:
    if cuenta_busqueda[2] < minimob:
      minimob=cuenta_busqueda[2]
      lista_actualb=cuenta_busqueda
  total_busquedas_ordenadas.append(lista_actualb)
  total_busquedas.remove(lista_actualb)
#print(total_busquedas_ordenadas)  
#len(total_busquedas_ordenadas) 
#96 productos ordenados desde 0 hasta 263 búsquedas

#---------
##------MAYORES BÚSQUEDAS POR PRODUCTO-----
#--------

#Quita las búsquedas que son menores que 10
#total_busquedas_hechas es una lista ordenada de productos con 10 búsquedas hasta 263 búsquedas
total_busquedas_hechas=[]
for total in total_busquedas_ordenadas:
  if total[2]>=10:
    total_busquedas_hechas.append(total)
#print(total_busquedas_hechas)
#len(total_busquedas_hechas) #Sólo 27 productos se buscaron 10 o más veces

#Lista ordenada de más buscados (263 búsquedas) a menos buscados(10)
mas_buscados=list(reversed(total_busquedas_hechas))
#print(mas_buscados)
#27 productos más buscados

#Muestra los 27 productos "más vendidos" (con 10 o más búsquedas)
if int(opcion)==2:
  print("\n**BÚSQUEDAS POR PRODUCTO**\n")
  print("\n**PRODUCTOS CON MÁS BÚSQUEDAS**\n")
  for mas_buscado in mas_buscados:
    print("El producto ", mas_buscado[0], ": ", mas_buscado[1], "se buscó ", mas_buscado[2], "veces.\n")

#------------
##------MENORES BÚSQUEDAS POR PRODUCTO----
#----------------------------

#Lista ordenada de menos BÚSQUEDAS (0 a 7 búsquedas)
menos_buscados=[]
for no_buscados in total_busquedas_ordenadas:
  if no_buscados[2]<10:
    menos_buscados.append(no_buscados)
#print(menos_buscados)
#len(menos_buscados) 
#productos buscados menos de 10 veces son 69

#Muestra lista ordenada con los productos menos buscados (de 0 a 7 búsquedas)
if int(opcion)==4:
  print("\n**PRODUCTOS CON MENOS BÚSQUEDAS**\n")
  for menos_buscado in menos_buscados:
    if menos_buscado[2]==0:
      print("El producto ", menos_buscado[0], ": ", menos_buscado[1], "NO se buscó.\n")
    elif menos_buscado[2]==1:
      print("El producto ", menos_buscado[0], ": ", menos_buscado[1], "se buscó ", menos_buscado[2], "vez.\n")
    else:
      print("El producto ", menos_buscado[0], ": ", menos_buscado[1], "se buscó ", menos_buscado[2], "veces.\n")

#-----------
##BÚSQUEDAS POR CATEGORÍA
#-----------

#Crea una lista que ligue el id con el número de búsquedas realizadas
contador_b=0
busquedas=[] #[[id, contador],[id2, contador2]]
for productob in lifestore_products:
  for busqueda in lifestore_searches:
    if productob[0]==busqueda[1]:
      contador_b+=1
      
  formato_bus=[productob[0],contador_b]
  busquedas.append(formato_bus)
  contador_b=0
#busquedas está ordenada de menor a mayor por id

#Extrae los nombres de las categorías
categorias_b=[[lifestore_products[0][3]]]
for producto in lifestore_products:
  contador_bus=0
  for categoria in categorias_b:
    if categoria[0]==producto[3]:
      contador_bus=1
  if contador_bus==0:
    categorias_b.append([producto[3]])

#Suma las búsquedas por categoría
for categoria in categorias_b:
  suma_cat=0
  for busq in busquedas:
    for productocatalogo in lifestore_products:
      if busq[0]==productocatalogo[0] and productocatalogo[3]==categoria[0]:
        suma_cat+=busq[1]
  categoria.append(suma_cat)
#categorias_b=[categoria,busquedas por categoria]

##ordena por el número de búsquedas de menor a mayor
busquedas_ordenadas_cat=[] #[[id, producto, # de busquedas],[]]
while categorias_b:
  minimob_cat=categorias_b[0][1]
  lista_bus=categorias_b[0]
  for cuentab_cat in categorias_b:
    if cuentab_cat[1] < minimob_cat:
      minimob_cat=cuentab_cat[1]
      lista_bus=cuentab_cat
  busquedas_ordenadas_cat.append(lista_bus)
  categorias_b.remove(lista_bus)
#print(busquedas_ordenadas_cat)  

peores_busquedas=busquedas_ordenadas_cat[0:4]
orden_busquedas=list(reversed(busquedas_ordenadas_cat))
mejores_busquedas=orden_busquedas[0:4]
if int(opcion)==2:
  print("\n**BÚSQUEDAS POR CATEGORÍA**\n")
  print("\n Las categorías más buscadas fueron: \n")
  for mejor_b in mejores_busquedas:
    print(" *",mejor_b[0],"con",mejor_b[1],"búsquedas registradas.\n")
if int(opcion)==4:
  print("\n Las categorías menos buscadas fueron: \n")
  for peor_b in peores_busquedas:
    print(" *",peor_b[0],"con",peor_b[1],"búsquedas registradas.\n")

#-------------------------

##---------RESEÑAS----------
#--------------------------

#Extrae el id, reseña y devolución y tiene 283 elementos
reseñas=[]
for venta in lifestore_sales:
  formato_reseñas=[venta[1], venta[2],venta[4]]
  reseñas.append(formato_reseñas)
#print(reseñas)
#reseñas=[[id, reseña, devolución]]

## reseña_porp=[id, nombre, suma reseñas, # de reseñas, devolución]
contador_res = 0
suma = 0
sumadev = 0
reseña_porp = []
for producto in lifestore_products:
    for reseña in reseñas:
        if producto[0] == reseña[0]:  ##Liga el id on el nombre
            contador_res += 1
            suma = suma + reseña[1]
            sumadev = reseña[2]+sumadev
    formato_nuevo = [producto[0], producto[1], suma, contador_res, sumadev]
    reseña_porp.append(formato_nuevo)
    contador_res = 0
    suma = 0
    sumadev = 0
#print(reseña_porp)
#reseña_porp=[id, nombre, suma reseñas, # de reseñas, devolución]

##Checar si los productos marcados como devueltos están bn
# devoluciones=[]
# for res_porp in reseña_porp:
#   if res_porp[4]==1:
#     formato_dev=[res_porp[0],res_porp[1],res_porp[4]]
#     devoluciones.append(formato_dev)

# print(devoluciones)


#PROMEDIO RESEÑAS
#reseña_porp=[id, nombre, suma reseñas, # de reseñas, devolución]
promedio_res=0
reseñas_promedios=[]
for cada_producto in reseña_porp:
  if cada_producto[2]!=0:
    promedio_res=cada_producto[2]/cada_producto[3]
  else:
    promedio_res=0

  formato_promedios=[cada_producto[0],cada_producto[1],promedio_res,cada_producto[4]]
  reseñas_promedios.append(formato_promedios)
  promedio_res=0
#print(reseñas_promedios) 
#reseñas_promedios=[[id, nombre, promedio_reseña, devolución]]

##ORDENAR RESEÑAS POR PROMEDIO

#Ordena por reseña (de menor a mayor)
reseñas_ordenadas=[]
while reseñas_promedios:
  minimor=reseñas_promedios[0][2]
  lista_actual_res=reseñas_promedios[0]
  for reseña_prom in reseñas_promedios:
    if reseña_prom[2]<minimor:
      minimor=reseña_prom[2]
      lista_actual_res=reseña_prom
  reseñas_ordenadas.append(lista_actual_res)
  reseñas_promedios.remove(lista_actual_res)
#print(reseñas_ordenadas)
#total_reseñas_ordenadas ordena de menor a mayor
#reseñas_ordenadas=[[id, nombre, reseña, devolucion]]

#Lista ordenada de mejores a peores reseñas
nuevo_orden_reseñas=list(reversed(reseñas_ordenadas))
#print(nuevo_orden_reseñas)

#Muestra las mejores 20 reseñas
mejores_reseñas=nuevo_orden_reseñas[0:20]
#print(mejores_reseñas)
#mejores_reseñas=[[id, nombre,promedio reseña, devolución]]

#Productos con peores reseñas que SÍ se vendieron
peores_reseñas=[]
for peores in reseñas_ordenadas:
  if peores[2]>0 and peores[2]<5:
    formato_peores=[peores[0],peores[1],peores[2],peores[3]]
    peores_reseñas.append(formato_peores)
#print(peores_reseñas)

#20 productos con peores reseñas que SÍ se vendieron
peores_20=peores_reseñas[0:20]
#print(peores_20)
#peores_20=[[id, nombre, reseña promedio, devolucion]]
if int(opcion)==5 or continuar=="Sí":
  print("\n**RESEÑAS**\n")
  print("\n**20 PRODUCTOS CON MEJORES RESEÑAS**\n")
  for mejor_producto in mejores_reseñas:
    #print(mejor_producto[3]) #Ninguno fue devuelto
    if mejor_producto[3]==0:
      print("El producto ", mejor_producto[0], ":",mejor_producto[1], "tiene reseña promedio de: ", mejor_producto[2],"\n")
    else:
      print("El producto ", mejor_producto[0], ":",mejor_producto[1], "tiene reseña promedio de: ", mejor_producto[2], "pero fue devuelto.")

  ##QUIERO LIGAR ESTO CON EL # DE VENTAS

  print("\n**20 PRODUCTOS CON PEORES RESEÑAS**\n")
  for peor_producto in peores_20:
    #print(peor_producto[3]) #Ninguno fue devuelto
    if peor_producto[3]==0:
      print("El producto ", peor_producto[0], ":",peor_producto[1], "tiene reseña promedio de: ", peor_producto[2],"\n")
    else:
      print("El producto ", peor_producto[0], ":",peor_producto[1], "tiene reseña promedio de: ", peor_producto[2], "y tuvo devoluciones.\n")

##QUIERO LIGAR ESTO CON EL # DE VENTAS


##------HASTA AQUI TODO BN



##VENTAS ANUALES Y MENSUALES
"""
lifestore-sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore-products = [id_product, name, price, category, stock]
"""
##---------------
##ESTO SE PUEDE HACER MENOSSSS

#Sacar sólo id y fechas de todas las ventas

ventas_simples=[]
for venta_producto in lifestore_sales:
  formato_venta_simple=[venta_producto[1],venta_producto[3]]
  ventas_simples.append(formato_venta_simple)

#print(ventas_simples)
#len(ventas_simples) #se hicieron 283 ventas

#Sacar id y fechas de todo 2020
ventas_2020=[]
for venta_simple in ventas_simples:
  if venta_simple[1][6:10]=="2020":
    formato_venta_2020=[venta_simple[0],venta_simple[1]]
    ventas_2020.append(formato_venta_2020)

#print(ventas_2020)
#len(ventas_2020) #Se hicieron 281 ventas

for product in lifestore_products:
  for ventas in ventas_2020:
    if ventas[0] == product[0]:
      ventas.append(product[2])

#ventas_2020(id,fecha,precio)
#len(ventas_2020) #Se hicieron 281 ventas


ventas_mensuales2020 = []
meses = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

#Crea lista de listas (mensuales) de productos vendidos
j=0
for mes in meses:
  k=0
  for venta_mes in ventas_2020:
    if venta_mes[1][3:5] == mes:
      formato_mes = [venta_mes[0], venta_mes[1],venta_mes[2]]
      if k==0:
        ventas_mensuales2020.append([formato_mes])
      if k>0:
        ventas_mensuales2020[j].append(formato_mes)
      k=k+1
  j+=1
#ventas_mensuales2020=[[[id, fecha, precio]]]

meseslargos=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]


#Lista de productos devueltos en 2020
devoluciones2020 = [] 
for sales in lifestore_sales:
    if sales[3][6:10] == "2020" and sales[4] != 0:
        devoluciones2020.append([sales[1], sales[3], sales[4]])
#print(devoluciones2020)
#devoluciones2020=[id, fecha de compra]

#Crea lista de listas (mensuales) de productos devueltos
j = 0
devoluciones_mensuales2020 = []
for mes in meses:
    i = 0
    for devoluciones in devoluciones2020:
        if devoluciones[1][3:5] == mes:
            formato_mes = [devoluciones[0], devoluciones[1]]
            if i == 0:
                devoluciones_mensuales2020.append([formato_mes])
            if i > 0:
                devoluciones_mensuales2020[j].append(formato_mes)
            i = i + 1
    j += 1
#print(devoluciones_mensuales2020)
#devoluciones_mensuales2020=[[[id(mes1), fecha(mes1)]][[id(mes2),fecha(mes2)]]]
if int(opcion)==6:
  print("\n**VENTAS PROMEDIO MENSUALES**\n")
  for mes in ventas_mensuales2020:
    contadori=0
    for mes_dev in devoluciones_mensuales2020:
      mesnumero = int(mes[0][1][3:5])
      mesnumero_dev = int(mes_dev[0][1][3:5])
      if mesnumero==mesnumero_dev:
        contadori=1
        #Si se presentó una venta y una devolución
        if str(len(mes)) == "1" and str(len(mes_dev))=="1":
            print("Se realizó",len(mes), "venta en", meseslargos[mesnumero-1], ". Así, el promedio fue de", round(len(mes)/30,3), "ventas por día. Sin embargo, se presentó",len(mes_dev),"devolución.\n")
            break
        else:
          #Si se presentó más de una venta y una devolución
          if (mesnumero==1 or mesnumero==3 or mesnumero==5 or mesnumero==7 or mesnumero==8) and str(len(mes_dev))=="1":
            print("Se realizaron", len(mes), "ventas en", meseslargos[mesnumero-1], ". Así, el promedio fue de", round(len(mes)/31,3), "ventas por día. Sin embargo, se presentó",len(mes_dev),"devolución.\n")
          #Si se presentó más de una venta y más de una devolución
          elif (mesnumero==1 or mesnumero==3  or mesnumero==5 or mesnumero==7 or mesnumero==8) and str(len(mes_dev))!="1":
            print("Se realizaron", len(mes), "ventas en", meseslargos[mesnumero-1], ". Así, el promedio fue de", round(len(mes)/31,3), "ventas por día. Sin embargo, se presentaron",len(mes_dev),"devoluciones.\n")
            break
          #CASO FREBRERO BISIESTO
          elif mesnumero==2:
            if mesnumero==2 and str(len(mes_dev))=="1":
              print("Se realizaron", len(mes), "ventas en", meseslargos[mesnumero-1], ". Así, el promedio fue de", round(len(mes)/29,3), "ventas por día. Sin embargo, se presentó",len(mes_dev),"devolución.\n")
            else:
              print("Se realizaron", len(mes), "ventas en", meseslargos[mesnumero-1], ". Así, el promedio fue de", round(len(mes)/29,3), "ventas por día. Sin embargo, se presentaron",len(mes_dev),"devoluciones.\n")
              break
          else:
            print("Se realizaron", len(mes), "ventas en", meseslargos[mesnumero-1], ". Así, el promedio fue de", round(len(mes)/30,3), "ventas por día. Sin embargo, se presentaron", len(mes_dev),"devoluciones.\n")
            break
    if contadori==0:
        print("Se realizaron", len(mes), "ventas en", meseslargos[mesnumero-1], ". Así, el promedio fue de", round(len(mes)/30,3), "ventas por día.\n")

    
##-------------
##--------INGRESOS---------
#-----------------

sumas_mensuales=[]
for mes in ventas_mensuales2020: #elige la sublista de un solo mes
  #ventas_mensuales2020=[[[id, fecha,precio]]]
  mesnumero = int(mes[0][1][3:5]) #Busca el mes dentro de la lista [[[]]]
  suma=0
  for importeporventa in mes: #elige la sublista de la venta de un producto en determinado mes
    suma+=importeporventa[2] #elige el precio de la venta
  sumas_mensuales.append(suma)

for mes in devoluciones_mensuales2020:
  mesnumero = int(mes[0][1][3:5])
  suma=0
  for dev in mes:
    for producto in lifestore_products:
      if dev[0]==producto[0]:
        suma+=producto[2]
  sumas_mensuales[mesnumero-1]-=suma
if int(opcion)==6:
  print("\n**INGRESOS MENSUALES**\n")
  suma_anual=0
  for suma_mensual in sumas_mensuales:
    suma_anual=suma_anual+suma_mensual
  print("Con lo anterior, considerando las ventas y devoluciones mensuales, tenemos que: \n")

  for mes in ventas_mensuales2020:
      mesnumero = int(mes[0][1][3:5])
      print("El ingreso bruto para el mes de:",meseslargos[mesnumero-1], "fue de: $", sumas_mensuales[mesnumero-1],".\n")

  print("\n**INGRESO ANUAL**\n")    
  print("Con corte al 5 de septiembre de 2020, el INGRESO TOTAL ANUAL fue de: $",suma_anual,". Así, el INGRESO MENSUAL PROMEDIO fue de: $", round(suma_anual/(8+(5/30)),3))
#Sólo consideramos 5 días de septiembre


##PROBLEMA TRIMESTRAL

#ORDENA VENTAS POR PRODUCTO
contador=0
total_ventas=[] #[[id, nombre, contador],[id2, nombre2, contador2]]
for producto in lifestore_products:
  for venta in lifestore_sales:
    if producto[0]==venta[1] and str(venta[3][6:10])=="2020":
      contador+=1     
  formato_ideal=[producto[0],producto[1],contador]
  total_ventas.append(formato_ideal)
  contador=0

##ordena por el número de ventas de menor a mayor
total_ventas_ordenadas=[]
while total_ventas:
  minimo=total_ventas[0][2]
  lista_actual=total_ventas[0]
  for cuenta_ventas in total_ventas:
    if cuenta_ventas[2] < minimo:
      minimo=cuenta_ventas[2]
      lista_actual=cuenta_ventas
  total_ventas_ordenadas.append(lista_actual)
  total_ventas.remove(lista_actual)
#print(total_ventas_ordenadas)  

categorias=[[lifestore_products[0][3]]]
for producto in lifestore_products:
  k=0
  for categoria in categorias:
    if categoria[0]==producto[3]:
      k=1
  if k==0:
    categorias.append([producto[3]])

for categoria in categorias:
  suma=0
  for producto in total_ventas_ordenadas:
    for productocatalogo in lifestore_products:
      if producto[0]==productocatalogo[0] and productocatalogo[3]==categoria[0]:
        suma+=producto[2]
  categoria.append(suma)
  
for categoria in categorias:
  suma=0
  for producto in total_busquedas_ordenadas:
    for productocatalogo in lifestore_products:
      if producto[0]==productocatalogo[0] and productocatalogo[3]==categoria[0]:
        suma+=producto[2]
  categoria.append(suma)



CategoriasT1=[]
for i in categorias:
  suma=0
  
  for ventas in lifestore_sales:
    for producto in lifestore_products:
      if int(ventas[3][3:5])<=3 and ventas[1]==producto[0] and producto[3]==i[0] and str(ventas[3][6:10])=="2020":
        if ventas[4]==0:
          suma+=producto[2]
  CategoriasT1.append([i[0],suma])

CategoriasT2=[]
for i in categorias:
  suma=0
  for ventas in lifestore_sales:
    for producto in lifestore_products:
      if 3<int(ventas[3][3:5])<=6 and ventas[1]==producto[0] and producto[3]==i[0] and str(ventas[3][6:10])=="2020":
        if ventas[4]==0:
          suma+=producto[2]
  CategoriasT2.append([i[0],suma])

CategoriasT3=[]
for i in categorias:
  suma=0
  for ventas in lifestore_sales:
    for producto in lifestore_products:
      if 6<int(ventas[3][3:5])<=9 and ventas[1]==producto[0] and producto[3]==i[0] and str(ventas[3][6:10])=="2020":
        if ventas[4]==0:
          suma+=producto[2]
  CategoriasT3.append([i[0],suma])

"""
for i in range(len(categorias)):
  sumaporcatego=(CategoriasT1[i][1]+CategoriasT2[i][1]+CategoriasT3[i][1])
  promedio=sumaporcatego/categorias[i][1]
  categorias[i].append(sumaporcatego)
  categorias[i].append(promedio)
print(categorias)

"""



#Ordenar ingresos por categoría en trimestre 1
ingresos_catt1=[]
while CategoriasT1:
  minimo_t1=CategoriasT1[0][1]
  lista_t1=CategoriasT1[0]
  for cuenta_catt1 in CategoriasT1:
    if cuenta_catt1[1] < minimo_t1:
      minimo_t1=cuenta_catt1[1]
      lista_t1=cuenta_catt1
  ingresos_catt1.append(lista_t1)
  CategoriasT1.remove(lista_t1)

#Ordenar ingresos por categoría en trimestre 2
ingresos_catt2=[]
while CategoriasT2:
  minimo_t2=CategoriasT2[0][1]
  lista_t2=CategoriasT2[0]
  for cuenta_catt2 in CategoriasT2:
    if cuenta_catt2[1] < minimo_t2:
      minimo_t2=cuenta_catt2[1]
      lista_t2=cuenta_catt2
  ingresos_catt2.append(lista_t2)
  CategoriasT2.remove(lista_t2)

#Ordenar ingresos por categoría en trimestre 3
ingresos_catt3=[]
while CategoriasT3:
  minimo_t3=CategoriasT3[0][1]
  lista_t3=CategoriasT3[0]
  for cuenta_catt3 in CategoriasT3:
    if cuenta_catt3[1] < minimo_t3:
      minimo_t3=cuenta_catt3[1]
      lista_t3=cuenta_catt3
  ingresos_catt3.append(lista_t3)
  CategoriasT3.remove(lista_t3)
if int(opcion)==6:
  print("\n**INGRESOS POR CATEGORÍA TRIMESTRALES**\n")
  print("\nEn el trimestre 1, los ingresos por categoría fueron los siguientes:\n")
  for ingreso_catt1 in ingresos_catt1:
    print(" *", ingreso_catt1[0], "obtuvo ingresos de $",ingreso_catt1[1])
  print("\nEn el trimestre 2, los ingresos por categoría fueron los siguientes:\n")
  for ingreso_catt2 in ingresos_catt2:
    print(" *", ingreso_catt2[0], "obtuvo ingresos de $",ingreso_catt2[1])
  print("\nEn el trimestre 3, los ingresos por categoría fueron los siguientes:\n")
  for ingreso_catt3 in ingresos_catt3:
    print(" *", ingreso_catt3[0], "obtuvo ingresos de $",ingreso_catt3[1])



"""
    lifestore-products = [id_product, name, price, category, stock]
  
"""

stock_por_categorias=[]
for i in categorias:
  suma=0
  for producto in lifestore_products:
    if producto[3]==i[0]:
      suma+=producto[4]
  stock_por_categorias.append([i[0],suma])

#stock_por_categorias (categoria,stock)
#ayuda a comparar el stock disponible con las ventas realizadas durante el año. El caso ideal es tener stock considerable para las categorías más vendidas y poco para las menos solicitadas.