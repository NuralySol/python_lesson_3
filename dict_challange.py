#! Dictionary lab challange (20 min to solve)
#! make a spreadsheet called in data-frame in python data science from a list of car dictionaries

import pandas as pd

# given this list of 10 similar car dictionaries:
cars = [
    {
        "VIN": "4Y1-SL658-4-8-Z-41-1439",
        "available": False,
        "car fax": True,
        "color": "red",
        "condition": "excellent",
        "doors": 2,
        "engine": {"cyl": 8, "hp": 260, "ltr": 5.0},
        "extras": [
            "sun roof",
            "mag wheels",
            "leather seats",
            "spoiler",
            "frame decals",
        ],
        "make": "Ford",
        "model": "Mustang GT",
        "mpg": {"city": 14, "hwy": 23},
        "odometer": 71639.21160000002,
        "owner": {
            "first name": "Brian",
            "last name": "McClain",
            "original owner": False,
            "zip code": 10011,
        },
        "top speed": 151,
        "transmission": "manual",
        "year": 2003,
    },
    {
        "VIN": "3FA6P0H74HR245678",
        "available": True,
        "car fax": True,
        "color": "blue",
        "condition": "good",
        "doors": 4,
        "engine": {"cyl": 4, "hp": 175, "ltr": 2.5},
        "extras": ["backup camera", "Bluetooth", "cruise control"],
        "make": "Ford",
        "model": "Fusion",
        "mpg": {"city": 21, "hwy": 32},
        "odometer": 45821.35,
        "owner": {
            "first name": "Emily",
            "last name": "Jones",
            "original owner": True,
            "zip code": 94110,
        },
        "top speed": 130,
        "transmission": "automatic",
        "year": 2017,
    },
    {
        "VIN": "5J8TB3H5XFL012345",
        "available": True,
        "car fax": False,
        "color": "white",
        "condition": "fair",
        "doors": 4,
        "engine": {"cyl": 6, "hp": 280, "ltr": 3.5},
        "extras": ["navigation system", "heated seats"],
        "make": "Acura",
        "model": "RDX",
        "mpg": {"city": 20, "hwy": 28},
        "odometer": 95342.11,
        "owner": {
            "first name": "John",
            "last name": "Smith",
            "original owner": False,
            "zip code": 60614,
        },
        "top speed": 135,
        "transmission": "automatic",
        "year": 2015,
    },
    {
        "VIN": "1C4RJFAG4FC123456",
        "available": False,
        "car fax": True,
        "color": "black",
        "condition": "excellent",
        "doors": 4,
        "engine": {"cyl": 6, "hp": 295, "ltr": 3.6},
        "extras": ["4WD", "sun roof", "leather seats"],
        "make": "Jeep",
        "model": "Grand Cherokee",
        "mpg": {"city": 18, "hwy": 25},
        "odometer": 60213.75,
        "owner": {
            "first name": "Sarah",
            "last name": "Brown",
            "original owner": True,
            "zip code": 75201,
        },
        "top speed": 119,
        "transmission": "automatic",
        "year": 2016,
    },
    {
        "VIN": "19XFC2F59HE234567",
        "available": True,
        "car fax": True,
        "color": "silver",
        "condition": "excellent",
        "doors": 4,
        "engine": {"cyl": 4, "hp": 158, "ltr": 2.0},
        "extras": ["Bluetooth", "backup camera", "cruise control"],
        "make": "Honda",
        "model": "Civic",
        "mpg": {"city": 30, "hwy": 38},
        "odometer": 34219.55,
        "owner": {
            "first name": "Michael",
            "last name": "Davis",
            "original owner": False,
            "zip code": 30303,
        },
        "top speed": 125,
        "transmission": "manual",
        "year": 2017,
    },
    {
        "VIN": "2T1BURHE4JC345678",
        "available": True,
        "car fax": False,
        "color": "red",
        "condition": "good",
        "doors": 4,
        "engine": {"cyl": 4, "hp": 132, "ltr": 1.8},
        "extras": ["Bluetooth", "backup camera"],
        "make": "Toyota",
        "model": "Corolla",
        "mpg": {"city": 28, "hwy": 36},
        "odometer": 41258.77,
        "owner": {
            "first name": "Ashley",
            "last name": "Wilson",
            "original owner": True,
            "zip code": 98101,
        },
        "top speed": 115,
        "transmission": "automatic",
        "year": 2018,
    },
    {
        "VIN": "3VW2B7AJ7HM456789",
        "available": False,
        "car fax": True,
        "color": "green",
        "condition": "fair",
        "doors": 4,
        "engine": {"cyl": 4, "hp": 170, "ltr": 1.8},
        "extras": ["heated seats", "Bluetooth"],
        "make": "Volkswagen",
        "model": "Jetta",
        "mpg": {"city": 24, "hwy": 33},
        "odometer": 67321,
        "owner": {
            "first name": "David",
            "last name": "Martinez",
            "original owner": False,
            "zip code": 80202,
        },
        "top speed": 126,
        "transmission": "manual",
        "year": 2017,
    },
    {
        "VIN": "1N4AL3AP7JC678901",
        "available": True,
        "car fax": False,
        "color": "black",
        "condition": "excellent",
        "doors": 4,
        "engine": {"cyl": 4, "hp": 182, "ltr": 2.5},
        "extras": ["backup camera", "Bluetooth", "sun roof"],
        "make": "Nissan",
        "model": "Altima",
        "mpg": {"city": 27, "hwy": 38},
        "odometer": 52873.98,
        "owner": {
            "first name": "Jessica",
            "last name": "Garcia",
            "original owner": True,
            "zip code": 94105,
        },
        "top speed": 130,
        "transmission": "automatic",
        "year": 2018,
    },
    {
        "VIN": "WBA8E9C56GK123456",
        "available": True,
        "car fax": True,
        "color": "white",
        "condition": "good",
        "doors": 4,
        "engine": {"cyl": 4, "hp": 248, "ltr": 2.0},
        "extras": ["navigation system", "heated seats", "sun roof"],
        "make": "BMW",
        "model": "328i",
        "mpg": {"city": 23, "hwy": 34},
        "odometer": 37821.67,
        "owner": {
            "first name": "Chris",
            "last name": "Robinson",
            "original owner": False,
            "zip code": 60610,
        },
        "top speed": 155,
        "transmission": "automatic",
        "year": 2016,
    },
    {
        "VIN": "1FTFW1EF1HFB12345",
        "available": False,
        "car fax": True,
        "color": "blue",
        "condition": "excellent",
        "doors": 4,
        "engine": {"cyl": 8, "hp": 385, "ltr": 5.0},
        "extras": ["4WD", "backup camera", "Bluetooth"],
        "make": "Ford",
        "model": "F-150",
        "mpg": {"city": 15, "hwy": 21},
        "odometer": 29872.99,
        "owner": {
            "first name": "Mark",
            "last name": "Hernandez",
            "original owner": True,
            "zip code": 33101,
        },
        "top speed": 105,
        "transmission": "automatic",
        "year": 2017,
    },
]
# pass cars list to pandas to pandas data-frame method and it will return a data fram which is a 2D matrix 
#! of rows and colums here you have print it out as an object to see the output in the terminal
cars_df = pd.DataFrame(cars)
print(cars_df)

