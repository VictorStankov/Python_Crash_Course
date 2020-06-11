def build_car(manufacturer, model_name, **stuff):
    car_info = {}
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model_name
    for key, value in stuff.items():
        car_info[key] = value
    return car_info


car = build_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
