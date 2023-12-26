from faker import Faker
import json

faker = Faker()


def payload_create_booking():
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_create_booking_dynamic():
    json_payload = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=1000),
        "depositpaid": faker.boolean(),
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
            # "checkin": str(faker.date_between(start_date='-3y', end_date='today')),
            # "checkout": str(faker.date_between(start_date='today', end_date='+3y'))
        },
        "additionalneeds": faker.random_elements(elements=("breakfast", "Parking", "WiFi"))
    }
    return json_payload


def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload
