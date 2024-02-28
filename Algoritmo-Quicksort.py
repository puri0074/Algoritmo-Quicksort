def quicksort(arr):
    # Paso base: Verificar si la lista es de longitud 1 o menos 
    if len(arr) <= 1:
        return arr

    # Elegimos un pivote (En este caso, el primer elemento)
    pivot = arr[0]

    # Dividimos la lista en dos partes, menores o iguales al pivote y mayores al pivote 
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    # Aplicamos recursivamente Quicksort a ambas partes y combinamos los resultados
    return quicksort(less) + [pivot] + quicksort(greater)

# Ejemplo de uso 
mi_lista = [3, 6, 8, 10, 1, 2, 1]
resultado = quicksort(mi_lista)
print("Lista original:", mi_lista)
print("Lista Ordenada:", resultado)