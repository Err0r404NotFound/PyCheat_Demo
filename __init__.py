import os
import sys
def check_uc():
    try:
        import undetected_chromedriver as uc
        print("undetected_chromedriver está instalado.")
        return True
    except ImportError:
        return False

def is_chrome_installed():
    chrome_paths = {
        "win32": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "linux": "/usr/bin/google-chrome",
        "darwin": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    }

    # Detectar el sistema operativo actual
    current_os = sys.platform

    # Obtener la ruta correspondiente para el sistema operativo
    chrome_path = chrome_paths.get(current_os)

    if chrome_path and os.path.exists(chrome_path):
        print("Google Chrome está instalado.")
        return True
    else:
        return False
if __name__ == "__main__":
    # Validar si Chrome y undetected_chromedriver están instalados
    if not is_chrome_installed():
        print("Por favor, instala Google Chrome para continuar.")
        input("Presiona Enter para salir...")
        sys.exit()

    if not check_uc():
        print("Por favor, instala undetected_chromedriver para continuar.")
        input("Presiona Enter para salir...")
        sys.exit()
        #Si existen las 2 cosas, procedemos a importar los modulos y a ejecutar el programa
    while True:
        try:
            print("""
 _____        _____ _                _   
|  __ \      / ____| |  By:Diego G  | |  
| |__) |   _| |    | |__   ___  __ _| |_ 
|  ___/ | | | |    | '_ \ / _ \/ _` | __|
| |   | |_| | |____| | | |  __/ (_| | |_ 
|_|    \__, |\_____|_| |_|\___|\__,_|\__|
        __/ |                            
        |___/    V.1.1.0              

Para detener el programa Ctrl + C   

Opciones:
1:Buscar En Scribd.
2:Buscar En Studocu. (Bypass Por Bot, Bypass Por Bloqueo)
3:Desbloquear Documento Manual Scribd
4:Desbloquear Documento Manual Studocu

Por favor seleccione una de las opciones.
    """)

            result = int(input("$>:"))
            if result == 1:
                search_term = input("Por favor, ingrese la pregunta para la búsqueda: \n$>: ")  
                input(f"La busqueda fue: {search_term}\nEsto es solo una version de prueba, vaya a release para descargar la version completa")
            elif result == 2:
                search_term = input("Por favor, ingrese la pregunta para la búsqueda: \n$>: ")
                input(f"La busqueda fue: {search_term}\nEsto es solo una version de prueba, vaya a release para descargar la version completa")
            elif result == 3:
                search_term = input("Por favor, ingrese el link: \n$>: ")
                input(f"La busqueda fue: {search_term}\nEsto es solo una version de prueba, vaya a release para descargar la version completa")
            elif result == 4:   
                search_term = input("Por favor, ingrese el link: \n$>: ")
                input(f"La busqueda fue: {search_term}\nEsto es solo una version de prueba, vaya a release para descargar la version completa")
            else:
                print("Opción no válida. Inténtelo de nuevo.")
        except Exception as e:
            print(f"Error al capturar resultados: {e}")
        except KeyboardInterrupt:
            print("\nSe ha detenido el programa.")
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")
