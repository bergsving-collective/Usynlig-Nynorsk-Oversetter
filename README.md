# Usynlig Nynorsk Oversetter
Et enkelt Python skript som oversetter utklippstavlen din til Nynorsk. Fungerer ideelt med AutoHotKey slik at man kan aktivere skriptet ved et enkelt tastetrykk. Skriptet fungerer som en webscraper, og kobles til nettstedet Apertium via en hodeløs Firefox-nettleser. Dermed krever skriptet åpent nett.
## Installasjon og Bruk
- Sørg for at du har den nyeste versjonen av [Python 3](https://www.python.org/downloads/).
- Skriptet bruker Selenium som igjen bruker [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/). Du trenger ikke bruke Firefox som standard nettleser, men sørg for at det er installert.

- Vi er også avhengig av to eksterne pakker. Åpne et terminalvindu og installer disse:
```
python -m pip install selenium
python -m pip install pyperclip
```
Du kan nå kjøre [skriptet](https://github.com/cheval-constipe/Usynlig-Nynorsk-Oversetter/blob/main/script.py). Når skriptet kjører dukker det opp et svart terminalvindu som lukker seg igjen etter et øyeblikk. Da er utklippstavlen din oversatt (eller noe har gått galt). Prøv selv!

### Med AutoHotKey
Man kan kjøre skriptet ved et tastetrykk med [AutoHotKey](https://www.autohotkey.com).
- Installer programmet
- Last ned [denne filen](https://github.com/cheval-constipe/Usynlig-Nynorsk-Oversetter/blob/main/oversett.ahk) og plasser i samme mappe som Python-skriptet.
- Kjør med AutoHotKey.

Du skal nå kunne starte skriptet med Home knappen. Du kan endre `Home` til hvilken tast du ønsker. Du kan finne en liste med forskjellige taster [her](https://www.autohotkey.com/docs/KeyList.htm).
