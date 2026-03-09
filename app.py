import pandas as pd 
import os

def agregar_producto(nombre, cantidad, precio):
    archivo = 'inventario.csv'
    nuevo_item = {'Producto': nombre, 'Cantidad': cantidad, 'Precio': precio}

    if not os.path.isfile(archivo):
        df = pd.DataFrame([nuevo_item])
        df.to_csv(archivo, index=False)

    else:
        df = pd.read_csv(archivo)
        df = pd.concat([df, pd.DataFrame([nuevo_item])], ignore_index=True)
        df.to_csv(archivo, index=False)

    print(f"{nombre} guardado con exito.")

print("--- SISTEMA DE INVENTARIO ---")
nombre_prod = input("Nombre del producto: ")
cant_prod = int(input("Cantidad: "))
precio_prod = float(input("Precio: "))

agregar_producto(nombre_prod, cant_prod, precio_prod)