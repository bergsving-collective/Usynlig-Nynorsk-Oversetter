# Importer pakker
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import pyperclip

# Hent utklippstavle
i = pyperclip.paste()

# Start headless FireFox vindu
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get("https://www.apertium.org/index.nob.html#?dir=nob-nno&q="+str(i))

# Hent oversatt tekst og kopier
elem = driver.find_elements(By.TAG_NAME, "textarea")[1].text
pyperclip.copy(elem)

# Lukk vindu
driver.close()
