from functions.selenium_config import configure_driver
from functions.scraper import scrape_data
from functions.data_cleaning import clean_data, process_data, compute_ev
from functions.excel_export import export_to_excel

def main():
    driver = configure_driver()

    try:
        match_data = scrape_data(driver)

        cleaned_data = clean_data(match_data)
        processed_data = process_data(cleaned_data)
        final_data = compute_ev(processed_data)

        export_to_excel(final_data)

    finally:
        # Fermer le navigateur
        driver.quit()

if __name__ == "__main__":
    main()