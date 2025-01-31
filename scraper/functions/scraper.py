from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pandas as pd
import time

def scrape_data(driver):
    match_data = []

    try:
        # Accéder à la page d'accueil de betclever.com
        driver.get("https://www.betclever.com")

        # Attendre que le bouton "View More Games" soit cliquable
        wait = WebDriverWait(driver, 10)
        view_more_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="showmore"]/b'))
        )
        
        # Cliquer sur le bouton "View More Games"
        view_more_button.click()
        print("Bouton 'View More Games' cliqué avec succès.")

        # Attendre que les nouveaux éléments se chargent
        time.sleep(5)

        # Récupérer les éléments "Match Tips"
        match_tips_elements = driver.find_elements(By.XPATH, '//a[contains(text(), "Match Tips")]')
        links = [element.get_attribute('href') for element in match_tips_elements]
        print("Liens 'Match Tips' récupérés avec succès.")

        # Parcourir chaque lien pour extraire les données
        for link in links:
            driver.get(link)
            time.sleep(3)  # Attendre le chargement complet de la page

            try:
                # Extraction des informations spécifiques au match
                date = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[1]/div/div[1]/div[3]/p[1]').text
                championship = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[1]/div/div[1]/div[1]/div[1]').text
                match = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[1]/div/div[1]/div[1]/div[2]').text

                # Section des prédictions "Match Result Predictions"
                predictions_section = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[2]')
                home_win = predictions_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[0].text
                home_odds = predictions_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[1].text
                draw = predictions_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[2].text
                draw_odds = predictions_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[3].text
                away_win = predictions_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[4].text
                away_odds = predictions_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[5].text

                # Section des prédictions "Total Goals Predictions"
                total_goals_section = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[4]/div/div[2]')
                over_1_5 = total_goals_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[0].text
                odds_1_5 = total_goals_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[1].text
                over_2_5 = total_goals_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[2].text
                odds_2_5 = total_goals_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[3].text
                over_3_5 = total_goals_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[4].text
                odds_3_5 = total_goals_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[5].text
                btts = total_goals_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[6].text
                odds_btts = total_goals_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[7].text

                # Ajouter les données au tableau
                match_data.append({
                    "Date": date,
                    "Championship": championship,
                    "Match": match,
                    "Home Win (%)": home_win,
                    "Home Odds": home_odds,
                    "Draw (%)": draw,
                    "Draw Odds": draw_odds,
                    "Away Win (%)": away_win,
                    "Away Odds": away_odds,
                    "Over 1.5 (%)": over_1_5,
                    "Odds 1.5": odds_1_5,
                    "Over 2.5 (%)": over_2_5,
                    "Odds 2.5": odds_2_5,
                    "Over 3.5 (%)": over_3_5,
                    "Odds 3.5": odds_3_5,
                    "Btts (%)": btts,
                    "Odds btts": odds_btts,
                    "Link": link
                })

            except Exception as e:
                print(f"Erreur lors de l'extraction des informations pour le lien {link}: {e}")
                continue

    except TimeoutException as e:
        print(f"Erreur: {e}")

    finally:
        # Fermer le navigateur
        driver.quit()

    # Convertir les données en DataFrame pandas
    return pd.DataFrame(match_data)
