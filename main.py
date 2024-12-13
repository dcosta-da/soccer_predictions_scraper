import time
import os
from selenium_config import configure_driver
from scraper import scrape_data
from data_cleaning import clean_data, process_data
from excel_export import export_to_excel

def main():
    # Configurer Selenium
    driver = configure_driver()

    try:
        # Scraper les données
        match_data = scrape_data(driver)

        # Nettoyer et formater les données
        cleaned_data = clean_data(match_data)
        final_data = process_data(cleaned_data)

        # Exporter les données vers un fichier Excel
        export_to_excel(final_data)

    finally:
        # Fermer le navigateur
        driver.quit()

if __name__ == "__main__":
    main()