#!/usr/bin/python3

import data.formats
import generators.user_details
import random


def generate_users_file(min_user_id=1, max_user_id=101, file_format=data.formats.Files.sql):
    file_name = '/home/cahlien/Documents/eastcoders'
    file_name += '.sql' if file_format == data.formats.Files.sql else ''
    file_name += '.txt' if file_format == data.formats.Files.txt else ''

    outfile = open(file_name, 'w')

    for x in range(min_user_id, max_user_id):
        user = generate_user(x)
        outfile.write(user + '\n')

    outfile.close()


def generate_user(primary_key):
    gender = generators.user_details.generate_gender()
    first_name = generators.user_details.generate_given_name(gender)
    last_name = generators.user_details.generate_surname()
    dob = generators.user_details.generate_date(1900, 2021)
    street_address = generators.user_details.generate_street_address()
    city = generators.user_details.generate_city()
    state = generators.user_details.generate_state()
    zip_code = generators.user_details.generate_zipcode()
    email = generators.user_details.generate_email(first_name, last_name)
    password = 'tempPass'
    join_date = generators.user_details.generate_date(2021, 2021)
    role_id = random.randint(1, 2)
    phone_number = generators.user_details.generate_phone_number()

    values = str(primary_key) + ", TRUE, '" + city + "', '" + state + "', " + street_address + "', " + str(
        zip_code) + ", '" + password + "', '" + join_date + "', '" + dob + "', '" + email + "', '" + \
        first_name + "', '" + last_name + "', '" + phone_number + "', " + str(role_id)

    query = assemble_query(values)
    print(query)
    return query


def assemble_query(values):
    query = "insert into users values(" + values + ");"
    return query
