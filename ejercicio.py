# Ingrese una lista de compras: manzanas, plátanos, leche, pan
# Los productos en la lista de compras son: ['manzanas', 'plátanos', 'leche', 'pan']

# compras = input("Ingrese una lista de compras: ")
# productos = compras.split(", ")
productos=['manzanas', 'plátanos', 'leche', 'pan']
print(f"Los productos en la lista de compras son: {productos}")

# Convertir la lista de compras en una tupla
def convertir_lista_a_tupla(lista):
    tupla_productos = tuple(lista)
    return tupla_productos