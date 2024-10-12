import argparse
from tools.sublister import ejecutar_sublister
from tools.subfinder import ejecutar_subfinder
from tools.amass import ejecutar_amass
from utils.file_utils import leer_dominios, guardar_subdominios

# Nombre del archivo de salida estático
NOMBRE_ARCHIVO_SALIDA = "subdominios_encontrados.txt"

def buscar_subdominios(entrada):
    # Verificar si la entrada es un archivo o un dominio individual
    if entrada.endswith('.txt'):
        # Leer dominios desde el archivo
        dominios = leer_dominios(entrada)
    else:
        # Si no es un archivo, tratar como un dominio único
        dominios = [entrada]

    subdominios_totales = set()

    # Procesar cada dominio
    for dominio in dominios:
        print(f"Buscando subdominios para {dominio}...")

        # Ejecutar herramientas y filtrar subdominios
        subdominios_sublister = ejecutar_sublister(dominio)
        subdominios_subfinder = ejecutar_subfinder(dominio)
        subdominios_amass = ejecutar_amass(dominio)

        # Combinar subdominios encontrados y eliminar duplicados
        subdominios_totales.update(subdominios_sublister)
        subdominios_totales.update(subdominios_subfinder)
        subdominios_totales.update(subdominios_amass)

    # Guardar todos los subdominios válidos en un solo archivo de salida
    guardar_subdominios(subdominios_totales, NOMBRE_ARCHIVO_SALIDA)

def main():
    parser = argparse.ArgumentParser(description="Buscar subdominios utilizando múltiples herramientas.")
    group = parser.add_mutually_exclusive_group(required=True)
    
    group.add_argument("--dominio", type=str, help="Dominio único a buscar (ejemplo.com)")
    group.add_argument("--archivo", type=str, help="Archivo .txt que contiene la lista de dominios")

    args = parser.parse_args()

    # Elegir la entrada correcta
    if args.dominio:
        buscar_subdominios(args.dominio)
    else:
        buscar_subdominios(args.archivo)

# Ejecutar el programa principal
if __name__ == "__main__":
    main()