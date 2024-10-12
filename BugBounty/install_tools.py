#Install_tools.py
import subprocess
import os
from color import Colors

#Función para verificar si una herramienta ya está instalada
def is_installed(tool):
    result = subprocess.run(f"which {tool}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

# Función para instalar una herramienta
def install_tool(tool_name, tool_info):
    if is_installed(tool_name):
        print(f"{Colors.GREEN}{tool_name} ya está instalada.{Colors.RESET}")
    else:
        print(f"Instalando {tool_name}...")

        if tool_info["type"] == "go":
            result = subprocess.run(tool_info["command"], shell=True)
        elif tool_info["type"] == "apt":
            result = subprocess.run(tool_info["command"], shell=True)
        else:
            print(f"Tipo de instalación no soportada para {tool_name}.")
            return
        
        if result.returncode == 0:
            print(f"{Colors.GREEN}{tool_name} instalado con éxito.{Colors.RESET}")
        else:
            print(f"{Colors.RED}Error al instalar {tool_name}.{Colors.RESET}")
        
# Función para copiar los binarios de Go a /usr/local/bin
def copy_binaries():
    go_bin_path = os.path.expanduser("~/go/bin")

    if os.path.exists(go_bin_path):
        print("Copiado los binarios de Go a /usr/local/bin...")
        result = subprocess.run(f"sudo cp {go_bin_path}/* /usr/local/bin", shell=True)
        if result.returncode == 0:
            print("Binarios de Go copiados con éxito.")
        else:
            print("Error al copiar los binarios de Go.")
    else:
        print("No se encontraron binario de Go para copiar.")

# Función principal que instala todas las herramientas
def install_tools(tools):
    for tool_name, tool_info in tools.items():
        install_tool(tool_name, tool_info)
    # Copiar los binario de Go una vez instaladas las herramientas
    copy_binaries()