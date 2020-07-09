import json


cars = ["BMW", "AUDI", "TOYOTA"]


def getCars(event, context):
    response = {
        "statusCode": 200,
        "body": json.dumps(cars)
    }

    return response


def addCar(event, context):
    # cars.append()
    response = {
        "statusCode": 200,
        "body": json.dumps(cars)
    }

    return response
