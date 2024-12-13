from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_data(driver):
    match_data = []
    driver.get("https://www.betclever.com")
    
    # Attendre et cliquer sur le bouton 'View More Games'
    wait = WebDriverWait(driver, 10)
    view_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="showmore"]/b')))
    view_more_button.click()
    
    # Attendre que les nouveaux matchs se chargent
    time.sleep(5)
    
    # Récupérer les liens
    match_tips_elements = driver.find_elements(By.XPATH, '//a[contains(text(), "Match Tips")]')
    links = [element.get_attribute('href') for element in match_tips_elements]
    
    # Extraire les données des liens
    for link in links:
        driver.get(link)
        time.sleep(3)  # Attendre que la page se charge complètement
        
        # Ajouter des informations dans match_data (c'est ici que les détails sont extraits)
        try:
            # Extraire les informations nécessaires pour chaque match
            # (les éléments XPath sont à adapter selon la structure du site)
            match_info = extract_match_info(driver)
            match_data.append(match_info)
        except Exception as e:
            print(f"Erreur lors de l'extraction pour {link}: {e}")
    
    return match_data

def extract_match_info(driver):
    # Logique pour extraire les informations spécifiques de chaque match
    # Cette fonction doit être adaptée en fonction des éléments HTML du site
    match_info = {
        "Date": driver.find_element(By.XPATH, '/html/body/div[1]/main/section[1]/div/div[1]/div[3]/p[1]').text,
        "Championship": driver.find_element(By.XPATH, '/html/body/div[1]/main/section[1]/div/div[1]/div[1]/div[1]').text,
        "Match": driver.find_element(By.XPATH, '/html/body/div[1]/main/section[1]/div/div[1]/div[1]/div[2]').text,
        # Ajouter d'autres informations similaires ici
    }
    return match_info
