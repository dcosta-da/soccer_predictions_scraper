from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pandas as pd
import time

def scrape_data(driver):
    match_data = []

    try:
        driver.get("https://www.betclever.com")

        wait = WebDriverWait(driver, 10)
        view_more_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="showmore"]/b'))
        )
        
        view_more_button.click()
        print("Bouton 'View More Games' cliqué avec succès.")

        time.sleep(5)

        match_tips_elements = driver.find_elements(By.XPATH, '//a[contains(text(), "Match Tips")]')
        links = [element.get_attribute('href') for element in match_tips_elements]
        print("Liens 'Match Tips' récupérés avec succès.")

        for link in links:
            driver.get(link)
            time.sleep(3) 

            try:
                date = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[1]/div/div[1]/div[3]/p[1]').text
                championship = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[1]/div/div[1]/div[1]/div[1]').text
                match = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[1]/div/div[1]/div[1]/div[2]').text

                predictions_section = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[2]')
                home_win = predictions_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[0].text
                home_odds = predictions_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[1].text
                away_win = predictions_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[4].text
                away_odds = predictions_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[5].text

                total_goals_section = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[4]/div/div[2]')
                over_2_5 = total_goals_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[2].text
                odds_2_5 = total_goals_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[3].text
                over_3_5 = total_goals_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[4].text
                odds_3_5 = total_goals_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[5].text
                btts = total_goals_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[6].text
                odds_btts = total_goals_section.find_elements(By.CLASS_NAME, 'match-history__item-numbers')[7].text

                match_data.append({
                    "Date": date,
                    "Championship": championship,
                    "Match": match,
                    "Home Win (%)": home_win,
                    "Home Odds": home_odds,
                    "Away Win (%)": away_win,
                    "Away Odds": away_odds,
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
        driver.quit()

    return pd.DataFrame(match_data)
