def city_country(city, country, population=''):
    if population:
        output = f"{city.title()}, {country.title()} - population {str(population)}"
    else:
        output = f"{city.title()}, {country.title()}"
    return output
