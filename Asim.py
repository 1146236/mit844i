from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import re 

# Start
driver = webdriver.Chrome()

# Url 
url = "www.bbc.com/news"

try:

    # go to BBC News page
    driver.get(f"https://{url}")                                    

    # Wait and find
    DEFAULT_WAIT = 15
    cards = WebDriverWait(driver, DEFAULT_WAIT).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="card-text-wrapper"]'))
    )

    print("\nBBC News page is loading...\n")
    for i, card in enumerate(cards, 1):

        try:
            # Title
            headline = card.find_element(By.CSS_SELECTOR, '[data-testid="card-headline"]').text
            # Summary
            description = card.find_element(By.CSS_SELECTOR, '[data-testid="card-description"]').text

            if re.search("[a-zA-Z]", headline or description) or headline == "Sign up here":
                # print Title and Summary
                print(f"\n--- News {i} {"-"*38}")
                print(f"Title: {headline}")
                print(f"Summary: {description}")
                print("-"*50)
            else:
                continue

        except Exception as e:
            print(f"{i}.Error: {e}")

finally:
    # Quit
    driver.quit()
