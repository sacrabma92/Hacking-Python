import argparse
from tools.sublister import ejecutar_sublister
from tools.subfinder import ejecutar_subfinder
from utils.file_utils import leer_dominios, guardar_subdominios

def buscar_subdominios(archivo_dominios, archivo_salida):
    # Leer los dominios desde el archivo proporcionado
    dominios = leer_dominios(archivo_dominios)
    subdominios_totales = set()

    # Procesar cada dominio
    for dominio in dominios:
        print(f"Buscando subdominios para {dominio}...")

        # Ejecutar herramientas y filtrar subdominios
        subdominios_sublister = ejecutar_sublister(dominio)
        subdominios_subfinder = ejecutar_subfinder(dominio)

        # Combinar subdominios encontrados y eliminar duplicados
        subdominios_totales.update(subdominios_sublister)
        subdominios_totales.update(subdominios_subfinder)

    # Guardar todos los subdominios válidos en un solo archivo de salida
    guardar_subdominios(subdominios_totales, archivo_salida)

# Ejecutar el programa principal
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Buscar subdominios utilizando múltiples herramientas.")
    parser.add_argument("archivo", help="El archivo que contiene los dominios principales (.txt)")
    parser.add_argument("salida", help="El archivo de salida para almacenar los subdominios encontrados")
    
    args = parser.parse_args()
    
    buscar_subdominios(args.archivo, args.salida)
