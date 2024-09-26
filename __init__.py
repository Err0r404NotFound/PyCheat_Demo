import os
import sys
# Función para verificar si undetected_chromedriver está instalado
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
        
def display_results_and_choose(search_results):
    """Mostrar resultados de búsqueda y permitir al usuario elegir una opción."""
    if not search_results:
        print("No hay resultados para la búsqueda.\nRevisa tu ortografía o prueba con otro término.")
        return None
    
    print("\nEstas son las opciones disponibles, ¿con cuál quieres probar?")
    for index, result in enumerate(search_results, start=1):
        print(f"{index}: {result['name']}")
    
    try:
        choice = int(input("Selecciona el número de la opción deseada: \n$>:"))
        if 1 <= choice <= len(search_results):
            return search_results[choice - 1]
        else:
            print("Selección inválida.")
    except ValueError:
        print("Por favor, ingresa un número válido.")
    
    return None

def handle_scribd_search(term):
    """Realiza la búsqueda en Scribd y permite seleccionar una opción."""
    try:
        search_results = search_scribd(term)
        selected_result = display_results_and_choose(search_results)
        
        if selected_result:
            open_pdf_in_window(selected_result['href'])
    except Exception as e:
        print(f"Error al manejar la búsqueda en Scribd: {e}")

def handle_studocu_search(term):
    """Realiza la búsqueda en Studocu y permite seleccionar una opción."""
    search_results = search_studocu(term)
    selected_result = display_results_and_choose(search_results)
    
    if selected_result:
        open_page_and_hide_elements(selected_result['href'])

    
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
    from scribd.module_search_scribd import search_scribd, open_pdf_in_window
    from studocu.module_search_studocu import open_page_and_hide_elements, search_studocu
    
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
        |___/    V.1.1.0.0               

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
                handle_scribd_search(search_term)
            elif result == 2:
                search_term = input("Por favor, ingrese la pregunta para la búsqueda: \n$>: ")
                handle_studocu_search(search_term)
            elif result == 3:
                search_term = input("Por favor, ingrese el link: \n$>: ")
                open_pdf_in_window(search_term)
            elif result == 4:   
                search_term = input("Por favor, ingrese el link: \n$>: ")
                open_page_and_hide_elements(search_term)
            else:
                print("Opción no válida. Inténtelo de nuevo.")
        except Exception as e:
            print(f"Error al capturar resultados: {e}")
        except KeyboardInterrupt:
            print("\nSe ha detenido el programa.")
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")
