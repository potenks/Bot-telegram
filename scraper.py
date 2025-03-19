from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def get_followers(username):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecuta Chrome sin interfaz gráfica
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    url = f"https://www.instagram.com/{username}/"
    driver.get(url)
  #  time.sleep(5)  # Esperar a que cargue la página
    
    try:
        followers_element = driver.find_element(By.CSS_SELECTOR, 'meta[property="og:description"]')
        followers_text = followers_element.get_attribute("content")
        followers_count = followers_text.split(" ")[0]  # Extrae el número de seguidores
    except:
        followers_count = "Error"
    
    driver.quit()
    return followers_count
