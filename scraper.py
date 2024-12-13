from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

def scrape_data(driver):
    match_data = []
    driver.get("https://www.betclever.com")

    try:
        # Attendre et cliquer sur le bouton 'View More Games'
        wait = WebDriverWait(driver, 10)
        view_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="showmore"]/b')))
        view_more_button.click()

        # Attendre que les nouveaux matchs se chargent
        time.sleep(5)

        # Récupérer les liens
        match_tips_elements = driver.find_elements(By.XPATH, '//a[contains(text(), "Match Tips")]')
        links = [element.get_attribute('href') for element in match_tips_elements]
    except TimeoutException:
        print("Erreur : Le bouton 'View More Games' ou les liens de matchs n'ont pas pu être trouvés.")
        return match_data

    # Extraire les données des liens
    for link in links:
        try:
            driver.get(link)
            wait.until(EC.presence_of_element_located((By.XPATH, '//main')))
            
            # Extraire les informations spécifiques de chaque match
            match_info = extract_match_info(driver)
            match_data.append(match_info)
        except Exception as e:
            print(f"Erreur lors de l'extraction pour {link}: {e}")

    return match_data

def extract_match_info(driver):
    wait = WebDriverWait(driver, 10)
    match_info = {}

    try:
        # Extraire la date
        date_element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "date-class")]/p[1]')))
        match_info["Date"] = date_element.text
    except TimeoutException:
        match_info["Date"] = "N/A"

    try:
        # Extraire le championnat
        championship_element = driver.find_element(By.XPATH, '//div[contains(@class, "championship-class")]')
        match_info["Championship"] = championship_element.text
    except NoSuchElementException:
        match_info["Championship"] = "N/A"

    try:
        # Extraire le match
        match_element = driver.find_element(By.XPATH, '//div[contains(@class, "match-class")]')
        match_info["Match"] = match_element.text
    except NoSuchElementException:
        match_info["Match"] = "N/A"

    return match_info
