""" A program for looking up a country's name from a country code. """

import country_api 

def main():
    while True:
        code = input('Enter country code or press enter to quit ')
        if not code:
            break
        if len(code) != 2:
            print('Country code must be 2 letters')
            continue
        found, country_info, error = country_api.get_country_name(code)
        
        if found:
            name, capital = country_info
            print(f'{code} is the country code for {name}')
            print(f'Capital: {capital}')
        elif not found and not error:
            print('No country found for that code')
        else:
            print('Error fetching data')
        

main()
