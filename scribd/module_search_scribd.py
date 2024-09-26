import undetected_chromedriver as uc
import time
import traceback

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"

def search_scribd(term):
    try:
        print("\nPor favor esperar a que termine el proceso de Busqueda... \n")
        # Configurar opciones para Chrome
        options = uc.ChromeOptions()
        options.add_argument(f"--user-agent={user_agent}")
        options.add_argument("--disable-webrtc")
        options.add_argument("--disable-extensions")
        options.add_argument("--incognito")
        #options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Modificar si es necesario

        print("Iniciando Chrome...")
        driver = uc.Chrome(options=options)
        driver.minimize_window()

        # Abrir Scribd
        driver.get(f"https://www.scribd.com/search?query={term}")
        time.sleep(5)  # Espera a que la página cargue

        results = []
        try:
            print("Buscando elementos...")
            # Encontrar todos los elementos con la clase especificada
            elements = driver.find_elements("class name", "FluidCell-module_linkOverlay__v8dDs")

            for element in elements[:10]:
                name = element.text
                href = element.get_attribute("href")
                results.append({"name": name, "href": href})
            print(f"Se encontraron {len(results)} resultados.")
        except Exception as e:
            print("Error al capturar resultados.")
            print(traceback.format_exc())

        # Cerrar el navegador
        driver.quit()
        return results

    except Exception as e:
        print("Error al iniciar el proceso.")
        print(traceback.format_exc())

def open_pdf_in_window(url):
    
    original_href = url
    id_part = original_href.split("/document/")[1].split("/")[0]
    modified_href = f"https://es.scribd.com/embeds/{id_part}/content"
    
    options = uc.ChromeOptions()
    options.add_argument(f"--user-agent={user_agent}")
    options.add_argument("--disable-webrtc")
    options.add_argument("--disable-extensions")
    options.add_argument("--incognito")
    options.add_argument(f"--app={modified_href}")
    driver = uc.Chrome(options=options) 

    driver.get(modified_href)
    time.sleep(5)
    driver.execute_script("""                 
(async function() {
    var elements = document.querySelectorAll('.toolbar_top, .right_tools, .toolbar_download');
    elements.forEach(function(element) {
        element.style.display = 'none'; // Ocultar los elementos
    });
    alert("Proceso Finalizado");
})();
                          """)