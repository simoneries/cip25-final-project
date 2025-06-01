"""
Je veux créer un outil pour me mettre à jour sur les concerts qui sortent avec l'api de ticketmaster.
First milestone : Recevoir des données de l'API
Second milestone : A partir des données, demander à l'utilisateur quels concerts il aimerait voir et en sortir les infos. 
"""
import requests

API_KEY= "4TE236Lsgs1zy2dWS9dNxGoOK9ZKsaxl"


#Second step : Get data for Paris, Nanterre, Saint-Denis

def main():

    pass

def get_api_data():
    #First step : Get API data.
    response = requests.get("https://app.ticketmaster.com/discovery/v2/events.json?countryCode=FR&apikey=4TE236Lsgs1zy2dWS9dNxGoOK9ZKsaxl")
    info_dict=response.json()
    print(info_dict["_embedded"]["events"][1])

get_api_data()