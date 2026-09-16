def transform_data(data):
    if data is None:
        return None
    for row in data:
        fahrenheit = row['temperature']
        celsius = (fahrenheit - 32) * 5/9
        row['temperature_f'] = round(celsius, 1)
    print(" Data transformerad (Fahrenheit → Celsius)")
    return data