# CHALLENGE A
# loop the list of car dictionaries and save image file names for each to new list
# callec car_imgs the year make and model of each as image file name:
# expected output:
# CHALLENGE A: Create image file names for each car

car_imgs = []

for car in cars:
    img_name = f"{car['year']} {car['make']} {car['model']}.jpg"
    img_name = img_name.replace(" ", "-")
    car_imgs.append(img_name)

print("Car image file names:", car_imgs)

# CHALLENGE B
# Loop the ChatGPT-provided cars list of dictionaries
# Each time through the list, print FOR SALE listings for each car:

# EXAMPLE:
# For Sale: 2003 Ford Mustang GT -
# Emgine: 8 cyl, manual transmission, excellent condition,
# 71,639 miles, red, many extras: leather seats, sunroof, more

# looping through list of car dict
# "For Sale:"
# " Now Only "
# "\n Powerful "
# " condition, and comes in \n"

for car in cars:
    print(f"\nFor Sale: {car['year']} {car['make']} {car['model']} -")
    print(
        f"Engine: {car['engine']['cyl']} cyl, {car['transmission']} transmission, {car['condition']} condition,"
    )
    print(
        f"{car['odometer']:.0f} miles, {car['color']}, many extras: {', '.join(car['extras'])}"
    )

#! An extra if you want to flatten the above nested dict.
#! Remember functions are first-class citizens meaning that they can be assigned to variables, passed as arguments to other functions, and returned from functions (very versatile)


def flatten_dict(d, parent_key="", sep="."):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


flattened_cars = [flatten_dict(car) for car in cars]

for i, car in enumerate(flattened_cars, 1):
    print(f"Car {i} (flattened):")
    for key, value in car.items():
        print(f"{key}: {value}")
    print("\n")

