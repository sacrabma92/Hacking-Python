def leer_dominios(archivo):
    """Leer dominios desde un archivo .txt"""
    try:
        with open(archivo, 'r') as f:
            dominios = f.read().splitlines()
        return dominios
    except FileNotFoundError:
        print(f"El archivo {archivo} no fue encontrado.")
        return []

def guardar_subdominios(subdominios, archivo_salida):
    """Guardar los subdominios encontrados en un archivo."""
    with open(archivo_salida, 'w') as f:
        for subdominio in sorted(subdominios):
            f.write(subdominio + '\n')
    
    print(f"Subdominios guardados en {archivo_salida}")
