def city_country(city, country, population=None, language=None):
    if population and language:
        return f"{city}, {country} - population {population}, {language}"
    elif population:
        return f"{city}, {country} - population {population}"
    else:
        return f"{city}, {country}"


# Final function calls
print(city_country("Berlin", "Germany"))
print(city_country("Santiago", "Chile", 5000000))
print(city_country("Tokyo", "Japan", 13900000, "Japanese"))