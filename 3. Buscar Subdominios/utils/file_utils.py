#
def leer_dominios(archivo):
    """Leer dominios desde un archivo .txt"""
    try:
        with open(archivo, 'r') as f:
            dominios = f.read().splitlines()
        return dominios
    except FileNotFoundError:
        print(f"El archivo {archivo} no fue contrado")
        return []
    
def guardar_subdominios(dominio, subdominios):
    """Guardar subdominios en un archivo .txt"""
    with open(f"{dominio}.txt", 'w') as f:
        for subdominio in subdominios:
            f.write(subdominio + '\n')
    print(f"Subdominios guardados en {dominio}.txt")