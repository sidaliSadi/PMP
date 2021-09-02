# PMP
# Guide installation 
***
* pip install selenium
* <a >https://github.com/mozilla/geckodriver/releases </a> pour installer geckodriver

* Ajouter le chemin du fichier téléchargé  dans la variable d'environnement PATH ==> driver = webdriver.Firefox()
* Sinon il faut modifier la ligne 
 driver = webdriver.Firefox(executable_path = 'C:/Users/33766/Downloads/geckodriver-v0.29.1-win64/geckodriver.exe')
 executable path = chemin vers le fichier téléchargé