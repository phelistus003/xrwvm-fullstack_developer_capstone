from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars"},
        {"name": "TOYOTA", "description": "Great cars"},
        {"name": "AUDI", "description": "Great cars"},
        {"name": "KIA", "description": "Great cars"},
        {"name": "CHEVROLET", "description": "Great cars"}
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))

    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "Xtrail", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "Corolla", "type": "Sedan", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "Camry", "type": "Sedan", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "RAV4", "type": "SUV", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "A3", "type": "Sedan", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "A4", "type": "Sedan", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "A6", "type": "Sedan", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "Sportage", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Sorento", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Cruze", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4]}
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'], 
            car_make=data['car_make'], 
            car_type=data['type'], 
            year=data['year']
        )