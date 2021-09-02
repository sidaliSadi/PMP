# import libraries

from selenium import webdriver
import time
import json
import re

def getStores(villes, url, filename):
    """
    Input:
        villes: liste de villes
        url: url de site sans le nom de ville
        filename: le nom de fichier de sortie fichier json
    """
    # run firefox webdriver from executable path
    driver = webdriver.Firefox(executable_path = 'C:/Users/33766/Downloads/geckodriver-v0.29.1-win64/geckodriver.exe')
    magasins_par_ville = []
    for ville in villes:
        magasins_dune_ville = dict()
        magasins_adresses = []
        # specify the url
        urlpage = url+ville 
        print(urlpage)
        # get web page
        driver.get(urlpage)
        time.sleep(5)
        #pour augmenter le rayon de recherche
        rayon_100 = driver.find_element_by_id('search-radius')
        rayon_100.send_keys(100)
        #attendre que la page se charge correctement
        time.sleep(5)
        magasins = driver.find_elements_by_css_selector('p.dhtNbX')
        adresse = " "
        for magasin in magasins:
            
            if splitAdresse(magasin.text):
                adresse = adresse +" "+ magasin.text
                magasins_adresses.append( adresse)
                adresse = " "
            else:
              adresse = adresse +" "+ magasin.text
        
        magasins_dune_ville[ville] = magasins_adresses
        magasins_par_ville.append(magasins_dune_ville)
        
    with open(filename, "w") as outfile:
        json.dump(magasins_par_ville, outfile, indent=4)
    driver.quit()

def splitAdresse(text):
    """
    elle verifie si un text est un code postal, cette fonction me sert pour la construction d'une adresse complete
    Input:
        chaine de caracteres
    Output:
        Bool
    """
    token_pattern = re.compile("^[A-Z]\w{0,2}\s")
    tokens = re.findall(token_pattern, text)
    if len(tokens):
        return True
    else:
        return False
   