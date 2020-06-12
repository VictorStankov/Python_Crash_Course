import json
from country_codes import get_country_code

filename = 'population_json.json'
with open(filename) as f:
    pop_data = json.load(f)

for pop_dict in pop_data:
    if pop_dict['Year'] == 2010:
        country_name = pop_dict['Country Name']
        population = int(pop_dict['Value'])
        code = get_country_code(country_name)
        if code:
            print(f"{code}: {str(population)}")
        else:
            print(f"Error - {country_name}")
