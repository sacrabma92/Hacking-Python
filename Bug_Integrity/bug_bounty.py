import argparse

# Definir una función de ejemplo para cada herramienta
def subdomain_enumeration():
    print("Ejecutando Subdomain Enumeration...")

def technology_detection():
    print("Ejecutando Technology Detection...")

def dns_record_scanning():
    print("Ejecutando DNS Record Scanning...")

def web_crawling():
    print("Ejecutando Web Crawling and URL Extraction...")

def favicon_hash_calculation():
    print("Ejecutando Favicon Hash Calculation...")

def host_header_injection_testing():
    print("Ejecutando Host Header Injection Testing...")

def security_header_analysis():
    print("Ejecutando Security Header Analysis...")

def network_vulnerability_analysis():
    print("Ejecutando Network Vulnerability Analysis...")

def wayback_machine_url_retrieval():
    print("Ejecutando Wayback Machine URL Retrieval...")

def javascript_file_discovery():
    print("Ejecutando JavaScript File Discovery...")

def broken_link_checking():
    print("Ejecutando Broken Link Checking...")

def http_request_smuggling_detection():
    print("Ejecutando HTTP Request Smuggling Detection...")

# Mapear nombres de flags a funciones
tool_functions = {
    "subenum": subdomain_enumeration,
    "techdet": technology_detection,
    "dnsscan": dns_record_scanning,
    "crawl": web_crawling,
    "favicon": favicon_hash_calculation,
    "hostinj": host_header_injection_testing,
    "sechead": security_header_analysis,
    "netvuln": network_vulnerability_analysis,
    "wayback": wayback_machine_url_retrieval,
    "jsdiscover": javascript_file_discovery,
    "linkchk": broken_link_checking,
    "httpsmug": http_request_smuggling_detection,
    # Agregar el resto de funciones según tus necesidades
}

def main():
    parser = argparse.ArgumentParser(description="Herramientas de Seguridad y Reconocimiento")

    # Definir cada flag con nombres cortos
    parser.add_argument("--subenum", action="store_true", help="Subdomain enumeration")
    parser.add_argument("--techdet", action="store_true", help="Technology detection")
    parser.add_argument("--dnsscan", action="store_true", help="DNS record scanning")
    parser.add_argument("--crawl", action="store_true", help="Web crawling and URL extraction")
    parser.add_argument("--favicon", action="store_true", help="Favicon hash calculation")
    parser.add_argument("--hostinj", action="store_true", help="Host header injection testing")
    parser.add_argument("--sechead", action="store_true", help="Security header analysis")
    parser.add_argument("--netvuln", action="store_true", help="Network vulnerability analysis")
    parser.add_argument("--wayback", action="store_true", help="Wayback machine URL retrieval")
    parser.add_argument("--jsdiscover", action="store_true", help="JavaScript file discovery")
    parser.add_argument("--linkchk", action="store_true", help="Broken link checking")
    parser.add_argument("--httpsmug", action="store_true", help="HTTP request smuggling detection")
    # Añade aquí el resto de las flags según sea necesario
    
    args = parser.parse_args()

    # Listar en orden de las flags activadas
    selected_tools = [flag for flag, active in vars(args).items() if active]
    
    # Ejecutar las herramientas en el orden especificado
    for tool in selected_tools:
        tool_function = tool_functions.get(tool)
        if tool_function:
            tool_function()
        else:
            print(f"Función para la herramienta {tool} no definida.")

if __name__ == "__main__":
    main()
