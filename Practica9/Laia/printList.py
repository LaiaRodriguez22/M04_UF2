areas = ["cuina", 7.88, "menjador", 13.0, "terrassa", 20.34,
         "lavabo", 6.55, "habitació1", 7.98, "habitació2", 12, "rebedor", 4.23]

#SEGON element
print(areas[1])

#ULTIM element
print(areas[13])

#area de TERRASSA
print(areas[5])

#del primer element al tercer element
print(areas[0:4])

#del TERCER element al ULTIM element
print(areas[3:14])

#Imprimir el total de l'àrea de les dues habitacions
print(areas[9] + areas[11])

#Modificar l’àrea del lavabo i imprimir la nova list area
areas[7] = 10.00
print(areas)

#Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.
areas.append("pati interior")
areas.append(2.78)
print(areas)
