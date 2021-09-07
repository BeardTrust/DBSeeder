#!/usr/bin/env python3

import enum
import uuid

import data.names
import data.domains
import data.addresses
import random


class Gender(enum.Enum):
    """
    This represents the gender of a biological organism.
    """
    female = 0
    male = 1


def generate_role():
    role_index = random.randint(0, 100000)
    return 'admin' if role_index <= 5 else 'user'


def generate_user_id():
    return uuid.uuid4()

def generate_gender():
    gender_identifier = random.randint(0, 1)

    return Gender(gender_identifier)


def generate_given_name(gender: Gender) -> str:
    """
    This function takes a Gender as an argument and generates an appropriate
    given name for a person with the provided gender.

    :param gender: the gender of the personal details being generated
    :return str: a gender-appropriate given name
    """

    gender_index = 0 if gender == gender.male else 1
    name_index = random.randint(0, len(data.names.get_given_names()) - 1)

    return data.names.get_given_names()[name_index][gender_index]


def generate_surname() -> str:
    """
    This function randomly generates a surname.
    :return str: the generated surname
    """

    surnames = data.names.get_surnames()
    max_index = len(surnames) - 1
    index = random.randint(0, max_index)

    return surnames[index]


def generate_email(first_name, last_name):
    domains = data.domains.get_domains()
    domain_index = random.randint(0, len(domains) - 1)
    return first_name + '.' + last_name + '@' + domains[domain_index]


def generate_date(min_year, max_year):
    year = random.randint(min_year, max_year)
    month = random.randint(1, 12)

    if month % 2 == 0:
        if month == 2:
            day = random.randint(1, 28)
        elif month < 8:
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 31)
    else:
        if month < 8:
            day = random.randint(1, 31)
        else:
            day = random.randint(1, 30)

    dob = str(year) + '-' + str(month) + '-' + str(day)

    return dob


def generate_street_address():
    streets = data.addresses.get_streets()
    street_index = random.randint(0, len(streets) - 1)

    house_number = random.randint(0, 9999)
    return str(house_number) + ' ' + streets[street_index]


def generate_city():
    cities = data.addresses.get_cities()
    city_index = random.randint(0, len(cities) - 1)

    return cities[city_index]


def generate_state():
    states = data.addresses.get_states()
    state_index = random.randint(0, len(states) - 1)

    return states[state_index]


def generate_zipcode():
    zip_code = ''
    for x in range(5):
        zip_code += (str(random.randint(0, 9)))

    return zip_code


def generate_phone_number():
    phone_number = ''
    for x in range(10):
        phone_number += (str(random.randint(0, 9)))
        if x == 2 or x == 5:
            phone_number += '-'

    return phone_number
