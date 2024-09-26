import undetected_chromedriver as uc 
import time
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"

#Con Undetected Chrome 
def search_studocu(term):
    print("\nPor favor esperar a que termine el proceso de Busqueda... \n")
    options = uc.ChromeOptions()
    #options.add_argument(f"--user-agent={user_agent}")
    options.add_argument("--disable-webrtc")
    options.add_argument("--disable-extensions")
    options.add_argument("--incognito")

    driver = uc.Chrome(options=options) 
    driver.minimize_window()
    driver.get(f"https://www.studocu.com/co/search/{term}?t={int(time.time())}")
    
    
    # Validar el título y recargar sin cache si es necesario
    while True:
        time.sleep(5) 
        if driver.title == "Access to this page has been denied":
            print("\nEl acceso a esta página ha sido denegado. Recargando sin cache...\n")
            driver.execute_script("location.href = location.href;")
        else:
            break 
    
    results = []
    try:
        elements = driver.find_elements("class name", "_95d1d9b8757c")

        for element in elements[:10]:
            link_element = element.find_element("tag name", "a")
            name = link_element.text
            href = link_element.get_attribute("href")
            results.append({"name": name, "href": href})

    except Exception as e:
        print(f"Error al capturar resultados: {e}")

    # Cerrar el navegador
    driver.quit()
    return results

def open_page_and_hide_elements(url):
    options = uc.ChromeOptions()
    options.add_argument(f"--user-agent={user_agent}")
    options.add_argument("--disable-webrtc")
    options.add_argument("--disable-extensions")
    options.add_argument("--incognito")
    options.add_argument(f"--app={url}")
    driver = uc.Chrome(options=options) 

    driver.get(url)
    # Validar el título y recargar sin cache
    while True:
        time.sleep(5)
        if driver.title == "Access to this page has been denied":
            print("\nEl acceso a esta página ha sido denegado. Recargando sin cache...\n")
            driver.execute_script("location.href = location.href;")
        else:
            break
    
    driver.execute_script("""
        function hideElementById(id) {
            var element = document.getElementById(id);
            if (element) {
                element.style.display = 'none';
            }
        }

    // Función para ocultar un elemento por clases
    function hideElementByClasses(classes) {
        var element = document.querySelector(classes);
        if (element) {
            element.style.display = 'none';
        }
    }

    // Ocultar elementos por ID
    hideElementById('onetrust-banner-sdk');
    hideElementById('sidebar');
    
    // Ocultar elementos por clases
    hideElementByClasses('._f04d82b80fd8');
    hideElementByClasses('._f677a7fe81a8')
    hideElementByClasses('._be945ce042ab._6f3dca40cabd._df890a73cf52._51b4ea13e1fb');
    hideElementByClasses('._f677a7fe81a8._2ff01c1a5338');
    hideElementByClasses('._2139c0274de9._3cb976d2b79b');
    hideElementByClasses('._bd6d12062c77');
    


    (async function() {

	const bgImageName = "bg1.png";
	const imageRegex = /bg[0-9]+\.png/
	const blurImageRegex = /blurred\/page([0-9]+)\.webp/
	const downloadButtonRegex = /(Download|Herunterladen|Scarica|Télécharger)/
	const maxInjectTries = 1000;

	let documentWrapper = null;
	let imgUrl = null;
	
	inject(maxInjectTries);
	setInterval(() => {
		if (documentWrapper != null && document.getElementById("bypass-button") == null) {
			console.log("StuDocu Unblocker: Reinject ...");
			inject(maxInjectTries);
		}
	}, 1000);

	async function inject(maxTries) {
		documentWrapper = null;
		while (documentWrapper == null) {
			documentWrapper = document.getElementById("document-wrapper");
			await new Promise(r => setTimeout(r, 100));
			if (maxTries-- <= 0) {
				console.error("StuDocu Unblocker: Could not find document wrapper!");
				return;
			}
		}

		for (const img of [...document.querySelectorAll("img")]) {
			if (img.src.replace(bgImageName, "") != img.src) {
				imgUrl = img.src;
				break;
			}
		}
		
		const globalStyle = document.createElement('style');
		globalStyle.innerText = `
			.unblock-button {
				margin: 0 0 0 10px;
				padding: 7px 24px;
				border: none;
				background-color: #61c4ff;
				color: white;
				cursor: pointer;
				font-weight: bold;
				border-radius: 32px;
			}
			.unblock-button:hover {
				background-color: #4da6ff;
			}
			.unblock-button:active {
				background-color: #3b8ad9;
			}
		`;
		document.head.appendChild(globalStyle);

		const header = document.querySelector("header");

		const bypassButton = document.createElement('button');
		bypassButton.id = "bypass-button";
		bypassButton.innerText = "🔓 Desbloquear Documento";
		bypassButton.className = "unblock-button";
		bypassButton.onclick = unblock;
		header.appendChild(bypassButton);

		console.log("StuDocu Unblocker: Injected!");
		alert("Proceso Finalizado");
	}

	function unblock() {
		var style = document.createElement('style');
		style.innerText = "div { filter: none !important; }";
		document.head.appendChild(style);


		const pages = [...documentWrapper.querySelectorAll(".pf")];
		
		for (const page of pages) {
			const children = [...page.children];
			for (const child of children) {
				if (child.innerHTML.toLowerCase().indexOf("<img") <= 0) {
					child.remove();
				}
			}
		}
	
		documentWrapper.querySelectorAll("div > div").forEach(e => {
			const computedStyleMap = e.computedStyleMap();
			const position = computedStyleMap.get('position');
			if (position && position.value.toLowerCase() == "sticky") {
				e.remove();
			}
		})
	
		documentWrapper.querySelectorAll("#premium-page-header").forEach(e => {
			e.remove();
		})
	
		// documentWrapper.querySelectorAll(".pf > div").forEach(e => {
		// 	if (e.innerHTML.toLowerCase().indexOf("premium") >= 0) {
		// 		e.remove();
		// 	}
		// })
	
		document.querySelectorAll("button").forEach(e => {
			if (downloadButtonRegex.test(e.innerHTML)) {
				var cloned = e.cloneNode(true);
				e.parentNode.replaceChild(cloned, e);
				cloned.className = "unblock-button";
				cloned.innerText = "🔓 Impresion";
				cloned.onclick = (e) => {
					e.preventDefault();
					printPdf();
				};
			}
		})

		documentWrapper.querySelectorAll("img").forEach(e => {
			if (blurImageRegex.test(e.src)) {
				const index = blurImageRegex.exec(e.src)[1];
				e.src = imgUrl.replace(bgImageName, `bg${index}.png`);
			}
		})
	
		
		function printPdf() {
			const printView = window.open();

			const styles = document.createElement('style');
			styles.innerText = `
				img {
					max-width: 100%;
					height: auto;
				}
			`;

			printView.document.head.appendChild(styles);

			const images = [...document.querySelectorAll("img")].filter(
				e => imageRegex.test(e.src)
			);
			printView.document.body.innerHTML = images.map(e => e.outerHTML).join("<br>");
		}
	}

})();
        
    """)
