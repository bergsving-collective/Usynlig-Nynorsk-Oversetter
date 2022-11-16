# Importer pakker
import json
import requests
import pyperclip
import os

# Hent utklippstavle
t = pyperclip.paste()

# Send API request
r = requests.get("https://beta.apertium.org/apy/translate",
                 params={"langpair": "nob|nno", "q": t})

final = json.loads(r.text)["responseData"]["translatedText"]

pyperclip.copy(final)

# Lukk terminalvindu
os.kill(os.getppid(), 1)
