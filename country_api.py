import requests 

def get_country_name(country_code):
    """ Returns a tuple of found, country name, error 
    If country is found, the tuple will be (True, country name, None)
    If country is not found, the tuple will be (False, None, None)
    If there is an error connecting to the API. the tuple will be (False, None, error message)"""

    try:
        country_api_url = create_url(country_code)
        country_data_response = make_api_request(country_api_url)
        if not country_data_response:
            return False, None, None
        country_official_name, country_capital = get_name_from_response(country_data_response)
        return True, (country_official_name, country_capital), None
    except Exception as e:
        return False, None, 'Error connecting to API'

def create_url(country_code):
    country_api_url = f'https://restcountries.com/v3.1/alpha/{country_code}'
    return country_api_url


def make_api_request(url):
    api_response = requests.get(url)
    if api_response.status_code == 404:
        return None
    api_response.raise_for_status()
    response_json_data = api_response.json()  
    return response_json_data


def get_name_from_response(json_response):
    try:
        country_official_name = json_response[0]['name']['official']
        country_capital = json_response[0].get('capital', ['Unknown'])[0]
        return country_official_name, country_capital
    except (IndexError, KeyError):
        return None, None
