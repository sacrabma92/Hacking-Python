# install_tools.py

import subprocess
import os
from color import Colors

# Función para verificar si una herramienta ya está instalada
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
            print(f"Tipo de instalación no soportado para {tool_name}.")
            return
        
        if result.returncode == 0:
            print(f"{Colors.GREEN}{tool_name} instalado con éxito.{Colors.RESET}")
        else:
            print(f"{Colors.RED}Error al instalar {tool_name}.{Colors.RESET}")

# Función para copiar los binarios de Go a /usr/local/bin
def copy_binaries():
    go_bin_path = os.path.expanduser("~/go/bin")

    if os.path.exists(go_bin_path):
        print("Copiando los binarios de Go a /usr/local/bin...")
        result = subprocess.run(f"sudo cp {go_bin_path}/* /usr/local/bin", shell=True)
        if result.returncode == 0:
            print("Binarios de Go copiados con éxito.")
        else:
            print("Error al copiar los binarios de Go.")
    else:
        print("No se encontraron binarios de Go para copiar.")

# Función para instalar Nuclei y clonar sus plantillas
def install_nuclei():
    if not os.path.exists("/root/nuclei-templates"):
        print("Instalando Nuclei y clonando sus plantillas...")
        result = subprocess.run("go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest", shell=True)
        
        if result.returncode == 0:
            print(f"{Colors.GREEN}Nuclei instalado con éxito.{Colors.RESET}")
            subprocess.run("git clone https://github.com/projectdiscovery/nuclei-templates /root/nuclei-templates", shell=True)
            print("Plantillas de Nuclei clonadas con éxito.")
        else:
            print(f"{Colors.RED}Error al instalar Nuclei.{Colors.RESET}")
    else:
        print(f"{Colors.GREEN}Las plantillas de Nuclei ya están clonadas.{Colors.RESET}")

# Función para instalar Corsy
def install_corsy():
    if not os.path.exists("/root/Corsy"):
        print("Instalando Corsy...")
        result = subprocess.run("git clone https://github.com/s0md3v/Corsy.git", shell=True)
        
        if result.returncode == 0:
            print("Corsy clonado con éxito.")
            subprocess.run("sudo mv Corsy /root/Corsy", shell=True)
            subprocess.run("pip3 install requests", shell=True)
            print(f"{Colors.GREEN}Corsy instalado con éxito.{Colors.RESET}")
        else:
            print(f"{Colors.RED}Error al clonar Corsy.{Colors.RESET}")
    else:
        print(f"{Colors.GREEN}Corsy ya está instalado.{Colors.RESET}")

# Función para instalar GF
def install_gf():
    print("Instalando GF...")
    result = subprocess.run("go install github.com/tomnomnom/gf@latest", shell=True)
    
    if result.returncode == 0:
        print(f"{Colors.GREEN}GF instalado con éxito.{Colors.RESET}")
        subprocess.run("sudo mv ~/go/bin/gf /usr/local/bin", shell=True)
        
        if not os.path.exists(os.path.expanduser("~/.gf")):
            os.makedirs(os.path.expanduser("~/.gf"), exist_ok=True)
        
        # Copiar ejemplos a ~/.gf
        subprocess.run("sudo cp ~/go/pkg/mod/github.com/tomnomnom/gf@v0.0.0-20200618134122-dcd4c361f9f5/examples/* ~/.gf", shell=True)
        subprocess.run("git clone https://github.com/1ndianl33t/Gf-Patterns", shell=True)
        subprocess.run("cp Gf-Patterns/* ~/.gf/", shell=True)
        print("GF instalado y configurado con éxito.")
    else:
        print(f"{Colors.RED}Error al instalar GF.{Colors.RESET}")

# Función principal que instala todas las herramientas
def install_tools(tools):
    for tool_name, tool_info in tools.items():
        install_tool(tool_name, tool_info)
    # Instalar Nuclei y clonar sus plantillas
    install_nuclei()
    # Instalar Corsy
    install_corsy()
    # Instalar GF
    install_gf()
    # Copiar los binarios de Go una vez instaladas las herramientas
    copy_binaries()