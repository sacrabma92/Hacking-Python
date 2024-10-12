import subprocess
from utils.filter_utils import filtrar_subdominios

def ejecutar_crt(domain):
    try:
        # Ejecutamos sublist3r y guardamos el resultado en un archivo
        print(f"Ejecutando crt.sh para {domain}")
        # Ejecutamos sublist3r y guardamos el resultado en un archivo
        resultado = subprocess.run(['crt.sh', '-d', domain], capture_output=True, text=True)

        # Si el comando no se ejecutó correctamente, mostramos un mensaje de error
        if resultado.returncode != 0:
            print(f"Error al ejecutar crt: {resultado.stderr}")
        # Si el comando se ejecutó correctamente, leemos el archivo con los resultados
        return filtrar_subdominios(resultado.stdout)
    
    except subprocess.CalledProcessError as e:
        print(e)