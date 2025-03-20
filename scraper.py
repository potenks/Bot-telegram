# scraper.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

def get_followers(username):
    # Configuración de opciones de Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecutar en modo sin cabeza
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")  # Evitar detección de bot
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")  # Simular un navegador real

    # Inicializar el navegador
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Abrir la página de Instagram
        url = f"https://www.instagram.com/{username}/"
        driver.get(url)

        # Esperar a que la página cargue completamente
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "seguidores")]'))
        )

        # Obtener el número de seguidores
        followers_element = driver.find_element(By.XPATH, '//a[contains(@href, "/followers/")]//span[@title]')
        followers_count = followers_element.get_attribute("title")

    except TimeoutException:
        followers_count = "Error: Tiempo de espera agotado. No se pudo cargar la página."
    except NoSuchElementException:
        followers_count = "Error: No se encontró el elemento de seguidores."
    except Exception as e:
        followers_count = f"Error inesperado: {str(e)}"
    finally:
        # Cerrar el navegador
        driver.quit()

    return followers_count