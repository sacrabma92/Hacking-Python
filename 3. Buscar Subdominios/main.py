import argparse # Importar librería para manejo de argumentos
from tools.subfinder import ejecutar_subfinder
from tools.sublister import ejectuar_sublister
from utils.file_utils import leer_dominios, guardar_subdominios

def buscar_subdominios(archivo_dominios):
    # Leer los dominos desde el archivo
    dominios = leer_dominios(archivo_dominios)

    # Procesar cada dominio
    for dominio in dominios:
        subdominios_sublister = ejectuar_sublister(dominio)
        subdominios_subfinder = ejecutar_subfinder(dominio)

        # Combinar y eliminar duplicados
        subdominos_totales = set(subdominios_sublister + subdominios_subfinder)

        # Guardar los resultados en un archivo
        guardar_subdominios(dominio, subdominos_totales)

        # Imprimir resultados en consola
        print(f"Subdominios encontrados para {dominio}:")
        print("\n".join(subdominos_totales))
        print('-' * 40)

# Ejecutar programa principal
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Buscar subdominios utilizando múltiples herramientas.")
    parser.add_argument("archivo", help="El archivo que contiene los dominios principales (.txt)")
    
    args = parser.parse_args()
    buscar_subdominios(args.archivo)