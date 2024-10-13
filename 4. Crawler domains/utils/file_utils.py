def leer_dominios(archivo):
    """ Leer archivo de dominios .txt"""
    try:
        with open(archivo, "r") as f:
            dominios = f.read().splitlines()
        return dominios
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe.")
        return []
    
def guardar_resultado(urls, archivo_salida):
    """ Guardar los dominios en un archivo de salida"""
    with open(archivo_salida, "w") as f:
        for url in sorted(urls):
            f.write(url + "\n")
    print(f"Resultados guardados en {archivo_salida}")