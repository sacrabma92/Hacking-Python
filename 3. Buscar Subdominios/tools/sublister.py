import subprocess
from utils.filter_utils import filtrar_subdominios

def ejecutar_sublister(domain):
    try:
        # Ejecutamos sublist3r y guardamos el resultado en un archivo
        print(f"Ejecutando sublist3r para {domain}")
        # Ejecutamos sublist3r y guardamos el resultado en un archivo
        resultado = subprocess.run(['sublist3r', '-d', domain], capture_output=True, text=True)

        # Si el comando no se ejecutó correctamente, mostramos un mensaje de error
        if resultado.returncode != 0:
            print(f"Error al ejecutar sublist3r: {resultado.stderr}")
        # Si el comando se ejecutó correctamente, leemos el archivo con los resultados
        return filtrar_subdominios(resultado.stdout)
    
    except subprocess.CalledProcessError as e:
        print(e)