areas = ["cuina", 7.88, "menjador", 13.0, "terrassa", 20.34, "lavabo", 6.55, "habitació1", 7.98, "habitació2", 12, "rebedor", 4.23]

# SEGUNDO ELEMENTO
print (areas[1])

# ÚLTIMO ELEMENTO
print (areas[13])

# AREA TERRAZA
print (areas[5])

# PRIMER ELEMENTO A TERCERO
print (areas[0:4])

# TERCER ELEMENTO A ÚLTIMO
print (areas[3:14])

# TOTAL AREA DOS HABITACIONES
print (areas[9]+ areas[11])

# MODIFICAR AREA LAVABO I NUEVA LISTA
areas[7] = [8.89]
print(areas)

# AÑADIR ÁREA PATIO INTERIOR Y 2.78 ÚLTIMA POSICIÓN
areas.append("patio interior") # Append se utiiliza para añadir un elemento a una lista.
areas.append(2.78)
print (areas)