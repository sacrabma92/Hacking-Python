import subprocess

def ejectuar_sublister(domain):
    try:
        # Ejecutamos sublist3r y guardamos el resultado en un archivo
        print(f"Ejecutando sublist3r para {domain}")
        # Ejecutamos sublist3r y guardamos el resultado en un archivo
        resultado = subprocess.run(['sublist3r', '-d', domain], capture_output=True, text=True)

        # Si el comando no se ejecutó correctamente, mostramos un mensaje de error
        if resultado.returncode != 0:
            print(f"Error al ejecutar sublist3r: {resultado.stderr}")
        # Si el comando se ejecutó correctamente, leemos el archivo con los resultados
        return resultado.stdout.splitlines()
    
    except subprocess.CalledProcessError as e:
        print(e)