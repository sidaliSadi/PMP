import freedom as free

if __name__ == "__main__":
    # specify the url
    url = 'https://locations.freedommobile.ca/results?address='
    villes = ['Ottawa, ON, Canada', 'Vancouver, BC, Canada', 'Toronto, ON, Canada', 'Richmond, BC, Canada', 'Calgary, AB, Canada', 'Edmonton, AB, Canada', 'Mississauga, ON, Canada', 'Cambridge, ON, Canada', 'Brampton, ON, Canada', 'Hamilton, ON, Canada']
    free.getStores(villes, url, 'resultat.json')
    