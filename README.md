# Usynlig Nynorsk Oversetter
Et enkelt Python skript som oversetter utklippstavlen din til Nynorsk. Fungerer ideelt med AutoHotKey slik at man kan aktivere skriptet ved et enkelt tastetrykk. Skriptet fungerer som en webscraper, og kobles til nettstedet Apertium via en hodeløs Firefox-nettleser. Dermed krever skriptet åpent nett.
## Installasjon og Bruk
Sørg for at du har den nyeste versjonen av [Python 3](https://www.python.org/downloads/).

Skriptet bruker Selenium som igjen bruker [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/). Installer dette.

Vi er også avhengig av to eksterne pakker. Åpne et terminalvindu og installer disse:
```
pip install selenium
pip install pyperclip
```
Du kan nå kjøre [skriptet](https://github.com/cheval-constipe/Usynlig-Nynorsk-Oversetter/blob/main/script.py).

### Med AutoHotKey
Man kan kjøre skriptet ved et tastetrykk med [AutoHotKey](https://www.autohotkey.com). Installer programmet, last ned [denne filen](https://github.com/cheval-constipe/Usynlig-Nynorsk-Oversetter/blob/dev-1/oversett.ahk) og plasser i samme mappe som Python-skriptet. Kjør med AutoHotKey. Du skal nå kunne starte skriptet med Home knappen. Du kan endre `Home` til hvilken tast du ønsker. Du kan finne en liste med forskjellige taster [her](https://www.autohotkey.com/docs/KeyList.htm).
